# src/ib_data_fetcher.py

from .flex_query import initiate_flex_query_report, download_flex_query_report, get_last_dividend_date, get_dividend_query_id, get_trade_query_id
from .report_parser import parse_cash_transaction, parse_trade_transaction
import logging

from flask_socketio import SocketIO, emit
import eventlet


def fetch_dividends_from_ib(token, config):
    """
    Fetch dividend information from Interactive Brokers using a Flex Query.

    :param token: Authentication token for IB API.
    :param config: Configuration dict containing settings like retry attempts, etc.
    :return: A list of dictionaries with dividend data.
    """
    query = get_dividend_query_id(get_last_dividend_date(), config['flex_queries'])
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

import logging
from .flex_query import initiate_flex_query_report, download_flex_query_report, get_trade_query_id
from .report_parser import parse_trade_transaction

def fetch_trades_from_ib(token, config):
    """
    Fetch trade information from Interactive Brokers using a Flex Query.

    :param token: Authentication token for IB API.
    :param config: Configuration dictionary containing settings like retry attempts, etc.
    :return: A list of dictionaries with detailed trade data.
    """
    query_id = get_trade_query_id(config['flex_queries'])
    if not query_id:
        logging.error("Trade Flex Query ID is not defined in the configuration.")
        return []
    
    reference_code = initiate_flex_query_report(query_id, token)
    report_data = download_flex_query_report(reference_code, token, config['retry_attempts'], config['retry_wait'])
    if not report_data:
        logging.error("No report data returned from Interactive Brokers.")
        return []
    
    trades = parse_trade_transaction(report_data)
    if not trades:
        logging.error("Failed to parse trade data from the report.")
        return []
    
    trade_dicts = []
    for trade in trades:
        trade_dict = {
            'symbol': trade.get('symbol'),
            'dateTime': trade.get('dateTime'),
            'putCall': trade.get('putCall'),
            'transactionType': trade.get('transactionType'),
            'quantity': trade.get('quantity'),
            'tradePrice': trade.get('tradePrice'),
            'closePrice': trade.get('closePrice'),
            'cost': trade.get('cost'),
            'origTradePrice': trade.get('origTradePrice'),
            'origTradeDate': trade.get('origTradeDate'),
            'buySell': trade.get('buySell'),
            'orderTime': trade.get('orderTime'),
            'openDateTime': trade.get('openDateTime'),
            'assetCategory': trade.get('assetCategory'),
            'strike': trade.get('strike'),
            'expiry': trade.get('expiry'),
            'tradeDate': trade.get('tradeDate'),
            # Add any additional fields you've defined
        }
        trade_dicts.append(trade_dict)
    
    #logging.debug("Fetched and processed trades: %s", trade_dicts)
    return trade_dicts
