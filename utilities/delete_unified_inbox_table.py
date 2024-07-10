import sqlite3

def check_unified_inbox():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database, timeout=10)  # Set timeout to 10 seconds
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM unified_inbox")
    rows = cursor.fetchall()

    print("Contents of unified_inbox table:")
    for row in rows:
        print(row)

    conn.close()

def clear_unified_inbox():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database, timeout=10)  # Set timeout to 10 seconds
    cursor = conn.cursor()

    cursor.execute("DELETE FROM unified_inbox")
    conn.commit()
    print("All unified_inbox records have been deleted.")

    conn.close()

def drop_unified_inbox_table():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database, timeout=10)  # Set timeout to 10 seconds
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS unified_inbox")
    conn.commit()
    print("unified_inbox table has been dropped.")

    conn.close()

if __name__ == "__main__":
    check_unified_inbox()  # Display all records first
    clear_unified_inbox()  # Then delete all records
    check_unified_inbox()  # Check again to confirm deletion
    drop_unified_inbox_table()  # Finally, drop the table
