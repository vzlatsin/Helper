# The book 4th of April

# Table of Contents

- [OVERVIEW](#overview)
- [Project Structure Overview](#overview-project-structure-overview)
  - [Environment Setup](#overview-environment-setup)
- [app_async](#app_async)
- [Async Application Documentation](#app_async-async-application-documentation)
  - [Overview](#app_async-overview)
  - [Setup](#app_async-setup)
  - [Key Components](#app_async-key-components)
  - [Routes](#app_async-routes)
  - [Event Handlers](#app_async-event-handlers)
  - [Background Processing](#app_async-background-processing)
  - [Error Handling](#app_async-error-handling)
  - [Future Enhancements](#app_async-future-enhancements)
- [data-access](#data-access)
- [Data Access Documentation](#data-access-data-access-documentation)
  - [Functions Overview](#data-access-functions-overview)
  - [Example Usage](#data-access-example-usage)
  - [Tips for New Developers](#data-access-tips-for-new-developers)
  - [Future Improvements](#data-access-future-improvements)
- [flex-query](#flex-query)
- [Flex Query Documentation](#flex-query-flex-query-documentation)
  - [Functions Overview](#flex-query-functions-overview)
  - [Example Usage](#flex-query-example-usage)
  - [Error Handling](#flex-query-error-handling)
  - [Future Enhancements](#flex-query-future-enhancements)
- [run](#run)
- [Running the Application](#run-running-the-application)
  - [Overview](#run-overview)
  - [Prerequisites](#run-prerequisites)
  - [Configuration](#run-configuration)
  - [Logging](#run-logging)
  - [Usage](#run-usage)
  - [Environment Variables](#run-environment-variables)
  - [Command-Line Arguments](#run-command-line-arguments)
  - [Code Snippets](#run-code-snippets)
  - [Troubleshooting](#run-troubleshooting)




### 1. **Project Structure Overview**
Provide a detailed overview of your project's directory structure, including the purpose of key directories (e.g., `templates`, `static`, `src`). Example:
- `templates/`: Contains HTML files for rendering views.
- `static/`: Stores static files like CSS, JavaScript, and images.
- `src/`: Holds Python modules for various functionalities like data access, utility functions, etc.

### 2. **Environment Setup**
Detail the steps required to set up the development environment, including necessary software, frameworks (e.g., Flask, Express), and libraries (e.g., Flask-SocketIO, eventlet). Include version numbers where applicable to ensure compatibility.

### 3. **Running the Application**
Include instructions on how to start the application locally. Mention any commands needed, the default URL to access the app (e.g., `http://localhost:5000`), and how to stop the server.

### 4. **URL Routing Conventions**
Explain your approach to defining routes, especially the naming conventions for URL paths. Highlight the difference between accessing static files directly (if applicable) and serving pages through routes.

### 5. **Template Rendering Guide**
Describe how templates are rendered and served. Include a note on where templates should be located (`templates` folder) and how they're referenced in the server-side code.

### 6. **Linking to Pages from HTML**
Clarify the correct way to create links in HTML templates, emphasizing the use of URL paths defined by routes instead of direct file references. Provide examples of both correct and incorrect linking methods.

### 7. **Static Files Usage**
Detail how static files (CSS, JavaScript, images) are organized and how they should be referenced within HTML templates and CSS files.

### 8. **Common Errors and Troubleshooting**
Include a section on common errors (like the 404 error when clicking a link) with explanations and troubleshooting steps. This could serve as a quick reference to diagnose and fix issues.

### 9. **Version Control and Deployment**
Offer guidance on how to prepare the application for version control (e.g., using git) and deployment, including any steps to ensure sensitive information is not pushed to public repositories.

### 10. **Contact Information for Further Assistance**
Provide contact details or specify channels (e.g., email, issue tracker) for seeking further assistance or reporting issues with the documentation or application.



<a id='app_async'></a>
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



<a id='data-access'></a>
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



<a id='flex-query'></a>
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


<a id='run'></a>
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



