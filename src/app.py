# app.py
from flask import Flask, request, jsonify, redirect, url_for, render_template
import os
import json
from .helper import MyTradingApp
import logging
from src.flex_query import initiate_flex_query_report, download_flex_query_report

def create_app(config):
    app = Flask(__name__, template_folder='../templates')
    trading_app = MyTradingApp()

    

    @app.route('/')
    def home():
        app.logger.info("Welcome!")
        logging.debug("test")
        return 'Welcome!'
    
    @app.route('/run-flex-query-form')
    def show_flex_query_form():
        return render_template('run_flex_query.html')

    
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

