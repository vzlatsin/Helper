# data_access.py

import sqlite3
import logging
from sqlite3 import Error
from datetime import datetime, timedelta
import json 

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
        logging.info(f'Inserted new record into DB: {symbol}, date: {ex_date}, amount: {amount}')
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

def get_dividend_date_range(conn):
    cur = conn.cursor()
    cur.execute("SELECT MIN(ex_date), MAX(ex_date) FROM dividends")
    min_date, max_date = cur.fetchone()
    return min_date, max_date

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

def fetch_dividends_by_quarter(conn):
    """
    Fetch dividends data from the database and aggregate it by quarter,
    with pay_date in the 'YYYYMMDD' format.
    
    :param conn: An open SQLite database connection object.
    :return: A list of tuples, each containing the quarter and the sum of dividends for that quarter.
    """
    dividends_by_quarter = []
    try:
        cursor = conn.cursor()
        query = """
        SELECT
            SUBSTR(pay_date, 1, 4) || ' Q' || CASE
                WHEN CAST(SUBSTR(pay_date, 5, 2) AS INTEGER) BETWEEN 1 AND 3 THEN '1'
                WHEN CAST(SUBSTR(pay_date, 5, 2) AS INTEGER) BETWEEN 4 AND 6 THEN '2'
                WHEN CAST(SUBSTR(pay_date, 5, 2) AS INTEGER) BETWEEN 7 AND 9 THEN '3'
                ELSE '4'
            END AS Quarter,
            SUM(amount) AS TotalDividends
        FROM dividends
        GROUP BY Quarter
        ORDER BY Quarter;
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            # Each row is a tuple (Quarter, TotalDividends)
            dividends_by_quarter.append(row)

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
    return dividends_by_quarter

def insert_trade_if_not_exists(conn, trade_data):
    """
    Insert a new trade into the trades table if it does not already exist, based on symbol, dateTime, and tradeDate.

    :param conn: Database connection object.
    :param trade_data: Dictionary containing trade details including all columns from the trades table.
    """
    try:
        # Extract identifying details from trade_data dictionary to check for existing trade
        symbol = trade_data['symbol']
        dateTime = trade_data.get('dateTime', None)
        tradeDate = trade_data['tradeDate']

        # Construct the query to check for existing trade
        check_query = """SELECT COUNT(*) FROM trades 
                         WHERE symbol = ? AND dateTime = ? AND tradeDate = ?"""
        cur = conn.cursor()
        cur.execute(check_query, (symbol, dateTime, tradeDate))
        exists = cur.fetchone()[0] > 0  # True if count is more than 0

        # If the trade does not exist, insert it
        if not exists:
            insert_query = '''INSERT INTO trades(symbol, dateTime, putCall, transactionType, quantity, tradePrice, 
                                                 closePrice, cost, origTradePrice, origTradeDate, buySell, orderTime, 
                                                 openDateTime, assetCategory, strike, expiry, tradeDate)
                              VALUES(:symbol, :dateTime, :putCall, :transactionType, :quantity, :tradePrice, 
                                     :closePrice, :cost, :origTradePrice, :origTradeDate, :buySell, :orderTime, 
                                     :openDateTime, :assetCategory, :strike, :expiry, :tradeDate)'''
            cur.execute(insert_query, trade_data)
            conn.commit()
            logging.info("Trade inserted successfully.")
        else:
            logging.info("Trade already exists.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception in insert_trade_if_not_exists: {e}")



def fetch_all_trades(conn):
    """
    Fetch all trade records from the trades table.
    :param conn: Database connection object.
    :return: A list of tuples containing all trade records.
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM trades")
    trades = cur.fetchall()
    return trades


def get_trades_by_symbol(conn, symbol):
    """
    Query trades by symbol.
    
    :param conn: the Connection object
    :param symbol: string, the symbol to query trades for
    :return: a list of dictionaries containing trade data
    """
    cur = conn.cursor()
    query = """
    SELECT id, symbol, dateTime, putCall, transactionType, quantity, 
           tradePrice, closePrice, cost, origTradePrice, origTradeDate, 
           buySell, orderTime, openDateTime, assetCategory, strike, 
           expiry, tradeDate
    FROM trades
    WHERE symbol like ?
    ORDER BY tradeDate ASC
    """
    cur.execute(query, (f"{symbol}%",))
    
    rows = cur.fetchall()
    
    # Converting row data to a list of dictionaries for easier processing
    trades = [
        {"id": row[0], "symbol": row[1], "dateTime": row[2], "putCall": row[3], 
         "transactionType": row[4], "quantity": row[5], "tradePrice": row[6], 
         "closePrice": row[7], "cost": row[8], "origTradePrice": row[9], 
         "origTradeDate": row[10], "buySell": row[11], "orderTime": row[12], 
         "openDateTime": row[13], "assetCategory": row[14], "strike": row[15], 
         "expiry": row[16], "tradeDate": row[17]}
        for row in rows
    ]
    
    return trades

def insert_time_entry(conn, date, start_time, end_time, task_description):
    """
    Insert a new time entry into the time_entries table
    :param conn: Database connection object
    :param date: Task date
    :param start_time: Task start time
    :param end_time: Task end time
    :param task_description: Description of the task
    :return: id of the inserted entry
    """
    sql = ''' INSERT INTO time_entries(date, start_time, end_time, task_description)
              VALUES(?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (date, start_time, end_time, task_description))
    conn.commit()
    return cur.lastrowid

def fetch_time_entries(conn):
    """
    Query all rows in the time_entries table
    :param conn: the Connection object
    :return: a list of dictionaries containing all time entries
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM time_entries")

    rows = cur.fetchall()
    entries = []
    for row in rows:
        entry = {
            "id": row[0],
            "date": row[1],
            "start_time": row[2],
            "end_time": row[3],
            "task_description": row[4]
        }
        entries.append(entry)
    return entries


def save_time_entry(conn, data):
    """
    Save a time entry to the database
    :param conn: Database connection object
    :param data: Dictionary containing date, start_time, end_time, and task_description
    """
    return insert_time_entry(conn, data['date'], data['start_time'], data['end_time'], data['task_description'])

def save_task_diary_entry(conn, data):
    """ Save a task diary entry to the database """
    sql = ''' INSERT INTO task_diary(date, tasks, reflections)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (data['date'], json.dumps(data['tasks']), data['reflections']))
    conn.commit()
    return cur.lastrowid

def fetch_task_diary_entries(conn):
    """ Fetch all task diary entries from the database """
    cur = conn.cursor()
    cur.execute("SELECT * FROM task_diary")
    rows = cur.fetchall()
    entries = []
    for row in rows:
        entry = {
            "id": row[0],
            "date": row[1],
            "tasks": json.loads(row[2]),
            "reflections": row[3]
        }
        entries.append(entry)
    return entries

def fetch_todays_tasks(conn):
    """
    Fetch tasks for today's date from the task_diary table.
    :param conn: the Connection object
    :return: a list of dictionaries containing today's tasks
    """
    today_date = datetime.now().date().isoformat()
    cur = conn.cursor()
    cur.execute("SELECT tasks FROM task_diary WHERE date = ?", (today_date,))
    rows = cur.fetchall()
    tasks = []
    for row in rows:
        tasks.extend(json.loads(row[0]))
    return tasks



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