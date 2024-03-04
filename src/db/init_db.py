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


    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        create_table(conn, sql_create_dividends_table)

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()