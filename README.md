# README.md
# Financial Data Automation Web Application

This application automates the retrieval, processing, and storage of financial information from Interactive Brokers using Python, Flask, and SQLite. Initially focused on dividends, it has evolved to include functionalities like file comparison for discrepancy analysis and adjustments for handling multiple dividends on the same day, making it a comprehensive tool for automating various financial tasks, including tax return preparation.

## Broad Objectives

- **Versatile Financial Data Handling**: Automates the handling of dividends and broader financial transactions, simplifying personal finance management.
- **Tax Preparation Assistance**: Streamlines the collection and organization of information necessary for tax returns, enhancing accuracy.
- **Expandable Framework**: Designed for easy integration of new modules for different financial tasks.

## Core Features

- **Interactive Web Interface**: A user-friendly web interface for manual data operations and financial report viewing.
- **Automated Data Integration**: Automated fetching, parsing, and storage of financial data.
- **Customizable Reporting**: Facilitates generating reports tailored for tax preparation and financial analysis.

## Project Structure and Key Components

- `/src` Directory: Contains the application's logic and functionality.
  - `app.py`: Sets up the Flask application and web routes.
  - `/db`: Includes database scripts for schema initialization (`init_db.py`) and data manipulation (`data_access.py`).
  - `flex_query.py`: Handles data retrieval from brokerage services.
  - Utility Scripts (`helper.py`, `report_parser.py`): Provide connectivity and data parsing assistance.
- **Configuration and Testing**: Environment-specific settings (`/config`) and a testing suite (`/tests`) ensure the application's reliability.

## New Updates

- **File Comparison Functionality**: Implements discrepancy analysis between fetched and stored data, aiding in identifying and rectifying data mismatches.
- **Handling Multiple Dividends**: Adjusts database schema to accommodate multiple dividends paid by a company on the same day.

## Getting Started

### Setup

1. Clone this repository.
2. Install Dependencies: `pip install -r requirements.txt`
3. Initialize Database: `python src/db/init_db.py`

### Running the Application

Execute `python run.py` to start the server. Access the web interface at http://localhost:5000.

### Accessing WebSocket Functionality

1. Open a web browser and navigate to `http://localhost:5000/socket_client`.
   - This page allows you to initiate WebSocket connections and test WebSocket events.

2. Once on the `/socket_client` page, look for a button or link labeled "Connect" or "Initiate WebSocket Connection".
   - Click on the button/link to trigger the event that establishes the WebSocket connection with the server.

3. After establishing the WebSocket connection, you can trigger the Flex Query event to test WebSocket functionality further.

### Initiating Flex Query Event

1. Navigate to `http://localhost:5000/run-flex-query-form`.
   - This page allows you to submit a form to initiate the Flex Query event via WebSocket.

2. Fill in the required fields (e.g., query ID, token) in the form and submit it.
   - This will trigger the event that initiates the Flex Query, and you can observe the WebSocket communication and query execution progress.

By following these steps, you can test the WebSocket functionality and Flex Query event in your Flask application.

## Expanding Functionality

To add new functionalities:

- **Web Interface**: Modify `app.py` and `/templates` for new data inputs or workflows.
- **Data Processing**: Update `flex_query.py` for additional data retrieval; adjust `data_access.py` for new database operations.
- **Schema Adjustments**: Update `init_db.py` for database schema changes to support new data types.

## Development Notes

- **Testing New Features**: Add tests in the `/tests` subfolder to cover new functionalities, ensuring the application's integrity. Run tests using the command `python run_tests.py`.
- **Logging**: Utilize `development.log` or `testing.log` for application monitoring and debugging.

### WebSocket Architecture and Setup

#### Overview
WebSockets play a crucial role in providing real-time updates and enhancing user experience within our application. This section provides an overview of how WebSockets are integrated and the setup required to enable WebSocket functionality.

