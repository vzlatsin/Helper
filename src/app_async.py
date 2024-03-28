from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import eventlet
from src.helper import MyTradingApp  # Assuming these imports are used elsewhere
from src.flex_query import initiate_flex_query_report, download_flex_query_report
#from src.compile_documentation import compile_documentation
from src.db.data_access import create_connection, get_latest_dividend_date, count_dividend_records, insert_dividend
from .data_sync import compare_dividend_data
from src.ib_data_fetcher import fetch_dividends_from_ib
from .db.data_access import fetch_dividends_from_db, insert_dividend_if_not_exists, fetch_dividends_by_quarter
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
                dividends = fetch_dividends_from_ib(token, config)
                # Process dividends (e.g., database operations)
                # Make sure this processing doesn't block; consider breaking up work or using eventlet for network/db operations
            except Exception as e:
                socketio.emit('update', {'message': f'Error processing dividends: {str(e)}'}, namespace='/')
            else:
                socketio.emit('update', {'message': 'Dividend processing complete'}, namespace='/')
    
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
        markdown_files = glob.glob(f"{directory_path}/*.md")
        compiled_content = f"# {title}\n\n"

        for file_path in sorted(markdown_files):
            with open(file_path, 'r', encoding='utf-8') as file:
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









