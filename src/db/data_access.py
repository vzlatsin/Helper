# data_access.py

import sqlite3
import logging
from sqlite3 import Error
from datetime import datetime, timedelta

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def insert_dividend(conn, symbol, amount, ex_date, pay_date):
    """
    Insert a new dividend into the dividends table
    :param conn:
    :param symbol: string
    :param amount: float
    :param ex_date: date
    :param pay_date: date
    :return: dividend id
    """
    sql = ''' INSERT INTO dividends(symbol, amount, ex_date, pay_date)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (symbol, amount, ex_date, pay_date))
    conn.commit()
    return cur.lastrowid

def insert_dividend_if_not_exists(conn, symbol, amount, ex_date, pay_date):
    """
    Insert a new dividend into the dividends table if it does not already exist.
   
    :param conn: The database connection object
    :param symbol: The stock symbol
    :param amount: The dividend amount
    :param ex_date: The ex-dividend date
    :param pay_date: The payment date
    """
    # Check if the record already exists
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM dividends WHERE symbol = ? AND ex_date = ? AND amount = ?", (symbol, ex_date, amount))
    exists = cur.fetchone()[0] > 0  # True if the count is more than 0

    # If the record does not exist, insert it
    if not exists:
        cur.execute("INSERT INTO dividends (symbol, amount, ex_date, pay_date) VALUES (?, ?, ?, ?)",
                    (symbol, amount, ex_date, pay_date))
        conn.commit()
    else:
        logging.info(f'Record exists in DB: {symbol} date: {ex_date} amount: {amount}')



def count_dividend_records(conn):
    """
    Count the number of dividend records in the database.
    :param conn: the Connection object
    :return: the count of dividend records
    """
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM dividends")
    count = cur.fetchone()[0]
    return count

def get_latest_dividend_date(conn):
    """
    Query the latest dividend date from the database.
    :param conn: SQLite connection object
    :return: The latest date as a datetime object or None if no data is found.
    """
    cur = conn.cursor()
    cur.execute("SELECT MAX(pay_date) FROM dividends")
    result = cur.fetchone()
    if result[0]:
        return datetime.strptime(result[0], '%Y-%m-%d')
    else:
        return None
    
import sqlite3

def fetch_dividends_from_db(conn):
    """
    Fetch dividend records from the SQLite database using an existing connection.
    :param conn: An open SQLite database connection object.
    :return: A list of dictionaries, each representing a dividend record.
    """
    dividends = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT symbol, amount, ex_date, pay_date FROM dividends")
        rows = cursor.fetchall()

        for row in rows:
            dividend = {
                'symbol': row[0],
                'amount': row[1],
                'ex_date': row[2],
                'pay_date': row[3]
            }
            dividends.append(dividend)
       
    except sqlite3.Error as e:
        print(f"Database error: {e}")
   
    return dividends

# Specify the path to your SQLite database file
database = "path/to/your/database.db"

"""
# Create a database connection
conn = create_connection(database)

with conn:
    # Insert a new record into the dividends table
    dividend_id = insert_dividend(conn, 'AAPL', 0.82, '2021-08-06', '2021-08-13')
    print(f"Inserted dividend with id: {dividend_id}")

"""    