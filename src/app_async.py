from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import eventlet
from src.helper import MyTradingApp  # Assuming these imports are used elsewhere
from src.flex_query import initiate_flex_query_report, download_flex_query_report
#from src.compile_documentation import compile_documentation
from src.db.data_access import create_connection, get_latest_dividend_date, count_dividend_records, insert_dividend
from .data_sync import compare_dividend_data
from src.ib_data_fetcher import fetch_dividends_from_ib, fetch_trades_from_ib
from .db.data_access import fetch_dividends_from_db, fetch_all_trades, insert_dividend_if_not_exists, insert_trade_if_not_exists, fetch_dividends_by_quarter, get_dividend_date_range
from src.file_operations import write_transactions_to_file
from flask import request
from flask import current_app
from flask_cors import CORS

import os
import markdown
import re
from werkzeug.utils import secure_filename
import logging
import glob


def create_async_app(config):
    app = Flask(__name__, template_folder='../templates')
    CORS(app)  # Enable CORS if it's required for your async app

    # Here, default configurations are set first.
    default_config = {'TESTING': True, 'DEBUG': True}
    app.config.update(default_config)
    
    # Then, the externally loaded configuration is applied.
    # This allows your external configuration to override the defaults as needed.
    if config:
        app.config.update(config)

    # Initialize SocketIO with your app
    socketio = SocketIO(app, logger=True, engineio_logger=True)

    
    # If you use trading_app in your async version, initialize it here.
    # Ensure that any use of trading_app is compatible with asynchronous operations.
    trading_app = MyTradingApp()

    @app.route('/async-route')
    async def async_route():
        # Emit a message directly from the route to all connected clients
        emit('update', {'message': 'Direct emit from async-route'}, namespace='/', broadcast=True)
        return 'Async route response'


    async def async_function():
        # Example async function
        eventlet.sleep(1)
        return 'Async function result'
    
 
    @app.route('/fetch-financial-data-async')
    def show_financial_data_form():
        return render_template('fetch_financial_data_async.html')
    
    @socketio.on('fetch_dividends')
    def handle_fetch_dividends(data):
        # Validate and extract data
        token = data.get('token')
        # Start the background task to fetch and process dividends without blocking
        socketio.start_background_task(target=process_dividends_async, token=token, config=app.config)

    def process_dividends_async(token, config):
        # This function runs in a background thread; async syntax isn't directly applicable here
        with app.app_context():
            # Emit status update to the client
            socketio.emit('update', {'message': 'Starting to process dividends...'}, namespace='/')
            try:
                # Synchronously fetch dividend data from IB
                # dividends = fetch_dividends_from_ib(token, config)
                # Process dividends (e.g., database operations)
                result = process_dividends(token, config)
                # Make sure this processing doesn't block; consider breaking up work or using eventlet for network/db operations
            except Exception as e:
                socketio.emit('update', {'message': f'Error processing dividends: {str(e)}'}, namespace='/')
            else:
                socketio.emit('update', {'message': 'Dividend processing complete'}, namespace='/')
    
    def process_dividends(token, app_config):
        app.logger.info(f"Processing dividends: Token: {token}")
        db_path = app_config['db_path']
        try:
            conn = create_connection(db_path)
            if conn is None:
                raise Exception("Failed to connect to the database.")
            # Before insertion
            initial_count = count_dividend_records(conn)
            print(f"Get dividend range...")
            date_range_start, date_range_end = get_dividend_date_range(conn)
            socketio.emit('update', {'message': f'Before insertion - Count: {initial_count}, Date range: {date_range_start} to {date_range_end}'}, namespace='/')

            transactions = fetch_dividends_from_ib(token, app_config)
            for t in transactions:
                try:
                    insert_dividend_if_not_exists(conn, t['symbol'], t['amount'], t['ex_date'], t['pay_date'])
                except Exception as e:
                    app.logger.error(f"Failed to insert dividend for {t['symbol']}: {e}")
            
            # After insertion
            final_count = count_dividend_records(conn)
            _, last_date = get_dividend_date_range(conn)
            socketio.emit('update', {'message': f'After insertion - Count: {final_count}, Last dividend date: {last_date}'}, namespace='/')
        except Exception as e:
            app.logger.error(f"Error processing dividends: {e}")
        finally:
            if conn:
                conn.close()

    @socketio.on('fetch_trades')
    def handle_fetch_trades(data):
        token = data.get('token')
        # Optionally, you can use different parameters to distinguish between trade and dividend data fetching
        socketio.start_background_task(target=process_trades_async, token=token, config=app.config)

    def process_trades_async(token, config):
        with app.app_context():
            conn = None  # Ensuring conn is defined regardless of the try block's outcome
            print(f"Starting trade processing...")
            socketio.emit('update', {'message': 'Starting to process trades...'}, namespace='/')
            try:
                # Emit the Flex Query ID being used to fetch trade data
                trade_query_id = config['flex_queries']['trades']
                print(f"Fetching trades...")
                socketio.emit('update', {'message': f'Fetching Trades with Query ID: {trade_query_id}'}, namespace='/')
                    # Fetch trade data from IB
                trades = fetch_trades_from_ib(token, config)
                if not trades:
                    socketio.emit('update', {'message': 'No trade data found to process.'}, namespace='/')
                    return

                print(f"Creating connection...")
                conn = create_connection(config['db_path'])
                if conn is None:
                    raise Exception("Failed to connect to the database.")
                
                # Process each trade
                for trade in trades:
                    trade_data = {
                        'symbol': trade['symbol'], 
                        'dateTime': trade.get('dateTime', None),  # Using .get for optional fields provides a default value of None if the key doesn't exist
                        'putCall': trade.get('putCall', None), 
                        'transactionType': trade['transactionType'], 
                        'quantity': trade['quantity'], 
                        'tradePrice': trade.get('tradePrice', None),
                        'closePrice': trade.get('closePrice', None),
                        'cost': trade.get('cost', None),
                        'origTradePrice': trade.get('origTradePrice', None),
                        'origTradeDate': trade.get('origTradeDate', None),
                        'buySell': trade.get('buySell', None),
                        'orderTime': trade.get('orderTime', None),
                        'openDateTime': trade.get('openDateTime', None),
                        'assetCategory': trade.get('assetCategory', None),
                        'strike': trade.get('strike', None),
                        'expiry': trade.get('expiry', None),
                        'tradeDate': trade.get('tradeDate', None)
                    }

                    insert_trade_if_not_exists(conn, trade_data)
                
                socketio.emit('update', {'message': 'Trade processing complete'}, namespace='/')
            except Exception as e:
                socketio.emit('update', {'message': f'Error processing trades: {str(e)}'}, namespace='/')
            finally:
                if conn:
                    conn.close()

    
    def process_trades(token, app_config):
        app.logger.info("Processing trades...")
        db_path = app_config['db_path']
        try:
            conn = create_connection(app_config['db_path'])
            if conn is None:
                raise Exception("Failed to connect to the database.")
            
            trades = fetch_trades_from_ib(token, app_config)
            for trade in trades:
                insert_trade_if_not_exists(conn, **trade)
            
            app.logger.info("Trade processing complete.")
        except Exception as e:
            app.logger.error(f"Error processing trades: {e}")
        finally:
            if conn:
                conn.close()

    # Route to render the documentation compilation page
    @app.route('/compile-documentation')
    def render_compile_documentation_page():
        return render_template('compile_documentation.html')

    @app.route('/compile-documentation', methods=['POST'])
    def handle_compile_documentation():
        title = request.form.get('documentationTitle')
        docs_path = request.form.get('docsPath')
        output_path = request.form.get('outputPath')

        # Sanitize and validate the docs_path and output_path here as needed

        try:
            compiled_doc_path = compile_docs_from_directory(docs_path, output_path, title)
            # Respond with success and possibly the path or a link to the compiled document
            return jsonify({"message": "Documentation compiled successfully!", "path": compiled_doc_path})
        except Exception as e:
            # Log the error and respond accordingly
            return jsonify({"error": str(e)}), 500

    def compile_docs_from_directory(directory_path, output_path, title):
        # First, generate the TOC
        toc = generate_toc_for_directory(directory_path)
        toc_content = "# Table of Contents\n\n"
        for entry in toc:
            filename, headings = entry
            toc_content += f"- [{filename}](#{filename.replace(' ', '-').lower()})\n"
            for level, heading in headings:
                indent = "  " * (level - 1)
                toc_content += f"{indent}- [{heading}](#{heading.replace(' ', '-').lower()})\n"

        # Then, compile the document content
        compiled_content = f"# {title}\n\n{toc_content}\n\n"
        markdown_files = glob.glob(f"{directory_path}/*.md")
        for file_path in sorted(markdown_files):
            with open(file_path, 'r', encoding='utf-8') as file:
                # You may want to insert anchors corresponding to the TOC here
                compiled_content += file.read() + "\n\n"
        
        # Save the compiled content to the specified output path
        with open(output_path, 'w', encoding='utf-8') as compiled_file:
            compiled_file.write(compiled_content)
        
        return output_path


    def compile_documentation(file_paths, title):
        compiled_content = ""
        output_path = os.path.join('compiled_docs', f"{title}.md")
        
        if not os.path.exists('compiled_docs'):
            os.makedirs('compiled_docs')
            logging.info(f"Created directory for compiled documentation.")

        try:
            for file_path in file_paths:
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    logging.info(f"Reading file {file_path}")
                    compiled_content += md_file.read() + "\n\n"
            
            with open(output_path, 'w', encoding='utf-8') as compiled_file:
                logging.info(f"Writing compiled content to {output_path}")
                compiled_file.write(compiled_content)
            
            return output_path
        except Exception as e:
            logging.error(f"Failed to compile documentation: {e}")
            raise


    # Function to compile documentation asynchronously
    def compile_documentation_async(title, files):
        with app.app_context():
            socketio.emit('update', {'message': 'Starting documentation compilation...'}, namespace='/')
            try:
                # Compile documentation into a book
                compile_documentation(title, files)
            except Exception as e:
                socketio.emit('update', {'message': f'Error compiling documentation: {str(e)}'}, namespace='/')
            else:
                socketio.emit('update', {'message': 'Documentation compilation complete'}, namespace='/')

    def extract_headings_from_md(file_path):
        """
        Extracts headings from a markdown file located at file_path.
        
        :param file_path: Path to the markdown file.
        :return: A list of tuples containing (level, heading title).
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as md_file:
                md_content = md_file.read()
        except IOError:
            print(f"Error opening or reading file: {file_path}")
            return []

        heading_re = re.compile(r'^(#+)\s*(.+)', re.MULTILINE)
        return [(len(m.group(1)), m.group(2)) for m in heading_re.finditer(md_content)]

    def generate_toc_for_directory(directory_path):
        toc = []
        for filename in sorted(os.listdir(directory_path)):
            if filename.endswith('.md'):
                file_path = os.path.join(directory_path, filename)
                headings = extract_headings_from_md(file_path)
                # Only include level 1 and level 2 headings to simplify the TOC
                headings = [h for h in headings if h[0] <= 2]
                # Append a tuple of filename (without extension) and the headings list
                toc.append((filename.replace('.md', ''), headings))
        return toc



    @app.route('/documentation-index')
    def documentation_index():
        docs_path = os.path.join(os.getcwd(), 'docs', 'scripts')
        toc = generate_toc_for_directory(docs_path)
        return render_template('documentation_index.html', toc=toc)

    
    @app.route('/documentation/<filename>')
    def serve_documentation(filename):
        # Construct the path to the requested documentation file
        docs_path = os.path.join(os.getcwd(), 'docs', 'scripts')
        file_path = os.path.join(docs_path, filename)

        # Check if the requested file exists
        if os.path.isfile(file_path):
            # Read the content of the file
            with open(file_path, 'r') as file:
                content = file.read()

            # Convert markdown content to HTML
            html_content = markdown.markdown(content)

            return html_content
        else:
            # If the file does not exist, return a 404 error
            return 'File not found', 404
    
    
    return app, socketio









