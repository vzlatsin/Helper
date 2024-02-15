# run.py
import os
import sys
import logging
import json


from src.app import create_app

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

logging.debug("Logging is configured.")


app = create_app(config)

if __name__ == '__main__':
    # Run Flask in debug
    app.run(debug=True, host='0.0.0.0')