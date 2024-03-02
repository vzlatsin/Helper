Enhanced Project Overview: Dividend Information Retrieval Web Application

This Python-based web application leverages the Flask framework and SQLite database to automate the retrieval and storage of dividend information from Interactive Brokers. Designed for efficiency and ease of use, it features a user-friendly web interface for manual interactions and automated processes for data handling.

Comprehensive Features:
Interactive Web Interface: Users can initiate Flex Queries and request dividend data processing through dedicated web forms.
Automated Data Retrieval and Storage: Automates the fetching, parsing, and storing of dividend information into an SQLite database, ensuring data is up-to-date and accessible.
Database Management: Utilizes custom database scripts for seamless data integration, supporting operations such as record insertion, data retrieval, and integrity checks.
Detailed Components:
Flask Application (app.py): The backbone of the web interface, facilitating user interactions, logging, and integration with backend services.
Flex Query Handler (flex_query.py): Interfaces with Interactive Brokers' Flex Query service for data retrieval, employing robust error handling and retry logic.
Database Access Layer (data_access.py): Encapsulates all database interactions, including connection management and data manipulation, ensuring a clean separation of concerns.
Database Operations:
Connection Establishment: Dynamically connects to the SQLite database, as specified in the application's configuration, ensuring a flexible and reliable data storage solution.
Data Management: Supports sophisticated data operations, such as inserting new dividend records, counting existing records, and querying the latest dividend dates, to facilitate intelligent data processing and retrieval.
Latest Dividend Date Retrieval: Employs logic to determine the most recent dividend entry, guiding the application in fetching only relevant new data to maintain efficiency and reduce redundancy.
Running the Application:
Environment Configuration: Set MY_APP_ENV to select the operating environment. Adjust settings in development.json or testing.json for database paths, server details, and logging configurations.

Launch: Execute python run.py from the project root to start the Flask server. Navigate to the application at the designated URL and port.

Utilizing the Web Interface:
Home and Data Retrieval Forms: Access forms for running Flex Queries and processing dividend data through intuitive web pages, enhancing user interaction and data management capabilities.
Dividend Data Management: Leverage automated processes to fetch, parse, and store up-to-date dividend information in the database, streamlining financial data analysis and accessibility.
Development, Testing, and Maintenance:
Comprehensive Testing Framework: Utilize run_tests.py for executing a suite of tests, ensuring robustness and reliability of web and database functionalities.
Advanced Logging: Detailed logs facilitate monitoring and troubleshooting, with distinct log files for development and testing environments, enhancing maintainability.