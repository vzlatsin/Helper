# src/ib_data_fetcher.py

from .flex_query import initiate_flex_query_report, download_flex_query_report, get_query_id, get_last_dividend_date
from .report_parser import parse_cash_transaction
import logging

def fetch_dividends_from_ib(token, config):
    """
    Fetch dividend information from Interactive Brokers using a Flex Query.

    :param token: Authentication token for IB API.
    :param config: Configuration dict containing settings like retry attempts, etc.
    :return: A list of dictionaries with dividend data.
    """
    query = get_query_id(get_last_dividend_date(), config['flex_queries'])
    reference_code = initiate_flex_query_report(query, token)
    report_data = download_flex_query_report(reference_code, token, config['retry_attempts'], config['retry_wait'])
    if report_data is None:
        logging.error("No report data returned from fetch_dividends_from_ib.")
        return []
    transactions_tuples = parse_cash_transaction(report_data)

    # Assuming transactions_tuples is a list of tuples like (symbol, amount, ex_date, pay_date)
    transactions_dicts = []
    for transaction in transactions_tuples:
        transaction_dict = {
            'symbol': transaction[0],  # Adjust these indexes based on the actual structure of your tuples
            'amount': transaction[1],
            'ex_date': transaction[2],
            'pay_date': transaction[3]
        }
        transactions_dicts.append(transaction_dict)

    logging.debug("Fetched transactions: %s", transactions_dicts)
    return transactions_dicts