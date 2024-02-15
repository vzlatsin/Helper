# flex_query.py
import requests
import logging

import xml.etree.ElementTree as ET


def parse_xml_response(response_text):
    # Parse the XML response
    root = ET.fromstring(response_text)
    return root

class RequestHandler:
    def get(self, url, params):
        # Debugging statement to log when the real RequestHandler is called
        # print(f"RequestHandler activated for URL: {url} with params: {params}")
        response = requests.get(url, params=params)
        # Optionally, log the response status code and a snippet of the response text
        # print(f"Response received: status code {response.status_code}, text snippet: {response.text[:100]}")
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
    logging.info('Initiating Flex Query with query ID: {query_id} and {token}')
    if response.status_code == 200:
        try:
            root = parse_xml_response(response.text)
            # Extract relevant data from XML
            status = root.find('.//Status').text
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
    

def download_flex_query_report(reference_code, token, request_handler=None):
    if request_handler is None:
        request_handler = RequestHandler()
    # Updated URL for downloading the report, based on the IB Flex Web Service documentation
    url = "https://ndcdyn.interactivebrokers.com/Universal/servlet/FlexStatementService.GetStatement"
    params = {"t": token, "q": reference_code, "v": "3"}
    response = request_handler.get(url, params=params)
    logging.info(f'Downloading Flex Query report with reference code: {reference_code} and token: {token}')
    if response.status_code == 200:
        try:
            root = parse_xml_response(response.text)
            # Now, process the XML as needed, for example, extract certain data
            # This is a placeholder, adjust based on your needs
            # Example: data = root.find('.//DesiredElement').text
            # Return or process this data as required
            return ET.tostring(root, encoding='unicode')  # Return the whole XML as a string, or process as needed
        except ET.ParseError:
            logging.error('Parsing XML has failed')
            return None
    else:
        logging.error(f'Error: HTTP {response.status_code} - {response.text}')
        return None