# test_file_operations.py
import unittest
from src.file_operations import compare_sorted_files,write_transactions_to_file, compare_files, compare_sorted_files_with_difflib
import os
import difflib

class TestFileOperations(unittest.TestCase):
    def test_write_transactions_to_file(self):
        # Define some dummy transactions
        transactions = [
            {'symbol': 'AAPL', 'amount': 10, 'ex_date': '2023-01-01', 'pay_date': '2023-01-02'},
            {'symbol': 'MSFT', 'amount': 20, 'ex_date': '2023-02-01', 'pay_date': '2023-02-02'}
        ]
        filename = "test_transactions.txt"
       
        # Write the transactions to file
        write_transactions_to_file(transactions, filename)
       
        # Ensure file exists
        self.assertTrue(os.path.exists(filename))
       
        # Read the file and verify contents
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)
            self.assertIn('AAPL', lines[0])
            self.assertIn('MSFT', lines[1])
       
        # Clean up: remove the test file
        os.remove(filename)

    def test_compare_files(self):
        # Create two temporary files with differences
        file1_path = "temp_file1.txt"
        file2_path = "temp_file2.txt"
        with open(file1_path, 'w') as file1, open(file2_path, 'w') as file2:
            file1.write("Line 1\nLine 2\nLine 3\n")
            file2.write("Line 1\nLine 2 - modified\nLine 3\n")

        # Compare the files
        differences = compare_files(file1_path, file2_path)
       
        # Verify the differences
        self.assertEqual(len(differences), 1)  # Expecting 1 difference
        self.assertEqual(differences[0][0], 2)  # Difference on line 2
        self.assertEqual(differences[0][1], "Line 2")  # Original line in file1
        self.assertEqual(differences[0][2], "Line 2 - modified")  # Modified line in file2
       
        # Clean up: remove the temporary files
        os.remove(file1_path)
        os.remove(file2_path)

    def test_compare_sorted_files_with_difflib(self):
        # These file paths should be to test files you've prepared with known differences
        file_path1 = 'tests/test_files/ib_dividends_sorted.txt'
        file_path2 = 'tests/test_files/db_dividends_sorted.txt'
       
        discrepancies = compare_sorted_files_with_difflib(file_path1, file_path2)
       
        # The assertion here depends on the expected discrepancies you've set up in your test files
        # For example, if you expect at least one discrepancy
        self.assertTrue(len(discrepancies) > 0)
        # To be more specific, you can check the content of the discrepancies
        # Example:
        # self.assertIn("- expected_line_here", discrepancies)
        # self.assertIn("+ unexpected_line_here", discrepancies)

if __name__ == '__main__':
    unittest.main()