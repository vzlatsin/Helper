import sqlite3

def check_backlog():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database, timeout=10)  # Set timeout to 10 seconds
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM backlog")
    rows = cursor.fetchall()

    print("Contents of backlog table:")
    for row in rows:
        print(row)

    conn.close()

def clear_backlog():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database, timeout=10)  # Set timeout to 10 seconds
    cursor = conn.cursor()

    cursor.execute("DELETE FROM backlog")
    conn.commit()
    print("All backlog records have been deleted.")

    conn.close()

if __name__ == "__main__":
    check_backlog()  # Display all records first
    clear_backlog()  # Then delete all records
    check_backlog()  # Check again to confirm deletion
