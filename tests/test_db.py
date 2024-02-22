
import unittest
"""
import sqlite3
from src.db.data_access import insert_dividend, create_connection

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Connect to your test database
        self.conn = sqlite3.connect(':memory:')  # Use in-memory database for tests
        self.cur = self.conn.cursor()
       
        # Create a table for testing
        self.cur.execute('''
            CREATE TABLE dividends (
                symbol TEXT,
                amount REAL,
                ex_date TEXT,
                pay_date TEXT
            )
        ''')

    def tearDown(self):
        # Close the connection after tests
        self.conn.close()

    def test_insert_dividend(self):
        # Test inserting a dividend record
        insert_dividend(self.conn, 'AAPL', 0.82, '2021-08-06', '2021-08-13')
        #self.cur.execute('INSERT INTO dividends (symbol, amount, ex_date, pay_date) VALUES (?, ?, ?, ?)',
        #                 ('AAPL', 0.82, '2021-08-06', '2021-08-13'))
        #self.conn.commit()
       
        # Retrieve the inserted record and assert its content
        self.cur.execute('SELECT * FROM dividends WHERE symbol = "AAPL"')
        record = self.cur.fetchone()
        self.assertEqual(record, ('AAPL', 0.82, '2021-08-06', '2021-08-13'))

"""
if __name__ == '__main__':
    unittest.main()