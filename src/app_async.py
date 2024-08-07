from flask import Flask, request, jsonify, render_template, render_template_string, send_from_directory
from markupsafe import Markup

from flask_socketio import SocketIO, emit
import eventlet
from src.helper import MyTradingApp  # Assuming these imports are used elsewhere
from src.flex_query import initiate_flex_query_report, download_flex_query_report
#from src.compile_documentation import compile_documentation
from src.db.data_access import create_connection, get_latest_dividend_date, count_dividend_records, insert_dividend
from src.db.data_access import save_time_entry, add_task, get_dummy_today_tasks, mark_tasks_as_closed
from .data_sync import compare_dividend_data
from src.ib_data_fetcher import fetch_dividends_from_ib, fetch_trades_from_ib
from .db.data_access import fetch_dividends_from_db, fetch_all_trades, insert_dividend_if_not_exists, insert_trade_if_not_exists, fetch_dividends_by_quarter, get_dividend_date_range, get_trades_by_symbol, save_task_diary_entry
from .db.data_access import fetch_task_diary_entries, fetch_time_entries, fetch_tasks_for_date, mark_tasks_as_selected
from .db.data_access import validate_pending_status, revert_task_statuses, fetch_forgotten_tasks
from .db.data_access import insert_backlog_entry, fetch_backlog_entries, move_task_to_backlog, move_task_to_time_entries

from .db.data_access import add_task_to_backlog, delete_unified_inbox_item, update_unified_inbox_item, fetch_unified_inbox_items, insert_unified_inbox_item
from src.file_operations import write_transactions_to_file
from src.trade_processing import generate_description_for_trade, filter_and_organize_trades
from flask import request
from flask import current_app
from flask_cors import CORS

import os
import markdown
import re
from werkzeug.utils import secure_filename
import logging
import glob
from datetime import date, timedelta


