# tests/test_socketio.py

from src.app import create_app, socketio
import unittest

class TestSocketIOConnection(unittest.TestCase):
    def setUp(self):
        print("Setting up the test...")
        # Create app with testing configuration
        self.app = create_app({'TESTING': True})
        self.app_context = self.app.app_context()
        self.app_context.push()
        # Create a test client
        self.client = socketio.test_client(self.app, namespace='/test')
        connected = self.client.is_connected('/test')
        print(f"Client connected: {connected}")  # This line is for debugging purposes
        assert connected, "Client should be connected."


    def tearDown(self):
        try:
            self.client.disconnect()
        except RuntimeError as e:
            if str(e) != 'not connected':
                raise  # Re-raise if it's a different RuntimeError
        self.app_context.pop()

    def test_connection(self):
        # Check if the client is connected
        assert self.client.is_connected('/test'), "Client should be connected to the /test namespace."

    def test_echo_event_response(self):
        # Test data to send with the echo event
        test_data = {'message': 'Hello, SocketIO'}

        # Emitting the echo event to the server with test data
        self.client.emit('echo', test_data, namespace='/test')

        # Receiving the response from the server
        received = self.client.get_received('/test')

        # Filter out 'response' event
        filtered_events = [event for event in received if event['name'] == 'echo_response']

        print("Filtered events:", filtered_events)  # Print filtered events for debugging

        # Checking if any response is received
        self.assertTrue(len(filtered_events) > 0, "No response received from the server.")

        if filtered_events:
            print("First received event:", filtered_events[0])  # Print the first received event for debugging

            # Checking the data received in the response
            self.assertEqual(filtered_events[0]['name'], 'echo_response', "Incorrect response event type.")
            self.assertEqual(filtered_events[0]['args'][0], test_data, "The response data does not match the sent data.")

if __name__ == '__main__':
    unittest.main()
