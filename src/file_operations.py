# file_operations.py
import difflib

def write_transactions_to_file(transactions, filename):
    """Writes a list of transactions to a file."""
    with open(filename, 'w') as file:
        for transaction in transactions:
            # Assuming transaction is a dictionary with keys 'symbol', 'amount', 'dateTime', and 'reportDate'
            # Adjust the keys as necessary to match your actual data structure
            line = f"{transaction['symbol']}, {transaction['amount']}, {transaction['ex_date']}, {transaction['pay_date']}\n"
            file.write(line)

def read_transactions_from_file(filename):
    """Reads transactions from a file and returns a list of transactions."""
    transactions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            transaction = (parts[0], float(parts[1]), parts[2], parts[3])
            transactions.append(transaction)
    return transactions

def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    differences = []
    for i, (line1, line2) in enumerate(zip(file1_lines, file2_lines)):
        if line1 != line2:
            differences.append((i+1, line1.strip(), line2.strip()))  # Line number, file1 line, file2 line

    return differences

def compare_sorted_files(file_path1, file_path2):
    # Read and sort the contents of the first file
    with open(file_path1, 'r') as file1:
        file1_lines = file1.readlines()
    sorted_file1_lines = sorted(file1_lines)

    # Read and sort the contents of the second file
    with open(file_path2, 'r') as file2:
        file2_lines = file2.readlines()
    sorted_file2_lines = sorted(file2_lines)

    # Compare the sorted contents of both files
    discrepancies = []
    for index, (line1, line2) in enumerate(zip(sorted_file1_lines, sorted_file2_lines)):
        if line1 != line2:
            discrepancies.append((index + 1, line1.strip(), line2.strip()))

    # Check for any remaining lines in either file
    longer_list = sorted_file1_lines if len(sorted_file1_lines) > len(sorted_file2_lines) else sorted_file2_lines
    for extra_index in range(index + 1, len(longer_list)):
        if extra_index < len(sorted_file1_lines):
            discrepancies.append((extra_index + 1, sorted_file1_lines[extra_index].strip(), 'No corresponding line'))
        if extra_index < len(sorted_file2_lines):
            discrepancies.append((extra_index + 1, 'No corresponding line', sorted_file2_lines[extra_index].strip()))

    return discrepancies

def compare_sorted_files_with_difflib(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()

    diff = difflib.unified_diff(file1_lines, file2_lines, fromfile='file1', tofile='file2', lineterm='')

    discrepancies = [line.strip() for line in diff if line.startswith('-') or line.startswith('+')]
    return discrepancies