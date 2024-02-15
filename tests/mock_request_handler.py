# tests/mock_request_handler.py
import json

class MockRequestHandler:
    def get(self, url, params):
        class MockResponse:
            def __init__(self, status_code=200, text=None, json_data=None):
                self.status_code = status_code
                self.text = text if text is not None else json.dumps(json_data)
                self.json_data = json_data
            def json(self):
                return self.json_data
            
            text = 'REFERENCE_CODE'
        # Simulate initiating the query
        if "initiate" in url:
            # Assuming the API returns a job ID for the initiated query
            return MockResponse(json_data={"job_id": "123456"})
        else:
            return MockResponse(status_code=404, json_data={"error": "Not found"})
        # Simulate a successful request

