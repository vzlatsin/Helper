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

## Expanding Functionality

To add new functionalities:

- **Web Interface**: Modify `app.py` and `/templates` for new data inputs or workflows.
- **Data Processing**: Update `flex_query.py` for additional data retrieval; adjust `data_access.py` for new database operations.
- **Schema Adjustments**: Update `init_db.py` for database schema changes to support new data types.

## Development Notes

- **Testing New Features**: Add tests in the `/tests` subfolder to cover new functionalities, ensuring the application's integrity. Run tests using the command `python run_tests.py`.
- **Logging**: Utilize `development.log` or `testing.log` for application monitoring and debugging.

## Contributing and Support

Contributions or suggestions for expanding the application's capabilities are welcome. For collaboration or questions, please open an issue in the repository.

## Future Directions

- **Tax Reporting Module**: An upcoming extension to automate tax return preparation.
- **Investment Analysis Tools**: Planned tools for analyzing portfolio performance and tax implications.

## License and Contact

For personal use. Contact for broader usage rights or contributions.
