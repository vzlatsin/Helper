import logging  # Ensure logging is imported
from src.file_operations import compare_files, compare_sorted_files, compare_sorted_files_with_difflib

def compare_dividend_data(db_dividends, ib_dividends):
    discrepancies = []

    # Log the count of records from both sources
    print("Total IB dividends records:", len(ib_dividends))
    print("Total DB dividends records:", len(db_dividends))
    discrepancies.append({
            "type": "Count Discrepancy",
            "detail": f"IB records count: {len(ib_dividends)}, DB records count: {len(db_dividends)}"
        })
    if len(ib_dividends) != len(db_dividends):
        # Compare files and add differences to discrepancies
        differences = compare_sorted_files_with_difflib('ib_dividends.txt', 'db_dividends.txt')
        print("differences:", differences)
   
    # Log the count of records from both sources
    logging.info("Total IB dividends records: %s", len(ib_dividends))
    logging.info("Total DB dividends records: %s", len(db_dividends))
    return discrepancies

"""
    # Debugging: Log key generation for the first few records
    for div in db_dividends[:5]:
        logging.info("DB Key: %s", f"{div['symbol']}_{div['ex_date']}")
    for div in ib_dividends[:5]:
        logging.info("IB Key: %s", f"{div['symbol']}_{div['ex_date']}")

    # Convert IB and DB dividends to dictionaries for easier comparison
    db_div_dict = {f"{div['symbol']}_{div['ex_date']}": div for div in db_dividends}
    ib_div_dict = {f"{div['symbol']}_{div['ex_date']}": div for div in ib_dividends}

    # Debugging: Log the size of each set
    logging.info(f"DB div dict size: {len(db_div_dict)}, IB div dict size: {len(ib_div_dict)}")

    missing_in_db_count = 0
    extra_in_db_count = 0
    i = 0

    # Find records in IB data not in DB
    for key, ib_div in ib_div_dict.items():
        i += 1
        #logging.info(f"Processing record: {i}")
        if key not in db_div_dict:
            logging.info(f"Missing in DB: {key}")
            discrepancies.append({"type": "Missing in DB", "key": key})
            missing_in_db_count += 1

    i = 0
    # Find records in DB not in IB data
    for key, db_div in db_div_dict.items():
        i += 1
        #logging.info(f"Processing record: {i}")
        if key not in ib_div_dict:
            logging.info(f"Extra in DB: {key}")
            discrepancies.append({"type": "Extra in DB", "key": key})
            extra_in_db_count += 1

    logging.info(f"Total missing in DB: {missing_in_db_count}")
    logging.info(f"Total extra in DB: {extra_in_db_count}")

    # If no discrepancies found, log that as well
    if not discrepancies:
        logging.info("No discrepancies found between DB and IB records.")
"""
    #return discrepancies



