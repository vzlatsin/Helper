from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
import eventlet
from src.helper import MyTradingApp  # Assuming these imports are used elsewhere
from src.flex_query import initiate_flex_query_report, download_flex_query_report

from src.db.data_access import create_connection, get_latest_dividend_date, count_dividend_records, insert_dividend
from .data_sync import compare_dividend_data
from src.ib_data_fetcher import fetch_dividends_from_ib
from .db.data_access import fetch_dividends_from_db, insert_dividend_if_not_exists, fetch_dividends_by_quarter
from src.file_operations import write_transactions_to_file
from flask import request
from flask import current_app

def create_async_app(config):
    app = Flask(__name__, template_folder='../templates')
    app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for session management and security
    socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

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
    
    @app.route('/fetch-financial-data', methods=['POST'])
    async def fetch_financial_data():
        # Extract parameters from the request
        token = request.form.get('token')
        data_type = request.form.get('data_type')

        # Instead of processing right away, emit an event to start the background task
        socketio.start_background_task(target=process_data, token=token, data_type=data_type, config=app.config)

                # Immediately return a response indicating the task has started
        return jsonify({"message": "Processing started"})
    
    def process_data(token, data_type, config):
        # Assuming this function is invoked as a background task
        with app.app_context():  # Change current_app to app
                socketio.emit('update', {'message': 'Starting to process data...'}, namespace='/')
                eventlet.sleep(5)  # Simulate some processing time
                socketio.emit('update', {'message': 'Data processing complete'}, namespace='/')


    @socketio.on('start_activity')
    def handle_start_activity(data):
        token = data['token']
        data_type = data['data_type']
        # Use 'socketio' to start the background task
        socketio.start_background_task(process_data, token=token, data_type=data_type, config=app.config)

    return app, socketio









