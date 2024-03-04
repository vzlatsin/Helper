# app.py
from flask import Flask, request, jsonify, redirect, url_for, render_template
import os
import json
from .helper import MyTradingApp
from .report_parser import parse_cash_transaction
import logging
from src.flex_query import initiate_flex_query_report, download_flex_query_report, get_query_id, get_last_dividend_date
from src.db.data_access import create_connection, get_latest_dividend_date, count_dividend_records, insert_dividend
from .data_sync import compare_dividend_data
from src.ib_data_fetcher import fetch_dividends_from_ib
from .db.data_access import fetch_dividends_from_db, insert_dividend_if_not_exists, fetch_dividends_by_quarter
from src.file_operations import write_transactions_to_file

def create_app(config):
    app = Flask(__name__, template_folder='../templates')
    trading_app = MyTradingApp()
    app.config.update(config)

    @app.route('/dividends-chart')
    def dividends_chart():
        return render_template('dividends_chart.html')
    
    @app.route('/api/dividends/by-quarter')
    def api_dividends_by_quarter():
        # Retrieve the database path from the app's configuration
        db_path = app.config['db_path']
        conn = create_connection(db_path)
        if not conn:
            return jsonify({"error": "Unable to connect to the database"}), 500

        data = fetch_dividends_by_quarter(conn)
        conn.close()
        
        # Convert data to a format that can be easily used in the frontend
        quarters = [item[0] for item in data]
        amounts = [item[1] for item in data]
        
        return jsonify(quarters=quarters, amounts=amounts)


    @app.route('/')
    def home():
        app.logger.info("Welcome!")
        logging.debug("test")
        return 'Welcome!'
        
    @app.route('/run-flex-query-form')
    def show_flex_query_form():
        return render_template('run_flex_query.html')

    @app.route('/get-dividends-form')
    def show_dividends_form():
        return render_template('get_dividends_form.html')

    @app.route('/compare-dividends-form')
    def show_compare_dividends_form():
        return render_template('compare_dividends_form.html')   
    
    @app.route('/get-dividends', methods=['POST'])
    def get_dividends():
        # Extract parameters from the request
        token = request.form.get('token')
        app.logger.info(f"Getting dividends: Token: {token}")

        # Open database connection
        db_path = app.config['db_path']  # Make sure you have DB_PATH in your config
        conn = create_connection(db_path)

        # Count the dividend records and log the count
        dividend_count = count_dividend_records(conn)
        app.logger.info(f"Total dividend records in the database: {dividend_count}")

        latest_dividend_date = get_last_dividend_date()
        app.logger.info(f"Latest dividend date: {latest_dividend_date}")

        # Fetch dividend data from IB
        transactions = fetch_dividends_from_ib(token, app.config)
        """
        query= get_query_id(latest_dividend_date, config['flex_queries'])
        logging.info(f"Query ID selected: {query}")
        # Assuming your Flex Query process involves initiating and then downloading
        app.logger.info(f"Running Flex Query with query ID: {query} Token: {token}")

        # Assuming your Flex Query process involves initiating and then downloading
        reference_code = initiate_flex_query_report(query, token)
        retry_attempts = app.config['retry_attempts']
        retry_wait = app.config['retry_wait']
        report_data = download_flex_query_report(reference_code, token, retry_attempts, retry_wait)

        transactions = parse_cash_transaction(report_data)
        """
        for t in transactions:
            # Example transaction dictionary structure: {'symbol': 'AAPL', 'amount': 0.82, 'ex_date': '2021-08-06', 'pay_date': '2021-08-13'}
            #insert_dividend_if_not_exists(conn, t[0], t[1], t[2], t[3])
            insert_dividend_if_not_exists(conn, t['symbol'], t['amount'], t['ex_date'], t['pay_date'])

            logging.info(f"Parsed transaction: {t}")

        conn.close()

        return jsonify({"status": "success", "data": "Dividends processed successfully"})
        
    @app.route('/compare-dividends', methods=['POST'])
    def compare_dividends(): 
        token = request.form.get('token')  # Assuming the token can be passed as a query parameter
        db_path = app.config['db_path']
        conn = create_connection(db_path)

        # Fetch dividends from IB and the database
        ib_dividends = fetch_dividends_from_ib(token, app.config)
        write_transactions_to_file(ib_dividends, 'ib_dividends.txt')
        db_dividends = fetch_dividends_from_db(conn)
        write_transactions_to_file(db_dividends, 'db_dividends.txt')
        

        # Perform comparison (this function needs to be implemented based on your comparison logic)
        discrepancies = compare_dividend_data(db_dividends, ib_dividends)

        conn.close()

        # Handle reporting of discrepancies (e.g., rendering a template, returning JSON)

        return jsonify({"discrepancies": discrepancies})


    @app.route('/run-flex-query', methods=['POST'])
    def run_flex_query():
        # Extract parameters from the request
        query_id = request.form.get('query_id')
        token = request.form.get('token')
        app.logger.info(f"Running Flex Query with query ID: {query_id} and Token: {token}")

        # Assuming your Flex Query process involves initiating and then downloading
        reference_code = initiate_flex_query_report(query_id, token)
        report_data = download_flex_query_report(reference_code, token)

        # Process the report data as needed, then return a response
        # This is a placeholder; adjust according to your needs
        return jsonify({"status": "success", "data": report_data})

    @app.route('/connect-tws')
    def connect_tws():
        print("Testing mode", app.config.get("TESTING"))
        # Check if 'TESTING' key exists, If it does not then we need to connect to TWS
        if not app.config.get('TESTING', False):
            print("Connecting to TWS from /connect-tws")
            success, message = trading_app.connect_to_tws(config['server_ip'], config['tws_port'])
            if not success:
                app.logger.error("Error connecting to TWS: %s", message)
                return "Error connecting to TWS:" + message
            return 'Connected to TWS'
        else:
            # While testing we want to simulate successful connection
            return 'Connected to TWS'
        
    return app