def create_async_app(config):

  
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
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
    app.logger.info("app_async.py is being executed....")

    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/index.html')
    def index_file():
        return render_template('index.html')
    
    @app.route('/task_diary')
    def task_diary():
        app.logger.info("task_diary....")
        return render_template('task_diary.html')
    
    @app.route('/task-diary', methods=['POST'])
    def add_task_diary_entry():
        app.logger.info("add_task_diary_entry....")
        data = request.json
        app.logger.info(f"Received data: {data}")
        
        if not "tasks" in data or not isinstance(data["tasks"], list):
            app.logger.error("Invalid data received: %s", data)
            return jsonify({"error": "Invalid data"}), 400
        
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                for task in data["tasks"]:
                    app.logger.info(f"Saving task: {task}")
                    # Provide default empty strings for start_time and end_time if they are missing
                    date = task.get("date", "").strip()
                    start_time = task.get("start_time", "")
                    end_time = task.get("end_time", "")
                    task_description = task.get("task_description", "").strip()

                    # Ensure date and task_description are not empty
                    if not date or not task_description:
                        app.logger.error("Invalid task data: %s", task)
                        return jsonify({"error": "Invalid task data"}), 400

                    result = save_time_entry(conn, date, start_time, end_time, task_description)
                    if result is None:
                        app.logger.error("Failed to save task: %s", task)
                        return jsonify({"error": "Failed to save task"}), 500

                conn.close()
                app.logger.info("Successfully saved task diary entries")
                return jsonify({"success": True}), 201
            else:
                app.logger.error("Database connection failed.")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error("Error saving task diary entry: %s", str(e))
            return jsonify({"error": str(e)}), 500

    @app.route('/get-task-diary-entries', methods=['GET'])
    def get_task_diary_entries():
        app.logger.info("get_task_diary_entries ...")

        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                app.logger.info("fetch entries from task diary ...")
                # Fetch task diary entries
                diary_entries = fetch_task_diary_entries(conn)
                app.logger.info(f"Fetched diary entries: {diary_entries}")
                # Fetch time entries
                time_entries = fetch_time_entries(conn)
                app.logger.info(f"Fetched time entries: {time_entries}")
                conn.close()

                # Create a dictionary to hold tasks by date
                tasks_by_date = {}
                for entry in time_entries:
                    date = entry['date']
                    if date not in tasks_by_date:
                        tasks_by_date[date] = []
                    tasks_by_date[date].append(entry['task_description'])

                # Format the diary entries with their associated tasks
                formatted_entries = []
                for entry in diary_entries:
                    date = entry['date']
                    formatted_entries.append({
                        "date": date,
                        "tasks": tasks_by_date.get(date, []),
                        "reflections": entry['reflections']
                    })

                app.logger.info(f"Formatted entries to be returned: {formatted_entries}")
                return jsonify(formatted_entries), 200
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error fetching task diary entries: {str(e)}")
            return jsonify({"error": str(e)}), 500

 
    
    @app.route('/time-entry', methods=['POST'])
    def handle_time_entry():
        data = request.json
        # Validate data
        if not all(key in data for key in ("date", "start_time", "end_time", "task_description")):
            return jsonify({"error": "Invalid data"}), 400
        
        try:
            # Directly save the time entry
            conn = create_connection(app.config['db_path'])
            if conn:
                entry_id = save_time_entry(conn, data)
                conn.close()
                return jsonify({"success": True, "entry_id": entry_id}), 201
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/tasks', methods=['GET'])
    def get_tasks_for_date():
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                date = request.args.get('date')
                tasks = fetch_tasks_for_date(conn, date)
                conn.close()
                return jsonify(tasks), 200
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        


    @app.route('/tasks/add', methods=['POST'])
    def add_task_route():
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                date = request.json.get('date')
                start_time = request.json.get('start_time')
                end_time = request.json.get('end_time')
                task_description = request.json.get('task_description')
                add_task(conn, date, start_time, end_time, task_description)
                conn.close()
                return jsonify({"message": "Task added"}), 200
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        


    @app.route('/tasks/today', methods=['GET'])
    def get_today_tasks_endpoint():
        app.logger.info(f"get_today_tasks_endpoint")
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                today = date.today().isoformat()
                app.logger.info(f"Retrieving tasks for today: {today}")
                tasks = fetch_tasks_for_date(conn, today)
                conn.close()
                app.logger.debug(f"Tasks retrieved: {tasks}")
                return jsonify(tasks), 200
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error retrieving tasks: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/tasks/tomorrow', methods=['GET'])
    def get_tomorrows_tasks_endpoint():
        app.logger.info(f"get_tomorrows_tasks_endpoint")
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                tomorrow = (date.today() + timedelta(days=1)).isoformat()
                app.logger.info(f"Retrieving tasks for tomorrow: {tomorrow}")
                tasks = fetch_tasks_for_date(conn, tomorrow)
                conn.close()
                app.logger.debug(f"Tasks retrieved: {tasks}")
                return jsonify(tasks), 200
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error retrieving tasks: {str(e)}")
            return jsonify({"error": str(e)}), 500


    @app.route('/tasks/close', methods=['POST'])
    def close_tasks_endpoint():
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                task_ids = request.json.get('task_ids')
                app.logger.debug(f"Received task IDs for closing: {task_ids}")

                if not task_ids:
                    app.logger.error("Task IDs are required but not provided.")
                    return jsonify({"error": "Task IDs are required"}), 400
                
                # Convert task IDs to integers
                try:
                    task_ids = [int(task_id) for task_id in task_ids]
                except ValueError as e:
                    app.logger.error(f"Error converting task IDs to integers: {e}")
                    return jsonify({"error": "Invalid task IDs"}), 400
                
                app.logger.debug(f"Converted task IDs to integers: {task_ids}")

                valid_ids = validate_pending_status(conn, task_ids)
                if len(valid_ids) != len(task_ids):
                    app.logger.error(f"Some tasks are not in the selected state: {task_ids}")
                    return jsonify({"error": "Some tasks are not in the selected state"}), 400

                app.logger.info(f"Closing tasks: {task_ids}")
                mark_tasks_as_closed(conn, task_ids)
                conn.close()
                return jsonify({"message": "Tasks marked as locked"}), 200
            else:
                app.logger.error("Database connection failed.")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error closing tasks: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/tasks/select', methods=['POST'])
    def select_tasks_for_date():
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                data = request.json
                task_ids = data.get('task_ids')
                
                if not task_ids:
                    app.logger.error("Task IDs are required but not provided")
                    return jsonify({"error": "Task IDs are required"}), 400

                app.logger.info(f"Marking tasks as selected: {task_ids}")
                valid_ids = validate_pending_status(conn, task_ids)
                app.logger.debug(f"Valid IDs: {valid_ids}")

                if len(valid_ids) != len(task_ids):
                    invalid_ids = set(task_ids) - set(valid_ids)
                    app.logger.error(f"Some tasks are not in the pending state: {invalid_ids}")
                    return jsonify({"error": f"Some tasks are not in the pending state: {invalid_ids}"}), 400

                mark_tasks_as_closed(conn, task_ids)
                app.logger.info(f"Tasks marked as closed: {task_ids}")
                conn.close()
                return jsonify({"message": "Tasks marked as selected"}), 200
            else:
                app.logger.error("Database connection failed")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error selecting tasks: {str(e)}")
            return jsonify({"error": str(e)}), 500


    @app.route('/tasks/forgotten', methods=['GET'])
    def get_forgotten_tasks_endpoint():
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                forgotten_tasks = fetch_forgotten_tasks(conn)
                app.logger.debug(f"Forgotten tasks retrieved: {forgotten_tasks}")
                conn.close()
                return jsonify(forgotten_tasks), 200
            else:
                app.logger.error("Database connection failed")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error retrieving forgotten tasks: {str(e)}")
            return jsonify({"error": str(e)}), 500




    @app.route('/tasks/revert', methods=['POST'])
    def revert_tasks_endpoint():
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                task_ids = request.json.get('task_ids')
                if not task_ids:
                    return jsonify({"error": "Task IDs are required"}), 400
                
                app.logger.info(f"Reverting tasks to selected state: {task_ids}")
                revert_task_statuses(conn, task_ids)
                conn.close()
                return jsonify({"message": "Tasks reverted to selected state"}), 200
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error reverting tasks: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/time_management.html')
    def time_management():
        return render_template('time_management.html')
    
    @app.route('/todays_tasks')
    def todays_tasks():
        return render_template('todays_tasks.html')
    
    @app.route('/get-todays-tasks', methods=['GET'])
    def get_todays_tasks():
        app.logger.info("Fetching today's tasks")
        # will be fixed later
        return 0
    
    @app.route('/backlog')
    def backlog():
        return render_template('backlog.html')
    
    @app.route('/tasks/backlog', methods=['GET'])
    def get_backlog_tasks_endpoint():
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                tasks = fetch_backlog_entries(conn)
                conn.close()
                app.logger.debug(f"Backlog tasks retrieved: {tasks}")
                return jsonify(tasks), 200
            else:
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error retrieving backlog tasks: {str(e)}")
            return jsonify({"error": str(e)}), 500


    @app.route('/move_to_backlog', methods=['POST'])
    def move_tasks_to_backlog_endpoint():
        app.logger.info("Received request to move tasks to backlog")
        try:
            # Create a database connection
            conn = create_connection(app.config['db_path'])
            if conn:
                app.logger.info("Database connection established")

                # Retrieve JSON data from the request
                data = request.json
                app.logger.debug(f"Received data: {data}")

                # Extract task descriptions from the received data
                task_descriptions = data.get('task_descriptions')

                # Validate the task descriptions
                if not isinstance(task_descriptions, list) or not task_descriptions:
                    app.logger.warning("Task descriptions are required and must be a list")
                    return jsonify({"error": "Task descriptions are required and must be a list"}), 400

                success = True

                # Process each task description
                for desc in task_descriptions:
                    # Add the task to the backlog
                    if not add_task_to_backlog(conn, desc):
                        success = False
                        app.logger.error(f"Failed to add task to backlog: {desc}")

                # Close the database connection
                conn.close()

                # Return appropriate response based on success or failure
                if success:
                    app.logger.info("Tasks moved to backlog successfully")
                    return jsonify({"message": "Tasks moved to backlog successfully"}), 200
                else:
                    app.logger.error("Failed to move some tasks to backlog")
                    return jsonify({"error": "Failed to move some tasks to backlog"}), 500
            else:
                app.logger.error("Database connection failed")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error moving tasks to backlog: {str(e)}")
            return jsonify({"error": str(e)}), 500




    # Unified Inbox Endpoints

    @app.route('/unified-inbox', methods=['GET'])
    def get_unified_inbox_items():
        app.logger.info("Received request to fetch all items from the Unified Inbox.")
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                items = fetch_unified_inbox_items(conn)
                conn.close()
                app.logger.info(f"Fetched {len(items)} items from the Unified Inbox.")
                return jsonify(items), 200
            else:
                app.logger.error("Database connection failed.")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error fetching items from the Unified Inbox: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/unified-inbox', methods=['POST'])
    def add_unified_inbox_item():
        app.logger.info("Received request to add item to unified inbox")
        try:
            data = request.json
            description = data.get('description')
            
            app.logger.debug(f"Received data: {data}")

            if not description:
                app.logger.error("Description is required")
                return jsonify({"error": "Description is required"}), 400

            conn = create_connection(app.config['db_path'])
            if conn:
                item_id = insert_unified_inbox_item(conn, description)
                conn.close()
                app.logger.info(f"Item added to unified inbox with id: {item_id}")
                return jsonify({"id": item_id, "description": description}), 201
            else:
                app.logger.error("Database connection failed")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error adding item to inbox: {str(e)}")
            return jsonify({"error": str(e)}), 500


    @app.route('/unified-inbox/<int:item_id>', methods=['PUT'])
    def update_unified_inbox_item_route(item_id):
        app.logger.info(f"Received request to update item with ID: {item_id}")
        try:
            data = request.json
            description = data.get('description')
            if not description:
                app.logger.warning("No description provided in the request.")
                return jsonify({"error": "Description is required"}), 400

            conn = create_connection(app.config['db_path'])
            if conn:
                update_unified_inbox_item(conn, item_id, description)
                conn.close()
                app.logger.info(f"Successfully updated item with ID: {item_id} to new description: '{description}'")
                return jsonify({"id": item_id, "description": description}), 200
            else:
                app.logger.error("Database connection failed.")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error updating item in the Unified Inbox: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @app.route('/unified-inbox/<int:item_id>', methods=['DELETE'])
    def delete_unified_inbox_item_route(item_id):
        app.logger.info(f"Received request to delete item with ID: {item_id}")
        try:
            conn = create_connection(app.config['db_path'])
            if conn:
                delete_unified_inbox_item(conn, item_id)
                conn.close()
                app.logger.info(f"Successfully deleted item with ID: {item_id}")
                return jsonify({"message": "Item deleted"}), 200
            else:
                app.logger.error("Database connection failed.")
                return jsonify({"error": "Database connection failed"}), 500
        except Exception as e:
            app.logger.error(f"Error deleting item from the Unified Inbox: {str(e)}")
            return jsonify({"error": str(e)}), 500

        



    @app.route('/select-tasks', methods=['GET', 'POST'])
    def select_tasks():
        sample_backlog = [
            {"id": 1, "task_description": "Review project proposal"},
            {"id": 2, "task_description": "Write report"},
            {"id": 3, "task_description": "Team meeting"}
        ]
        if request.method == 'POST':
            task_ids = request.form.getlist('task_ids')
            selected_tasks = [task for task in sample_backlog if str(task["id"]) in task_ids]
            return f'Tasks added to the closed list for today: {selected_tasks}'
        
        return render_template('select_tasks.html', backlog=sample_backlog)

    @app.route('/closed-list')
    def closed_list():
        return render_template('closed_lists.html')
    
    @app.route('/closed-lists')
    def closed_lists():
        return render_template('closed_lists.html')
    
    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory(app.static_folder, filename)
    
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

    @socketio.on('fetch-trades')
    def handle_fetch_trades(data):
        logging.info("handle_fetch_trades....")
        token = data.get('token')
        # Optionally, you can use different parameters to distinguish between trade and dividend data fetching
        socketio.start_background_task(target=process_trades_async, token=token, config=app.config)

    def process_trades_async(token, config):
        logging.info("process_trades_async....")
        with app.app_context():
            conn = None  # Ensuring conn is defined regardless of the try block's outcome
            logging.info("Starting trade processing...")
            socketio.emit('update', {'message': 'Starting to process trades...'}, namespace='/')
            try:
                # Emit the Flex Query ID being used to fetch trade data
                trade_query_id = config['flex_queries']['trades']
                logging.info("Fetching trades...")
                socketio.emit('update', {'message': f'Fetching Trades with Query ID: {trade_query_id}'}, namespace='/')
                    # Fetch trade data from IB
                trades = fetch_trades_from_ib(token, config)
                if not trades:
                    socketio.emit('update', {'message': 'No trade data found to process.'}, namespace='/')
                    return

                logging.info("Creating connection...")
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

    @app.route('/get-trades-for-stock', methods=['POST'])
    def handle_fetch_trades():
        stock_symbol = request.form.get('stockSymbol')
        file_name = request.form.get('fileName')
        
        socketio.start_background_task(process_trades_for_stock_async, stock_symbol=stock_symbol, file_name=file_name, app_config=app.config)

        return render_template_string("<p>Fetching trades for the stock symbol in the background. Results will be saved to " + file_name + ".</p>")



    def process_trades_for_stock_async(stock_symbol, file_name, app_config):
        db_path = app_config['db_path']

        if not stock_symbol:
            print("Stock symbol not provided.")
            return
        
        try:
            conn = create_connection(db_path)
            trades = get_trades_by_symbol(conn, stock_symbol)
            conn.close()

            # Update this part to filter and organize trades for description generation
            grouped_trades = filter_and_organize_trades(trades)
            
            with open(file_name, 'w') as file:
                for key, group in grouped_trades.items():
                    # Print all related (non-ExchTrade) entries for context
                    for related_trade in group['related']:
                        file.write(str(related_trade) + "\n")
                    # If an ExchTrade entry exists, print it and its description
                    if group['exchTrade']:
                        file.write(str(group['exchTrade']) + "\n")
                        description = generate_description_for_trade(group['exchTrade'])
                        file.write(description + "\n\n")
            
            # Notify via WebSocket (Flask-SocketIO) that processing is finished
            socketio.emit('processing_finished', {'message': 'Trades processing finished', 'file': file_name})
        except Exception as e:
            print({"error": str(e)})



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
        # Generate the TOC, including the OVERVIEW.md at the beginning
        logging.info(f"Generating TOC....")
        try:
            # Initialize toc_entries with actual entries instead of using ...
            # If you have more sections to add, include them as tuples similar to the provided ones
            toc_entries = [
                ("OVERVIEW.md", [
                    ("1", "Project Structure Overview"), 
                    ("2", "Environment Setup")
                    # Add additional sections as needed here, in the form of ("level", "Title"),
                ])
            ]
            toc = generate_toc_for_directory(directory_path)
            toc_entries.extend(toc)  # Incorporate other documentation files into the TOC
            
            toc_content = "# Table of Contents\n\n"
            for filename, headings in toc_entries:
                logging.info(f"TOC next entry {filename}")
                anchor_name = filename.replace(' ', '-').lower().replace('.md', '')
                toc_content += f"- [{filename.replace('.md', '')}](#{anchor_name})\n"
                for level, heading in headings:
                    level = int(level)  # Convert level to integer if it's not already
                    indent = "  " * level
                    toc_content += f"{indent}- {heading}\n"


            # Then, compile the document content
            compiled_content = f"# {title}\n\n{toc_content}\n\n"    

            
            # Key Change: Ensure OVERVIEW.md content is included after the TOC
            # Adjust the overview_path to match the actual location of OVERVIEW.md
            overview_path = os.path.join(directory_path, '../OVERVIEW.md')
            if os.path.exists(overview_path):
                with open(overview_path, 'r', encoding='utf-8') as overview_file:
                    logging.info("Adding OVERVIEW.md content....")
                    compiled_content += f"<a id='overview'></a>\n"
                    compiled_content += overview_file.read() + "\n\n"
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

        logging.info(f"Compiling documents ....")
        markdown_files = glob.glob(f"{directory_path}/*.md")
        for file_path in sorted(markdown_files):
            if "OVERVIEW.md" in file_path:
                continue  # Skip OVERVIEW.md since it's already included
            with open(file_path, 'r', encoding='utf-8') as file:
                # Consider adding anchors for each file and heading for TOC links
                file_basename = os.path.basename(file_path).replace(' ', '-').lower().replace('.md', '')
                compiled_content += f"<a id='{file_basename}'></a>\n"
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
        logging.info(f"Generating TOC for directory {directory_path}....")
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
    
    @app.route('/view-book', methods=['GET', 'POST'])
    def view_book():
        # Initialize a variable to hold the content that will be rendered
        book_content_html_safe = ""
        # Check if the request method is POST
        if request.method == 'POST':
            # Extract filePath from the form data
            file_path = request.form['filePath']
            # Ensure the file exists before attempting to open
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    book_content_md = file.read()
                book_content_html = markdown.markdown(book_content_md)
                book_content_html_safe = Markup(book_content_html)
            else:
                # If the file doesn't exist, prepare an error message
                book_content_html_safe = Markup("<p>File not found.</p>")
        
        # The HTML template remains largely the same
        html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Book</title>
</head>
<body>
    <h1>The Book</h1>
    {{ content }}
    <form action="/view-book" method="post">
        <label for="filePath">File Path:</label>
        <input type="text" id="filePath" name="filePath">
        <br>
        <input type="submit" value="View Document">
    </form>
</body>
</html>"""

        return render_template_string(html_template, content=book_content_html_safe)

    return app, socketio











