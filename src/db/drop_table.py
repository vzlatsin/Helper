import sqlite3
import sys
import os

def drop_table(db_file, table_name):
    """
    Drop a table from the specified SQLite database.

    :param db_file: Path to SQLite database file.
    :param table_name: Name of the table to drop.
    """
    # Create a database connection
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database {db_file}")
    except sqlite3.Error as e:
        print(e)
        return

    # Drop the table
    try:
        c = conn.cursor()
        c.execute(f'DROP TABLE IF EXISTS {table_name}')
        print(f"Table {table_name} dropped successfully.")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python drop_table.py <database_path> <table_name>")
        # example:   python src\db\drop_table.py src\db\database.db time_entries
        sys.exit(1)

    database_path = sys.argv[1]
    table_name = sys.argv[2]

    # Verify the database file exists before attempting to connect
    if not os.path.exists(database_path):
        print(f"Database file {database_path} does not exist.")
        sys.exit(1)

    drop_table(database_path, table_name)
