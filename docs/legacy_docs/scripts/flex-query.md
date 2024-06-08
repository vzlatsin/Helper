# Flex Query Documentation

This module is responsible for fetching financial data through Flex Query API calls, including initiating and downloading Flex Query reports.

## Functions Overview

- **`parse_xml_response(response_text)`**: Parses XML response strings into a structured format.
- **`RequestHandler.get(url, params)`**: Manages GET requests with given URL and parameters, facilitating communication with external APIs.
- **`initiate_flex_query_report(query_id, token, request_handler=None)`**: Initiates the process for requesting a Flex Query report from Interactive Brokers, using a specified query ID and authentication token.
- **`download_flex_query_report(reference_code, token, retry_attempts, retry_wait, request_handler=None)`**: Downloads the Flex Query report based on a reference code obtained from initiating the report. Includes retry logic to handle temporary issues.
- **`get_dividend_query_id(latest_date, flex_queries_config)`**: Determines the most appropriate Flex Query ID for fetching dividend data based on the latest date of dividend data in the database.
- **`get_trade_query_id(flex_queries_config, criteria=None)`**: Selects the appropriate Flex Query ID for fetching trade data, adaptable based on specified criteria or configurations.



## Example Usage

Demonstrate how to fetch and process financial reports by initiating and downloading a Flex Query report.

## Error Handling

Describes error logging during request failures or XML parsing issues for easier troubleshooting.

## Future Enhancements

Suggestions for implementing asynchronous request handling and enhancing error recovery mechanisms.
