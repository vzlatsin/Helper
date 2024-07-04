import sqlite3

def check_tasks():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM task_diary")
    rows = cursor.fetchall()

    print("Contents of task_diary table:")
    for row in rows:
        print(row)

    conn.close()

def clear_tasks():
    database = "src/db/database.db"  # Update this path to your actual database path

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM task_diary")
    cursor.execute("DELETE FROM time_entries")
    conn.commit()
    print("All tasks have been deleted.")

    conn.close()

if __name__ == "__main__":
    clear_tasks()
    check_tasks()
