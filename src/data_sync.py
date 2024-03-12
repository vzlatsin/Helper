import logging  # Ensure logging is imported
from datetime import datetime
from src.file_operations import compare_files, compare_sorted_files, compare_sorted_files_with_difflib
from src.file_operations import write_transactions_to_file

def compare_dividend_data(db_dividends, ib_dividends):
    logging.info("compare_dividend_data: need to compare two files")
    discrepancies = []
    # Assuming ex_date is in 'YYYYMMDD' format
    start_date_ib = min([datetime.strptime(d['ex_date'], '%Y%m%d') for d in ib_dividends])
    end_date_ib = max([datetime.strptime(d['ex_date'], '%Y%m%d') for d in ib_dividends])

    # Log the count of records from both sources
    logging.info("Total IB dividends records: %s", len(ib_dividends))
    logging.info("Total DB dividends records: %s", len(db_dividends))
    discrepancies.append({
            "type": "Count Discrepancy",
            "detail": f"IB records count: {len(ib_dividends)}, DB records count: {len(db_dividends)}"
        })
    
    filtered_db_dividends = [d for d in db_dividends if start_date_ib <= datetime.strptime(d['ex_date'], '%Y%m%d') <= end_date_ib]


    # Compare the count of records after filtering DB dividends to match the IB report's time window
    if len(ib_dividends) != len(filtered_db_dividends):
        logging.info("Need to compare records within the IB report's time window.")
        # Ensure you write the filtered DB dividends to 'filtered_db_dividends.txt' for an accurate comparison
        write_transactions_to_file(filtered_db_dividends, 'filtered_db_dividends.txt')
        
        # Compare files and add differences to discrepancies
        differences = compare_sorted_files_with_difflib('ib_dividends.txt', 'filtered_db_dividends.txt')
        logging.info(f"Differences within the relevant time window: {differences}")

        log_discrepancies(differences)
    else:
        logging.info("The length of two lists is the same")
         
    return discrepancies

def log_discrepancies(differences):
    additions = [line[1:] for line in differences if line.startswith('+') and not line.startswith('+++')]
    deletions = [line[1:] for line in differences if line.startswith('-') and not line.startswith('---')]

    # Identify records that appear in both added and removed, indicating a potential update rather than a simple add/remove
    common_records = set(additions) & set(deletions)
    for record in common_records:
        logging.info(f"UPDATED: {record}")
    
    # Filter out common records for clear addition/removal reporting
    pure_additions = [record for record in additions if record not in common_records]
    pure_deletions = [record for record in deletions if record not in common_records]

    for addition in pure_additions:
        logging.info(f"ADDED: {addition}")
    for deletion in pure_deletions:
        logging.info(f"REMOVED: {deletion}")

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



