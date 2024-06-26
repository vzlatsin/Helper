# flex_query.py
import requests
import logging
import time

import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime, timedelta

def parse_xml_response(response_text):
    # Parse the XML response
    root = ET.fromstring(response_text)

    # Convert the ElementTree Element to a pretty-printed XML string for easier reading
    rough_string = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml_as_string = reparsed.toprettyxml(indent="  ")

    # Print the pretty-printed XML
    print(pretty_xml_as_string)

    return root

def find_trades_response(root):
    logging.info("Entering find_trades_response...")
    
    # Log the count of FlexQueryResponse elements found
    flex_query_responses = list(root.iter('FlexQueryResponse'))
    logging.info(f"Total FlexQueryResponse elements found: {len(flex_query_responses)}")
    
    for elem in flex_query_responses:
        # Log the attributes of each FlexQueryResponse element
        logging.debug(f"FlexQueryResponse attributes: {elem.attrib}")
        
        if 'queryName' in elem.attrib:
            logging.info(f"Found FlexQueryResponse with attributes: {elem.attrib}")
            
            if elem.attrib['queryName'] == 'Trades':
                logging.info("FlexQueryResponse for 'Trades' found. Returning element.")
                return elem
            else:
                # Log if the queryName attribute doesn't match 'Trades'
                logging.debug(f"FlexQueryResponse found with queryName not equal to 'Trades': {elem.attrib['queryName']}")
        else:
            # Log if the FlexQueryResponse element doesn't have a queryName attribute
            logging.debug("Found FlexQueryResponse without a queryName attribute.")
    
    logging.info("No FlexQueryResponse for 'Trades' found. Returning None.")
    return None


class RequestHandler:
    def get(self, url, params):
        # Debugging statement to log when the real RequestHandler is called
        # print(f"RequestHandler activated for URL: {url} with params: {params}")
        response = requests.get(url, params=params)
        # Optionally, log the response status code and a snippet of the response text
        logging.info(f"Response received: status code {response.status_code}, text snippet: {response.text[:300]}")
        return response
    
def initiate_flex_query_report(query_id, token, request_handler=None):
    # print(f'initiate_flex_query_report activated')
    if request_handler is None:
        request_handler = RequestHandler()
    #else:
    #    print(f'Using provided request_handler of type: {type(request_handler).__name__}')
    url = "https://ndcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.SendRequest"
    params = {"t": token, "q": query_id, "v": "3"}
    response = request_handler.get(url, params=params)
    print(f"initiate_flex_query_report: Query ID: {query_id}, {token}")
    logging.info('initiate_flex_query_report: Initiating Flex Query with query ID: {query_id} and {token}')
    if response.status_code == 200:
        try:
            root = parse_xml_response(response.text)
            logging.info(f"Raw XML response: {response.text[:500]}")
            # Extract relevant data from XML
            status = root.find('.//Status').text
            logging.info(f"Found status: {status}")
            if status == "Success":
                reference_code = root.find('.//ReferenceCode').text
                return reference_code
            else:
                # Handle error or failure status
                error_message = root.find('.//ErrorMessage').text
                print(f"Error: {error_message}")
                return None
        except ET.ParseError:
            print('Parsing XML has failed')
    else:
        # Handle errors or invalid responses
        print(f'Error: HTTP {response.status_code} - {response.text}')
        return None
    

def download_flex_query_report(reference_code, token, retry_attempts=10, retry_wait=10, request_handler=None):
    if request_handler is None:
        request_handler = RequestHandler()
    # Updated URL for downloading the report, based on the IB Flex Web Service documentation
    url = "https://ndcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.GetStatement"
    params = {"t": token, "q": reference_code, "v": "3"}
    for attempt in range(retry_attempts):
        response = request_handler.get(url, params=params)
        logging.info(f"Downloading Flex Query report with reference code: {reference_code} and token: {token}")
        if response.status_code == 200:
            root = parse_xml_response(response.text)

            #print("Diagnostic XML Output:")
            #for elem in root.iter():
                #print(ET.tostring(elem, encoding='unicode'))

            trades_response = find_trades_response(root)
            
            cash_transactions = root.find('.//CashTransactions')

            # Check for expected elements in the response
            if root is not None and (trades_response is not None or cash_transactions is not None):
                logging.info('Successfully downloaded the report.')
                return ET.tostring(root, encoding='unicode')
            else:
                logging.warning('Expected elements not found in the report. Retrying...')
                time.sleep(retry_wait)
                continue
           
        else:
            logging.error(f'Error: HTTP {response.status_code} - {response.text}')
            break
    logging.error('Failed to download report after maximum attempts.')
    return None
    
def get_last_dividend_date():
    pass

def get_dividend_query_id(latest_date, flex_queries_config):
    """
    Select the appropriate Flex Query ID based on the difference from the latest date.
    :param latest_date: The latest date from the database
    :return: Flex Query ID as a string
    """
    if latest_date is None:
        # No dividends in the DB, consider fetching the longest duration
        return flex_queries_config['365_days']
   
    today = datetime.now()
    delta = today - latest_date
    if delta.days <= 7:
        return flex_queries_config['7_days']
    elif delta.days <= 30:
        return flex_queries_config['30_days']
    elif delta.days <= 180:
        return flex_queries_config['180_days']
    else:
        return flex_queries_config['365_days']
    
def get_trade_query_id(flex_queries_config, criteria=None):
    """
    Select the appropriate Flex Query ID for fetching trades.
    
    This is a placeholder function. The actual implementation might depend on specific criteria,
    similar to how `get_dividend_query_id` uses the latest date to determine the query ID.
    
    :param flex_queries_config: The configuration dictionary containing Flex Query IDs.
    :param criteria: Optional. Criteria used to select the Flex Query ID for trades.
    :return: Flex Query ID as a string.
    """
    # Example placeholder logic:
    # If you have different Flex Query IDs for trades based on certain criteria,
    # implement the logic here to select the appropriate ID from `flex_queries_config`.
    # For simplicity, this example assumes a single Flex Query ID for all trades.
    
    return flex_queries_config['trades']
