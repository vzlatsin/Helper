# run.py
import os
import sys
import logging
import json



from src.app import create_app, socketio
from src.app_async import create_async_app
import asyncio

config_name = os.getenv('MY_APP_ENV', 'development')
# Set an environment variable to specify the configuration
os.environ['APP_SETTINGS'] = config_name

def load_config():
    config_file = f'config/{config_name}.json'
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

# Load configuration
config = load_config()

# Configure logging
logging.basicConfig(filename=config['logging']['filename'],
                    level=getattr(logging, config['logging']['level'].upper()),
                    format=config['logging']['format'])
# print(config['db_path'])
logging.debug("Logging is configured.")

if len(sys.argv) > 1 and sys.argv[1] == 'async':
    # Import and run the asynchronous version of the app
    app, socketio = create_async_app(config)
else:
    app = create_app(config)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000,  debug=True)  # Run with SocketIO
