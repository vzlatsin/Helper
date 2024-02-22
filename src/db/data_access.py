import sqlite3
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