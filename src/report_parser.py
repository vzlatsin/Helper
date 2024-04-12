import xml.etree.ElementTree as ET
import logging

def parse_cash_transaction(cash_transaction_xml):
    # Parse the XML string into an Element
    root = ET.fromstring(cash_transaction_xml)
   
    # Extract details from each CashTransaction element
    transactions = []
    i = 0
    for transaction in root.findall('.//CashTransaction'):
        i += 1
        #logging.info(f"Processing record: {i}")
        symbol = transaction.attrib['symbol']
        amount = transaction.attrib['amount']
        dateTime = transaction.attrib['dateTime']
        reportDate = transaction.attrib['reportDate']
       
        transaction_data = (symbol, float(amount), dateTime.split(';')[0], reportDate)
        transactions.append(transaction_data)
   
    return transactions

def safe_float_conversion(value, default=0.0):
    """
    Safely converts a string to a float. Returns a default value if the conversion fails.
    :param value: The string to convert to float.
    :param default: The default value to return if conversion fails.
    :return: The converted float value or a default value.
    """
    try:
        return float(value) if value else default
    except ValueError:
        return default
    
def parse_trade_transaction(trade_transaction_xml):
    """
    Parse the XML string containing trade transactions.

    :param trade_transaction_xml: XML string with trade transaction data.
    :return: A list of dictionaries, each representing a trade, including detailed fields.
    """
    logging.info(f"XML to be processed: {trade_transaction_xml}")
    # Parse the XML string into an Element
    root = ET.fromstring(trade_transaction_xml)

    # Initialize a list to hold parsed trade transactions
    trades = []

    # Process both Trade and SymbolSummary elements
    for trade in root.findall('.//Trades/*'):
        try:
            # Extracting each field from the trade transaction element
            trade_info = {
                'symbol': trade.attrib.get('symbol', ''),
                'dateTime': trade.attrib.get('dateTime', ''),
                'putCall': trade.attrib.get('putCall', ''),
                'transactionType': trade.attrib.get('transactionType', ''),
                'quantity': safe_float_conversion(trade.attrib.get('quantity')),
                'tradePrice': safe_float_conversion(trade.attrib.get('tradePrice')),
                'closePrice': safe_float_conversion(trade.attrib.get('closePrice')),
                'cost': safe_float_conversion(trade.attrib.get('cost')),
                'origTradePrice': safe_float_conversion(trade.attrib.get('origTradePrice')),
                'origTradeDate': trade.attrib.get('origTradeDate', ''),
                'buySell': trade.attrib.get('buySell', ''),
                'orderTime': trade.attrib.get('orderTime', ''),
                'openDateTime': trade.attrib.get('openDateTime', ''),
                'assetCategory': trade.attrib.get('assetCategory', ''),
                'strike': safe_float_conversion(trade.attrib.get('strike')),
                'expiry': trade.attrib.get('expiry', ''),
                'tradeDate': trade.attrib.get('tradeDate', ''),
            }

            # If the trade is for NEM stock (or starts with "NEM"), log its details
            if trade_info['symbol'].strip().upper().startswith('NEM'):
                logging.info(f"NEM trade found: {trade_info}")

            trades.append(trade_info)
        except Exception as e:
            logging.error(f"Error processing trade transaction: {e}")
            # Optionally, continue to the next trade or handle the error as needed
            continue

    return trades



# Example usage (assuming report_data contains your XML data string)
"""report_data = <FlexQueryResponse queryName="Dividends last year" type="AF">
<CashTransactions>
<CashTransaction currency="AUD" symbol="RFF" description="RFF (AU000000RFF5) CASH DIVIDEND AUD 0.029325 (Mixed Income)" dateTime="20230801;102000" amount="46.92" type="Dividends" reportDate="20230731" />
...
</CashTransactions>
</FlexQueryResponse>

transactions = parse_cash_transaction(report_data)
for t in transactions:
    logging.info(f"Parsed transaction: {t}")
"""