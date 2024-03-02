Financial Data Automation Web Application
This application automates the retrieval, processing, and storage of financial information from Interactive Brokers using Python, Flask, and SQLite. Initially focused on dividends, it's designed to evolve into a comprehensive tool for automating various financial tasks, including tax return preparation.

Broad Objectives
Versatile Financial Data Handling: From dividends to broader financial transactions, aimed at simplifying personal finance management.
Tax Preparation Assistance: Streamlines the collection and organization of information necessary for tax returns, reducing manual effort and increasing accuracy.
Expandable Framework: Structured to facilitate the addition of new modules for different financial tasks over time.
Core Features
Interactive Web Interface: Facilitates manual data operations and viewing of financial reports through a user-friendly web interface.
Automated Data Integration: Leverages automated processes for fetching, parsing, and storing financial data in a structured database.
Customizable Reporting: Supports generating tailored reports, crucial for tax preparation and financial analysis.
Project Structure and Key Components
/src Directory: The backbone of the application, containing all the logic and functionality.

app.py: Flask application setup and web route definitions. Central to web interface modifications.
/db: Database scripts for schema initialization (init_db.py) and data manipulation (data_access.py). Extend here for new data types.
flex_query.py: Interacts with brokerage services for data retrieval. Update for new data sources or changes in API.
Utility Scripts (helper.py, report_parser.py): Assist with various tasks like connectivity and data parsing.
Configuration and Testing: Configuration files (/config) for environment-specific settings, and a testing suite (/tests) to ensure reliability.

Getting Started
Setup
Clone this repository.
Install Dependencies: pip install -r requirements.txt
Initialize Database: python src/db/init_db.py
Running the Application
python run.py starts the server. Access it via http://localhost:5000 to explore its features.

Expanding Functionality
To introduce new functionalities, such as additional financial data processing or tax report generation:

Web Interface: Adapt app.py and /templates for new workflows or data inputs.
Data Processing: Extend flex_query.py for additional data retrieval; adjust data_access.py for new database operations.
Schema Adjustments: Modify init_db.py for any database schema updates to accommodate new data types.
Development Notes
Testing New Features: Incorporate tests in /tests to cover new functionalities, maintaining application integrity.
Logging: Utilize development.log or testing.log for debugging and monitoring application behavior.
Contributing and Support
While currently focused on personal finance management, contributions or suggestions for expanding its capabilities are welcome. For collaboration or questions, please open an issue in the repository.

Future Directions
Tax Reporting Module: A planned extension to simplify tax return preparation, automatically organizing relevant financial data.
Investment Analysis Tools: To offer insights into portfolio performance and tax implications.
License and Contact
For personal use; please contact for broader usage rights or contributions.