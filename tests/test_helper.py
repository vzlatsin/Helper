import unittest
from unittest.mock import Mock, patch
from src.helper import MyTradingApp  # Import your app
import logging

class TestMyTradingApp(unittest.TestCase):

    def setUp(self):
        self.app = MyTradingApp()

    def test_has_placeOrder_method(self):
        self.assertTrue(hasattr(self.app, 'placeOrder'), "placeOrder method is missing")

    def test_has_orderStatus_method(self):
        self.assertTrue(hasattr(self.app, 'orderStatus'), "orderStatus method is missing")
    
    @patch('ibapi.client.EClient.__init__')
    def test_initialization(self, mock_init):
        logging.info("testing initialization")
        app = MyTradingApp();
        mock_init.assert_called_with(app,app)

    @patch('ibapi.client.EClient.connect')
    def test_connect_to_tws(self, mock_connect):
        app = MyTradingApp();
        #app.connect_to_tws('localhost', 7496)

        # Assert that connect was called with the correct parameters
        #mock_connect.assert_called_with("127.0.0.1", 7496, 0)

    # Add more tests for other methods

if __name__ == '__main__':
    unittest.main()