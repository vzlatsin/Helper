# data_access.py

import sqlite3
import logging
from sqlite3 import Error
from datetime import datetime, timedelta, date
import json 

# Configure logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


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
            "task_description": row[4],
            "status": row[5] 
        }
        entries.append(entry)
    return entries


def save_time_entry(conn, date, start_time, end_time, task_description, status='pending'):
    """
    Insert a new time entry into the time_entries table
    :param conn: Database connection object
    :param date: Task date
    :param start_time: Task start time
    :param end_time: Task end time
    :param task_description: Description of the task
    :param status: Status of the task (default is 'pending')
    :return: id of the inserted entry
    """
    try:
        logging.info(f"Attempting to save time entry: date={date}, start_time={start_time}, end_time={end_time}, task_description={task_description}, status={status}")
        
        sql = ''' INSERT INTO time_entries(date, start_time, end_time, task_description, status)
                  VALUES(?, ?, ?, ?, ?) '''
        cur = conn.cursor()
        cur.execute(sql, (date, start_time, end_time, task_description, status))
        conn.commit()
        logging.info(f"Successfully saved time entry with id: {cur.lastrowid}")
        return cur.lastrowid
    except Exception as e:
        logging.error(f"Error saving time entry: {e}")
        return None
    

def save_task_diary_entry(conn, data):
    """ Save a task diary entry to the database """
    sql = ''' INSERT INTO task_diary(date, reflections)
              VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (data['date'], data['reflections']))
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
            "reflections": row[2]
        }
        entries.append(entry)
    return entries

def fetch_tasks_for_date(conn, date):
    cur = conn.cursor()
    cur.execute("SELECT * FROM time_entries WHERE date = ?", (date,))
    rows = cur.fetchall()
    tasks = [{'id': row[0], 'date': row[1], 'start_time': row[2], 'end_time': row[3], 'task_description': row[4], "status": row[5]} for row in rows]
    return tasks

def mark_tasks_as_selected(conn, date):
    cur = conn.cursor()
    cur.execute("UPDATE time_entries SET status = 'selected' WHERE date = ?", (date,))
    conn.commit()

def add_task(conn, date, start_time, end_time, task_description):
    cur = conn.cursor()
    cur.execute("INSERT INTO time_entries (date, start_time, end_time, task_description, status) VALUES (?, ?, ?, ?, 'pending')", 
                (date, start_time, end_time, task_description))
    conn.commit()

def mark_tasks_as_closed(conn, task_ids):
    cursor = conn.cursor()
    cursor.executemany("UPDATE time_entries SET status = 'selected' WHERE id = ?", [(task_id,) for task_id in task_ids])
    conn.commit()

def revert_task_statuses(conn, task_ids):
    cursor = conn.cursor()
    cursor.executemany("UPDATE time_entries SET status = 'pending' WHERE id = ?", [(task_id,) for task_id in task_ids])
    conn.commit()

def validate_pending_status(conn, task_ids):
    cursor = conn.cursor()
    placeholder = ', '.join('?' for _ in task_ids)  # Create a placeholder string
    query = f"SELECT id FROM time_entries WHERE id IN ({placeholder}) AND status = 'pending'"
    print(f"Running query: {query} with task_ids: {task_ids}")
    cursor.execute(query, task_ids)
    valid_ids = [row[0] for row in cursor.fetchall()]
    print(f"Valid task IDs with 'pending' status: {valid_ids}")
    return valid_ids

def fetch_forgotten_tasks(conn):
    try:
        cursor = conn.cursor()
        cursor.row_factory = sqlite3.Row  # This will allow us to use row objects which can be converted to dicts
        today = date.today().isoformat()
        cursor.execute("""
            SELECT * FROM time_entries 
            WHERE status = 'pending' AND date < ?
        """, (today,))
        rows = cursor.fetchall()
        tasks = [dict(row) for row in rows]  # Convert row objects to dictionaries
        return tasks
    except Exception as e:
        print(f"Error fetching forgotten tasks: {str(e)}")
        return []

def insert_backlog_entry(conn, task_description):
    """
    Insert a new entry into the backlog table
    :param conn: Database connection object
    :param task_description: Description of the task
    :return: id of the inserted entry
    """
    sql = ''' INSERT INTO backlog(task_description, date_added)
              VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, (task_description, date.today().isoformat()))
    conn.commit()
    return cur.lastrowid

