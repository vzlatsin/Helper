import unittest
"""
import threading
import subprocess
import time
import os

class TWSConnectionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = MyTradingApp()

    @classmethod
    def setUpClass(cls):
        # This method will be executed once before running tests in the class
        cls.simulator_process = subprocess.Popen(['python', 'tws_simulator.py'])
        time.sleep(5)  # Wait for simulator to start

    @classmethod
    def tearDownClass(cls):
        # This method will be executed once after all tests are done
        cls.simulator_process.terminate()  # Terminate the simulator
"""
    #def test_connection_to_tws(self):
        # Run the helper script and capture its output
        #result = subprocess.run(['python', 'helper.py'], capture_output=True, text=True)
        #self.assertIn("Connected to TWS", result.stdout)  # Example assertion

if __name__ == '__main__':
    unittest.main()
