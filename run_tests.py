# run_tests.py
import os
import sys
import json
import logging
import unittest

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


def run_tests():
    config = load_config()
    configure_logging(config)
    # Set the environment variable to specify the testing environment
    os.environ['MY_APP_ENV'] = 'testing'

    # Discover and run only TimeManagement tests
    tests = unittest.TestLoader().discover('tests', pattern='TimeManagement.test.js')
    # Discover and run tests
    # tests = unittest.TestLoader().discover('tests')
    # tests = unittest.TestLoader().discover('tests', pattern='test_flex_query.py')
    tests = unittest.TestLoader().discover('tests', pattern='*.test.js')
    result = unittest.TextTestRunner().run(tests)
    if result.wasSuccessful():
        return 0  # Exit with 0 if tests were successful
    return 1  # Exit with 1 if tests failed


if __name__ == '__main__':
    exit(run_tests())
