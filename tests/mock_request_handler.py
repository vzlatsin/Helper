# tests/mock_request_handler.py
import json

class MockRequestHandler:
    def get(self, url, params):
        class MockResponse:
            def __init__(self, status_code=200, text=None):
                self.status_code = status_code
                self.text = text
            
        if "SendRequest" in url:
            return MockResponse(text='<FlexQueryResponse><Status>Success</Status><ReferenceCode>123456</ReferenceCode></FlexQueryResponse>')
        elif "GetStatement" in url:
            return MockResponse(text='<FlexQueryResponse><Status>Success</Status><Data>REPORT_DATA</Data></FlexQueryResponse>')
        else:
            return MockResponse(status_code=404, text='<Error>Not found</Error>')

