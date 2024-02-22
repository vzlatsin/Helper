import unittest
import logging
from src.data_fetcher import APIDataFetcher
from tests.mock_data_fetcher import MockDataFetcher
from tests.mock_request_handler import MockRequestHandler
from unittest.mock import patch
from src.flex_query import initiate_flex_query_report, download_flex_query_report


class TestFlexQueryDownload(unittest.TestCase):
    @patch('src.data_fetcher.APIDataFetcher', new=MockDataFetcher)
    def test_feature_with_mock(self):
        # Test that use MockDataFetcher instead of APIDataFetcher
        pass

    def test_1_initiate_flex_query_report(self):
        # Use MockRequestHandler instead of the real one
        job_id = initiate_flex_query_report('923682', 'TOKEN', request_handler=MockRequestHandler())
        self.assertEqual(job_id, '123456')
        logging.info("Test initiate_flex_query_report executed successfully")

    def test_2_download_flex_query_report(self):
        # Use MockRequestHandler for the download function
        report_data = download_flex_query_report('REFERENCE_CODE', 'TOKEN',request_handler=MockRequestHandler())
        
        expected_xml = '<FlexQueryResponse queryName="Dividends last year" type="AF"><CashTransactions><CashTransaction currency="AUD" symbol="RFF" description="RFF (AU000000RFF5) CASH DIVIDEND AUD 0.029325 (Mixed Income)" dateTime="20230801;102000" amount="46.92" type="Dividends" reportDate="20230731" /></CashTransactions></FlexQueryResponse>'
        self.assertEqual(report_data, expected_xml)

if __name__ == '__main__':
    unittest.main()
