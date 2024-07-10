# init_db.py

import sqlite3
import os

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = os.path.join(os.getcwd(), "src/db/database.db")

    sql_create_dividends_table = """ CREATE TABLE IF NOT EXISTS dividends (
                                        id integer PRIMARY KEY,
                                        symbol text NOT NULL,
                                        amount real NOT NULL,
                                        ex_date text NOT NULL,
                                        pay_date text NOT NULL
                                    ); """

    # SQL statement for creating the trades table
    sql_create_trades_table = """CREATE TABLE IF NOT EXISTS trades (
                                id INTEGER PRIMARY KEY,
                                symbol TEXT NOT NULL,
                                dateTime TEXT,
                                putCall TEXT,
                                transactionType TEXT,
                                quantity REAL NOT NULL,
                                tradePrice REAL,
                                closePrice REAL,
                                cost REAL,
                                origTradePrice REAL,
                                origTradeDate TEXT,
                                buySell TEXT,
                                orderTime TEXT,
                                openDateTime TEXT,
                                assetCategory TEXT,
                                strike REAL,
                                expiry TEXT,
                                tradeDate TEXT
                            );"""

    sql_create_time_entries_table = """CREATE TABLE IF NOT EXISTS time_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            start_time TEXT,
            end_time TEXT,
            task_description TEXT NOT NULL,
            status text DEFAULT 'pending'
        );"""
    
    sql_create_task_diary_table = """CREATE TABLE IF NOT EXISTS task_diary (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        date TEXT NOT NULL,
                                        reflections TEXT
                                    );"""

    sql_create_backlog_table = """CREATE TABLE IF NOT EXISTS backlog (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        task_description TEXT NOT NULL,
                                        date_added TEXT NOT NULL
                                    );"""
    
    sql_create_unified_inbox_table = """ CREATE TABLE IF NOT EXISTS unified_inbox (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            description TEXT NOT NULL
                                        ); """
    
    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        # Create dividends table
        create_table(conn, sql_create_dividends_table)
        print("Dividends table created successfully.")
        
        # Create trades table
        create_table(conn, sql_create_trades_table)
        print("Trades table created successfully.")

        # Create time entries table
        create_table(conn, sql_create_time_entries_table)
        print("Time entries table created successfully.")

        # create task_diary table
        create_table(conn, sql_create_task_diary_table)
        print("Task diary table created successfully.")

        # Create backlog table
        create_table(conn, sql_create_backlog_table)
        print("Backlog table created successfully.")

        # Create unified inbox table
        create_table(conn, sql_create_unified_inbox_table)
        print("Unified Inbox table created successfully.")

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()