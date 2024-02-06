
from flask import Flask
import os
import json
from .helper import MyTradingApp
import logging

def create_app():
    app = Flask(__name__)
    trading_app = MyTradingApp()


    def load_config():
        env = os.getenv('MY_APP_ENV', 'development')
        config_file = f'config/{env}.json'
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config

    config = load_config()
    

    @app.route('/')
    def home():
        return 'Welcome!'

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

