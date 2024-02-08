import unittest
from unittest.mock import patch
from src.flex_query import initiate_flex_query_report, download_flex_query_report

class TestFlexQueryDownload(unittest.TestCase):
    @patch('src.flex_query.requests.get')
    def test_initiate_flex_query_report(self, mock_get):
        # Mock the response for initiating the Flex Query report
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'REFERENCE_CODE'
       
        reference_code = initiate_flex_query_report('QUERY_ID', 'TOKEN')
        self.assertEqual(reference_code, 'REFERENCE_CODE')
       
    @patch('src.flex_query.requests.get')
    def test_download_flex_query_report(self, mock_get):
        # Mock the response for downloading the Flex Query report
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'REPORT_DATA'
       
        report_data = download_flex_query_report('REFERENCE_CODE', 'TOKEN')
        self.assertEqual(report_data, 'REPORT_DATA')

if __name__ == '__main__':
    unittest.main()
