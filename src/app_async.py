from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import eventlet
from src.helper import MyTradingApp  # Assuming these imports are used elsewhere
from src.flex_query import initiate_flex_query_report, download_flex_query_report
from src.compile_documentation import compile_documentation
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

    # Route to handle documentation compilation form submission
    @socketio.on('compile_documentation')
    def handle_compile_documentation(data):
        title = data.get('title')
        files = data.get('files')
        if title and files:
            socketio.start_background_task(target=compile_documentation_async, title=title, files=files)

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



    @app.route('/documentation-index')
    def documentation_index():
        # Get a list of documentation files in the 'docs/src' directory
        docs_path = os.path.join(os.getcwd(), 'docs', 'scripts')
        documentation_files = [f for f in os.listdir(docs_path) if os.path.isfile(os.path.join(docs_path, f))]

        # Generate the documentation index HTML
        index_html = '<h1>Documentation Index</h1>'
        index_html += '<ul>'
        for file_name in documentation_files:
            index_html += f'<li><a href="/documentation/{file_name}">{file_name}</a></li>'
        index_html += '</ul>'

        return index_html


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









