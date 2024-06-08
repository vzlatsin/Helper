

# Trades Extraction and Processing Specification

## Objective
Integrate functionality to extract and process trade data from Interactive Brokers (IB) using Flex Query ID 963193. This feature provides users with real-time access to their trade confirmations, enhancing investment decision-making.

## Workflow
1. **Data Extraction**: Fetch trade data using the Flex Query API.
2. **Data Processing**: Parse, validate, and process the fetched data.
3. **Database Integration**: Store trade data efficiently, preventing duplicates.
4. **Real-Time Updates**: Update the user interface in real-time using Flask-SocketIO.

## Integration Points
- **Flex Query Module (`flex_query`)**: Manages fetching trade data.
- **Data Access Module (`data-access`)**: Handles database operations.
- **Async Application Module (`app_async`)**: Manages the asynchronous core for real-time updates.

## Development Steps

### Data Handling
- Extend `flex_query.py` to include functions for initiating trade data queries and parsing responses.
- Update `data_access.py` to handle trade data storage and retrieval.

### Database Schema Extension

#### Trades Table
A new table named `trades` will be created in the database to store detailed information about each trade, including symbol, transaction type, trade ID, order and trade dates, buy/sell indicator, quantity, price, amount, commission, net cash, and tax.

### User Interface Integration

#### Fetching Financial Data Form
Modify the existing `fetch_financial_data_async.html` template to include a "Trades" option for data type selection. This facilitates user-initiated trade data extraction through a familiar interface.

### Real-Time Data Presentation
Utilize Flask-SocketIO for live updates of trade data processing, ensuring users receive immediate feedback within the web application.

## Testing and Validation
- Conduct unit tests for new functions in `flex_query` and `data_access`.
- Implement integration tests to verify the end-to-end data handling workflow.
- Validate the real-time update functionality with simulated trade data.

## Deployment Considerations
- Ensure the new database schema changes are applied smoothly during deployment.
- Maintain backward compatibility for uninterrupted user experience.

## Documentation
- Update documentation to include descriptions and usage guidelines for the new trade data functionality.

## Future Enhancements
- Consider advanced data analytics features for trade data.
- Explore additional financial data integration to broaden the application's capabilities.

## Fields Extracted from Interactive Brokers Report

The following fields will be extracted from the Interactive Brokers (IB) Flex Query report to be stored and processed in the database:

- **Symbol**: The ticker symbol of the traded asset.
- **DateTime**: The date and time of the trade.
- **PutCall**: Indicates if the asset is a put or call option. Relevant for options trading.
- **TransactionType**: Type of transaction (e.g., buy, sell).
- **Quantity**: The amount of the asset traded.
- **TradePrice**: The price at which the trade occurred.
- **ClosePrice**: The closing price of the asset on the trade date.
- **Cost**: The total cost associated with the trade.
- **OrigTradePrice**: The original trade price, relevant for trade modifications.
- **OrigTradeDate**: The original trade date, relevant for trade modifications.
- **BuySell**: Indicates whether the trade was a buy or sell order.
- **OrderTime**: The time the order was placed, in HH:MM:SS format.
- **OpenDateTime**: The date and time the position was opened.
- **AssetCategory**: The category of the asset (e.g., stock, option, futures).
- **Strike**: The strike price for options.
- **Expiry**: The expiry date for options.
- **TradeDate**: The date the trade took place.

This list represents the core data to be processed and integrated into the database for further analysis and decision-making support.


