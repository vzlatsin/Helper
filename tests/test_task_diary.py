import unittest
from src.db.data_access import create_connection, save_time_entry, fetch_tasks_for_date, save_task_diary_entry, fetch_task_diary_entries

class TestTaskDiary(unittest.TestCase):

    def setUp(self):
        self.conn = create_connection(":memory:")
        self.conn.execute('''CREATE TABLE IF NOT EXISTS time_entries (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                date TEXT NOT NULL,
                                start_time TEXT,
                                end_time TEXT,
                                task_description TEXT NOT NULL,
                                status TEXT DEFAULT 'pending'
                            );''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS task_diary (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                date TEXT NOT NULL,
                                reflections TEXT NOT NULL
                            );''')

    def tearDown(self):
        self.conn.close()

    def test_save_time_entry(self):
        date = "2024-07-01"
        start_time = "09:00"
        end_time = "10:00"
        task_description = "Test Task"
        status = "pending"
        entry_id = save_time_entry(self.conn, date, start_time, end_time, task_description, status)
        self.assertIsNotNone(entry_id)

    def test_fetch_tasks_for_date(self):
        date = "2024-07-01"
        start_time1 = "09:00"
        end_time1 = "10:00"
        task_description1 = "Test Task 1"
        status1 = "pending"
        
        start_time2 = "10:00"
        end_time2 = "11:00"
        task_description2 = "Test Task 2"
        status2 = "pending"

        save_time_entry(self.conn, date, start_time1, end_time1, task_description1, status1)
        save_time_entry(self.conn, date, start_time2, end_time2, task_description2, status2)

        tasks = fetch_tasks_for_date(self.conn, date)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0]['task_description'], "Test Task 1")
        self.assertEqual(tasks[1]['task_description'], "Test Task 2")
        self.assertEqual(tasks[0]['status'], "pending")
        self.assertEqual(tasks[1]['status'], "pending")

    def test_save_task_diary_entry(self):
        data = {
            "date": "2024-07-01",
            "reflections": "Reflections on the tasks"
        }
        entry_id = save_task_diary_entry(self.conn, data)
        self.assertIsNotNone(entry_id)

    def test_fetch_task_diary_entries(self):
        data1 = {
            "date": "2024-07-01",
            "reflections": "Reflection 1"
        }
        data2 = {
            "date": "2024-07-02",
            "reflections": "Reflection 2"
        }
        save_task_diary_entry(self.conn, data1)
        save_task_diary_entry(self.conn, data2)
        entries = fetch_task_diary_entries(self.conn)
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]['reflections'], "Reflection 1")
        self.assertEqual(entries[1]['reflections'], "Reflection 2")

if __name__ == "__main__":
    unittest.main()
