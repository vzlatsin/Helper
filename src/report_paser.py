import xml.etree.ElementTree as ET
import logging

def parse_cash_transaction(cash_transaction_xml):
    # Parse the XML string into an Element
    root = ET.fromstring(cash_transaction_xml)
   
    # Extract details from each CashTransaction element
    transactions = []
    for transaction in root.findall('.//CashTransaction'):
        symbol = transaction.attrib['symbol']
        amount = transaction.attrib['amount']
        dateTime = transaction.attrib['dateTime']
        reportDate = transaction.attrib['reportDate']
       
        transaction_data = (symbol, float(amount), dateTime.split(';')[0], reportDate)
        transactions.append(transaction_data)
   
    return transactions

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