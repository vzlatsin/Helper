import os
import sys


from src.app import create_app

# Set an environment variable to specify the configuration
# For Windows, use set in the command line or os.environ in the script
config_name = 'development'
os.environ['APP_SETTINGS'] = config_name

app = create_app()

if __name__ == '__main__':
    # Run Flask in debug
    app.run(debug=True)