# run_tests.py
import os
import unittest

def run_tests():
    # Set the environment variable to specify the testing environment
    os.environ['MY_APP_ENV'] = 'testing'

    # Discover and run tests
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner().run(tests)
    if result.wasSuccessful():
        return 0  # Exit with 0 if tests were successful
    return 1  # Exit with 1 if tests failed

if __name__ == '__main__':
    exit(run_tests())
