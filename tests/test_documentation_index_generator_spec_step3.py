import unittest
from src.app_async import create_async_app

class TestAppAsyncFunctionality(unittest.TestCase):
    def setUp(self):
        # Set up any required test configurations or objects
        self.app, self.socketio = create_async_app({'TESTING': True})
        self.client = self.app.test_client()

    def tearDown(self):
        # Clean up after each test
        pass

    def test_async_route_response(self):
        # Test if the asynchronous route responds correctly
        response = self.client.get('/async-route')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Async route response')

if __name__ == '__main__':
    unittest.main()