#### Integration Overview
Our application utilizes WebSockets to deliver real-time updates on financial data processing, status notifications, and other relevant information to users. This integration enhances the responsiveness of the application and provides users with immediate feedback during data retrieval and processing tasks.

#### Setup Instructions
To enable WebSocket functionality in your development environment, follow these steps:

1. **Installation of WebSocket Dependencies**:
   - Ensure that you have the necessary dependencies installed. Our application uses [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/) for WebSocket support. You can install it via pip:
     ```
     pip install flask-socketio
     ```

2. **WebSocket Server Initialization**:
   - Initialize the WebSocket server alongside the Flask application. This typically involves creating a separate Flask-SocketIO instance and configuring it to work with your Flask application.

3. **Client-Side Integration**:
   - Implement WebSocket client-side logic to establish a connection with the server and handle incoming WebSocket messages. Ensure that the client-side code is integrated into your application's front-end framework.

#### Communication Flow
WebSocket communication within our application follows a straightforward flow:

1. **Client-Server Handshake**:
   - The client initiates a WebSocket connection with the server upon loading the application or when WebSocket functionality is required.

2. **Server-Side Handling**:
   - The server processes incoming WebSocket connections and handles WebSocket events, such as message reception and transmission.

3. **Real-Time Updates**:
   - Upon receiving relevant events or data updates, the server emits WebSocket messages to connected clients, providing real-time updates on financial data processing and other tasks.

#### Message Handling
WebSocket messages exchanged between the client and server typically adhere to a predefined format. Ensure consistent message formatting and adhere to established conventions to facilitate smooth communication between client and server components.

### Next Steps
With WebSocket functionality set up, you're ready to enhance the real-time capabilities of your application. Consider expanding WebSocket integration to support additional features and use cases, such as live data visualization and interactive user interfaces.


## Contributing and Support

Contributions or suggestions for expanding the application's capabilities are welcome. For collaboration or questions, please open an issue in the repository.

## Future Directions

- **Tax Reporting Module**: An upcoming extension to automate tax return preparation.
- **Investment Analysis Tools**: Planned tools for analyzing portfolio performance and tax implications.

## Project Files

Below is a list of key files in the project along with their locations and descriptions:

- `/src/app.py`: Sets up the Flask application and web routes.
- `/src/app_async.py`: Adds asynchronous processing capabilities to the application.
- `/src/db/init_db.py`: Initializes the database schema.
- `/src/db/data_access.py`: Provides functionality for data manipulation in the database.
- `/src/flex_query.py`: Handles data retrieval from brokerage services.
- `/src/helper.py`: Contains utility functions used across the application.
- `/src/report_parser.py`: Parses financial reports for data extraction.
- `/config/`: Contains environment-specific settings for the application.
- `/tests/`: Includes the testing suite for ensuring application reliability.
- `async_test.html`: Template for testing asynchronous functionality.
- `fetch_financial_data_async.html`: Template for initiating asynchronous financial data fetching.
- `flex_query_status.html`: Template for monitoring the status of flex query processing.
- `tests/test_app_async.py`
- `run.py`: Entry point for running the Flask application.
- `requirements.txt`: Lists Python dependencies required for the project.
- `README.md`: Documentation providing an overview of the project, usage instructions, and development notes.

## Templates

The project's user interface is built using HTML templates. Below are the main template files along with their descriptions:

- `index.html`: This is the main landing page of the web application, displaying essential information and options for user interaction.
- `run_flex_query_form.html`: This template renders a form for initiating a Flex Query event via WebSocket. Users can input query ID and token here.
- `socket_client.html`: Provides a simple interface for testing WebSocket functionality. Users can connect to the WebSocket server and trigger events for testing purposes.
- `financial_report.html`: Renders financial reports generated by the application, providing users with insights into their financial data.
- `error.html`: Displays error messages or alerts to users when an error occurs during the application's operation.


## License and Contact

For personal use. Contact for broader usage rights or contributions.
