# Assuming MyTradingApp is in the helper module
from src.helper import MyTradingApp
from src.app import create_app
import unittest
from unittest.mock import patch
import logging

"""
class TestTradingAppConnection(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['server_ip'] = '127.0.0.1'
        self.app.config['tws_port'] = 7496
        self.client = self.app.test_client()
        logging.getLogger('werkzug').setLevel(logging.ERROR)

    @patch('src.helper.MyTradingApp')
    def test_connect_tws(self, mock_trading_app):
        # Configure the mock to return a success response
        # mock_trading_app_instance = mock_trading_app.return_value
        # mock_trading_app_instance.connect_to_tws.return_value = (True, "Connected successfully")

        response = self.client.get('/connect-tws')
        self.assertIn('Connected to TWS', response.data.decode())

"""
if __name__ == '__main__':
    unittest.main()
