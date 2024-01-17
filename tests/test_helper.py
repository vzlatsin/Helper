import unittest
from unittest.mock import Mock, patch
from src.helper import MyTradingApp  # Import your app

class TestMyTradingApp(unittest.TestCase):
    def setUp(self):
        # This method is called before each test
        # Set up your mock objects here
        self.mock_tws = Mock()  # Creating a mock object to represent TWS

    def test_connect_to_tws(self):
        # Test the connect_to_tws method
        with patch('src.helper.EClient.connect', self.mock_tws):
            app = MyTradingApp()
            app.connect_to_tws()

            # Assert that connect was called with the correct parameters
            self.mock_tws.assert_called_with("127.0.0.1", 7496, 0)

    # Add more tests for other methods

if __name__ == '__main__':
    unittest.main()