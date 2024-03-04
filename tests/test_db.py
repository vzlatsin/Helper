
import unittest

import sqlite3
from src.db.data_access import insert_dividend, create_connection, fetch_dividends_from_db, fetch_dividends_by_quarter

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Connect to your test database
        self.conn = sqlite3.connect(':memory:')  # Use in-memory database for tests
        self.cur = self.conn.cursor()
       
        # Create a table for testing
        self.cur.execute('''
            CREATE TABLE dividends (
                id INTEGER PRIMARY KEY,
                symbol TEXT NOT NULL,
                amount REAL NOT NULL,
                ex_date TEXT NOT NULL,
                pay_date TEXT NOT NULL
            )
        ''')

    def tearDown(self):
        # Close the connection after tests
        self.conn.close()

    def test_insert_and_fetch_dividend(self):
        # Insert two dividend records
        insert_dividend(self.conn, 'AAPL', 0.82, '2021-08-06', '2021-08-13')
        insert_dividend(self.conn, 'MSFT', 1.00, '2021-09-10', '2021-09-17')

        # Fetch dividends from the database to verify both insertions
        dividends = fetch_dividends_from_db(self.conn)
        expected_dividends = [
            {'symbol': 'AAPL', 'amount': 0.82, 'ex_date': '2021-08-06', 'pay_date': '2021-08-13'},
            {'symbol': 'MSFT', 'amount': 1.00, 'ex_date': '2021-09-10', 'pay_date': '2021-09-17'}
        ]

        # Sort the lists by symbol to ensure the order matches for comparison
        dividends.sort(key=lambda x: x['symbol'])
        expected_dividends.sort(key=lambda x: x['symbol'])

        self.assertEqual(dividends, expected_dividends, "The fetched dividend records do not match the expected values.")

        # Additional verification to ensure exactly two records are present
        self.assertEqual(len(dividends), 2, "There should be exactly two dividend records.")

    def test_fetch_dividends_by_quarter(self):
        # Insert dividend records spanning multiple quarters
        insert_dividend(self.conn, 'AAPL', 0.5, '2021-01-15', '20210131')
        insert_dividend(self.conn, 'AAPL', 0.5, '2021-04-15', '20210430')
        insert_dividend(self.conn, 'MSFT', 1.0, '2021-07-15', '20210731')
        insert_dividend(self.conn, 'GOOG', 1.5, '2021-10-15', '20211031')

        # Fetch aggregated dividends by quarter
        dividends_by_quarter = fetch_dividends_by_quarter(self.conn)
        
        # Define the expected results
        expected_results = [
            ('2021 Q1', 0.5),
            ('2021 Q2', 0.5),
            ('2021 Q3', 1.0),
            ('2021 Q4', 1.5)
        ]

        self.assertEqual(dividends_by_quarter, expected_results, "The aggregated dividends by quarter do not match the expected values.")

if __name__ == '__main__':
    unittest.main()