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

