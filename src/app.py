# app.py
from flask import Flask, request, jsonify, redirect, url_for, render_template
import os
import json
from .helper import MyTradingApp
from .report_paser import parse_cash_transaction
import logging
from src.flex_query import initiate_flex_query_report, download_flex_query_report, get_query_id, get_last_dividend_date
from src.db.data_access import create_connection, get_latest_dividend_date, count_dividend_records

def create_app(config):
    app = Flask(__name__, template_folder='../templates')
    trading_app = MyTradingApp()
    app.config.update(config)

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
        for t in transactions:
            logging.info(f"Parsed transaction: {t}")

        conn.close()

        return jsonify({"status": "success", "data": "Dividends processed successfully"})
        
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