import sqlite3

def check_time_entries():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database, timeout=10)  # Set timeout to 10 seconds
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM time_entries")
    rows = cursor.fetchall()

    print("Contents of time_entries table:")
    for row in rows:
        print(row)

    conn.close()

def clear_time_entries():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database, timeout=10)  # Set timeout to 10 seconds
    cursor = conn.cursor()

    cursor.execute("DELETE FROM time_entries")
    conn.commit()
    print("All time_entries records have been deleted.")

    conn.close()

if __name__ == "__main__":
    check_time_entries()  # Display all records first
    clear_time_entries()  # Then delete all records
    check_time_entries()  # Check again to confirm deletion
