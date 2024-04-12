# trade_processing.py

def filter_and_organize_trades(trades):
    """Organize trades into groups with related trades and a single ExchTrade entry."""
    grouped_trades = {}
    for trade in trades:
        key = (trade['symbol'], trade['tradeDate'])
        if key not in grouped_trades:
            grouped_trades[key] = {'related': [], 'exchTrade': None}
        if trade.get('transactionType') == 'ExchTrade':
            grouped_trades[key]['exchTrade'] = trade
        else:
            grouped_trades[key]['related'].append(trade)
    return grouped_trades

def generate_description_for_trade(trade):
    """Generate a description for a trade based on its details, specifically for ExchTrade entries."""
    option_type = "put" if trade['putCall'] == 'P' else "call"
    action = "Sold" if trade['quantity'] < 0 else "Bought"
    expiry_formatted = f"{trade['expiry'][:4]}-{trade['expiry'][4:6]}-{trade['expiry'][6:]}"
    
    if trade['putCall'] in ['P', 'C']:  # Option transaction
        description = f"{action} a {option_type} option on {trade['symbol']} with a strike price of ${trade['strike']}, expiring on {expiry_formatted}, for a premium of ${trade['tradePrice']}."
    else:  # Assuming stock transaction for simplicity
        description = f"{action} {abs(trade['quantity'])} shares of {trade['symbol']} at ${trade['tradePrice']} each."
    
    return description