def add_task_to_backlog(conn, task_description):
    try:
        cursor = conn.cursor()
        sql = ''' INSERT INTO backlog (task_description, date_added)
                  VALUES (?, ?) '''
        logger.debug(f"Executing SQL: {sql} with task_description: {task_description} and date_added: {date.today().isoformat()}")
        cursor.execute(sql, (task_description, date.today().isoformat()))
        conn.commit()
        logger.info("Task successfully added to backlog")
        return cursor.lastrowid is not None
    except Exception as e:
        logger.error(f"Error adding task to backlog: {str(e)}")
        return False




def fetch_backlog_entries(conn):
    """
    Query all rows in the backlog table
    :param conn: the Connection object
    :return: a list of dictionaries containing all backlog entries
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM backlog")
    rows = cur.fetchall()
    entries = [{'id': row[0], 'task_description': row[1], 'date_added': row[2]} for row in rows]
    return entries

# data_access.py
def move_task_to_backlog(conn, task_id):
    try:
        cursor = conn.cursor()

        # Fetch the task from time_entries
        cursor.execute("SELECT task_description FROM time_entries WHERE id = ?", (task_id,))
        task = cursor.fetchone()

        if task:
            task_description = task[0]
            # Insert the task into the backlog table
            cursor.execute("INSERT INTO backlog (task_description) VALUES (?)", (task_description,))
            # Delete the task from time_entries
            cursor.execute("DELETE FROM time_entries WHERE id = ?", (task_id,))
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        print(f"Error moving task to backlog: {str(e)}")
        return False


def move_task_to_time_entries(conn, backlog_id, date, start_time, end_time):
    """
    Move a task from backlog to time_entries
    :param conn: Database connection object
    :param backlog_id: ID of the backlog entry to move
    :param date: Task date
    :param start_time: Task start time
    :param end_time: Task end time
    """
    cur = conn.cursor()
    cur.execute("SELECT task_description FROM backlog WHERE id = ?", (backlog_id,))
    task = cur.fetchone()
    if task:
        task_description = task[0]
        insert_time_entry(conn, date, start_time, end_time, task_description)
        cur.execute("DELETE FROM backlog WHERE id = ?", (backlog_id,))
        conn.commit()
        return True
    else:
        return False


# Unified Inbox Functions

def insert_unified_inbox_item(conn, description):
    """
    Insert a new item into the unified_inbox table
    :param conn: Database connection object
    :param description: Text description of the item
    :return: id of the inserted entry
    """
    sql = ''' INSERT INTO unified_inbox(description)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (description,))
    conn.commit()
    return cur.lastrowid

def fetch_unified_inbox_items(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, description FROM unified_inbox")
        rows = cur.fetchall()
        return [{"id": row[0], "description": row[1]} for row in rows]
    except Exception as e:
        print(f"Error fetching items from the Unified Inbox: {str(e)}")
        return []


def update_unified_inbox_item(conn, item_id, description):
    """
    Update the description of an item in the unified_inbox table
    :param conn: Database connection object
    :param item_id: ID of the item
    :param description: New description of the item
    :return: None
    """
    sql = ''' UPDATE unified_inbox
              SET description = ?
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (description, item_id))
    conn.commit()

def delete_unified_inbox_item(conn, item_id):
    """
    Delete an item from the unified_inbox table
    :param conn: Database connection object
    :param item_id: ID of the item
    :return: None
    """
    sql = ''' DELETE FROM unified_inbox
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (item_id,))
    conn.commit()



# data_access.py
def get_dummy_today_tasks():
    return [
        {"id": 1, "task": "Dummy Task 1", "date": "2024-07-02"},
        {"id": 2, "task": "Dummy Task 2", "date": "2024-07-02"}
    ]





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