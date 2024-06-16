import os
import sys
import json
import logging
import unittest
import subprocess

def load_config():
    config_name = 'testing'  # Directly use 'testing' as we're running tests
    config_file = f'config/{config_name}.json'
    with open(config_file, 'r') as f:
        return json.load(f)

def configure_logging(config):
    logging.basicConfig(filename=config['logging']['filename'],
                        level=getattr(logging, config['logging']['level'].upper()),
                        format=config['logging']['format'])
    logging.debug("Test logging is configured.")

def run_python_tests():
    # Discover and run Python tests
    tests = unittest.TestLoader().discover('tests', pattern='test_*.py')
    result = unittest.TextTestRunner().run(tests)
    return result.wasSuccessful()

def run_jest_tests():
    # Determine the correct npm command
    npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
    try:
        result = subprocess.run([npm_command, 'test'], capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)  # Print the error output for debugging
        return result.returncode == 0
    except Exception as e:
        print(f"An error occurred while running Jest tests: {e}")
        return False

def run_tests():
    config = load_config()
    configure_logging(config)
    os.environ['MY_APP_ENV'] = 'testing'

    # Run both Python and JavaScript tests
    python_tests_passed = run_python_tests()
    jest_tests_passed = run_jest_tests()

    return python_tests_passed and jest_tests_passed

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
