# The book

# Table of Contents

- [app_async](#app_async)
- [Async Application Documentation](#async-application-documentation)
  - [Overview](#overview)
  - [Setup](#setup)
  - [Key Components](#key-components)
  - [Routes](#routes)
  - [Event Handlers](#event-handlers)
  - [Background Processing](#background-processing)
  - [Error Handling](#error-handling)
  - [Future Enhancements](#future-enhancements)
- [data-access](#data-access)
- [Data Access Documentation](#data-access-documentation)
  - [Functions Overview](#functions-overview)
  - [Example Usage](#example-usage)
  - [Tips for New Developers](#tips-for-new-developers)
  - [Future Improvements](#future-improvements)
- [flex-query](#flex-query)
- [Flex Query Documentation](#flex-query-documentation)
  - [Functions Overview](#functions-overview)
  - [Example Usage](#example-usage)
  - [Error Handling](#error-handling)
  - [Future Enhancements](#future-enhancements)
- [run](#run)
- [Running the Application](#running-the-application)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Configuration](#configuration)
  - [Logging](#logging)
  - [Usage](#usage)
  - [Environment Variables](#environment-variables)
  - [Command-Line Arguments](#command-line-arguments)
  - [Code Snippets](#code-snippets)
  - [Troubleshooting](#troubleshooting)


# Async Application Documentation

## Overview

This document describes `app_async.py`, the core of the asynchronous web application, leveraging Flask and Flask-SocketIO for real-time web communication and async processing.

## Setup

The script initializes a Flask app with CORS enabled, configures it with default and external settings, and sets up Flask-SocketIO for real-time communication.

## Key Components

- **Flask Application**: Configuration details, including testing and debug modes.
- **SocketIO Integration**: How SocketIO is integrated for real-time updates.
- **Async Routes**: Examples of asynchronous route definitions.
- **Background Tasks**: Utilization of `socketio.start_background_task` for async operations.

## Routes

- `/async-route`: Demonstrates an async response from a Flask route.
- `/fetch-financial-data-async`: Shows a form template for initiating financial data fetching.

## Event Handlers

- `fetch_dividends`: Triggered by a client request to start fetching and processing dividend data asynchronously.

## Background Processing

Details on processing dividends in the background, ensuring non-blocking operations while providing real-time updates to the client.

### Event-Driven Architecture and Real-Time Data Handling

The `app_async` module utilizes an event-driven architecture to manage real-time data updates and background processing tasks efficiently. This approach leverages Flask-SocketIO to facilitate real-time web communication, ensuring that the application remains dynamic and responsive to user interactions.

#### Handling Dividend Data in Real-Time

- **Event: `fetch_dividends`**
  - **Trigger:** Initiated by the user's request to fetch new dividend information.
  - **Process:** Upon triggering, the event enqueues a background task to retrieve dividend data using the `flex-query` module. Once the data is fetched and processed, it is stored in the database via the `data-access` module.
  - **Real-Time Updates:** The module then pushes updates to the client through a SocketIO event, allowing the user interface to display the latest dividend information without requiring a page refresh.

This architecture supports a highly interactive user experience by ensuring that data displayed to the user is as up-to-date as possible. By detailing specific events and their handling, developers can gain insights into integrating additional real-time data functionalities into the application.

### Handling Trade Data in Real-Time

- **Event: `fetch_trades`**
  - **Trigger**: User request to fetch trade information.
  - **Process**: Activates a background task to retrieve trade data using the `ib_data_fetcher` module, then processes and stores this data in the database, avoiding duplicates.
  - **Real-Time Updates**: Utilizes SocketIO to provide immediate updates to the client, showcasing the latest trade information seamlessly.

This module's structure allows for the efficient handling of both dividend and trade data in a non-blocking manner, significantly enhancing the application's responsiveness and user experience.

## Error Handling

Explanation of error handling within async tasks and routes, ensuring robust application behavior.

## Future Enhancements

Potential enhancements for expanding async capabilities and improving real-time feedback mechanisms.



# Data Access Documentation

This module manages database operations for financial data, including inserting new records and querying data.

## Functions Overview

- **create_connection(db_file)**: Establishes a database connection.
- **insert_dividend(conn, symbol, amount, ex_date, pay_date)**: Inserts a new dividend record.
- **insert_dividend_if_not_exists(conn, symbol, amount, ex_date, pay_date)**: Ensures no duplicate records are inserted.
- **insert_trade_if_not_exists(conn, symbol, transaction_type, trade_id, order_time, trade_date, buy_sell, quantity, price, amount, commission, net_cash, tax)**: Inserts a new trade record into the database if an identical record does not already exist. This function is essential for maintaining the integrity of the trades data stored within the application.

- **count_dividend_records(conn)**: Counts total dividend records.
- **get_latest_dividend_date(conn)**: Retrieves the latest dividend date.
- **fetch_dividends_from_db(conn)**: Fetches all dividend records.
- **fetch_dividends_by_quarter(conn)**: Aggregates dividends by quarter.

## Example Usage

Provides steps for connecting to the database, inserting records, and querying existing data.

## Tips for New Developers

Highlights the importance of SQLite installation and SQL syntax familiarity.

## Future Improvements

Discusses transitioning to asynchronous database operations and advanced data analysis queries.

### Interactions and Data Flow
The `data-access` module interfaces directly with the database, handling CRUD operations for financial data. It receives data from the `flex-query` module in JSON format, which it then validates and stores. Additionally, it serves processed data upon request to the `app_async` module for real-time display to users. 



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


# Running the Application

## Overview
`run.py` serves as the entry point for running the Flask web application. It supports both synchronous and asynchronous modes, determined by command-line input.

## Prerequisites
- Python 3.6+
- Flask
- Dependencies from `requirements.txt`

## Configuration
The script uses the `MY_APP_ENV` environment variable to determine the application's configuration mode (`development`, `production`, etc.). Configurations are loaded from corresponding JSON files within the `config` directory.

## Logging
Logging is configured according to the loaded configuration, specifying log files, levels, and formats.

## Usage
To run the application:
- For synchronous mode: `python run.py`
- For asynchronous mode: `python run.py async`

## Environment Variables
- `MY_APP_ENV`: Determines the app's running environment.
- `APP_SETTINGS`: Set by the script to match `MY_APP_ENV`.

## Command-Line Arguments
- `async`: Specifies that the app should run in asynchronous mode.

## Code Snippets
(Provide relevant code snippets for configuration loading and app initialization)

## Troubleshooting
(Include common issues and resolutions)



