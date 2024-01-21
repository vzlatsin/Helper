import unittest
from unittest.mock import Mock, patch
from src.helper import MyTradingApp  # Import your app
import logging

class TestMyTradingApp(unittest.TestCase):

    @patch('ibapi.client.EClient.__init__')
    def test_initialization(self, mock_init):
        logging.info("testing initialization")
        app = MyTradingApp();
        mock_init.assert_called_with(app,app)

    @patch('ibapi.client.EClient.connect')
    def test_connect_to_tws(self, mock_connect):
        app = MyTradingApp();
        app.connect_to_tws()

        # Assert that connect was called with the correct parameters
        mock_connect.assert_called_with("127.0.0.1", 7496, 0)

    # Add more tests for other methods

if __name__ == '__main__':
    unittest.main()