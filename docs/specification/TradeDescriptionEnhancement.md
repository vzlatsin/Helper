
# Specification for Generating Simplified Trade Descriptions

## Objective

To enhance the web application's functionality by automatically transforming detailed trade entries, including potential duplicates or closely related transactions, into simplified, coherent descriptions for end users.

## Input Data

Trade data is presented in lines, each with key attributes like `symbol`, `dateTime`, `putCall`, `transactionType`, `quantity`, `tradePrice`, `tradeDate`, and `assetCategory`. The data may contain duplicate or related entries for a single transaction, identified primarily by matching `symbol`, `tradeDate`, and transaction details.

## Processing Strategy

### Identification of Related Entries

- **Duplicate Detection**: Identify duplicate or closely related entries by comparing `symbol`, `tradeDate`, and specific transaction details. Prioritize entries marked as `ExchTrade` for final transaction details, considering others as preliminary or placeholder data.

### Simplification Process

1. **Aggregate Data**: For each set of related entries, aggregate necessary details to form a complete picture of the transaction.
2. **Template Selection**: Based on the `transactionType`, `putCall`, and `assetCategory`, select an appropriate template for generating the description.
3. **Data Insertion**: Fill in the selected template with details from the aggregated data to generate a coherent description.

## Description Templates

- **Option Transactions**:
  - "Sold a [putCall] option on [symbol] with a strike price of $[strike], expiring on [expiry], for a premium of $[tradePrice]. The transaction was completed on [tradeDate]."

- **Stock Transactions**:
  - For purchases: "Bought [quantity] shares of [symbol] at $[tradePrice] each, on [tradeDate]."
  - For sales: "Sold [quantity] shares of [symbol] at $[tradePrice] each, on [tradeDate]."

## Implementation Notes

- **Data Parsing**: Implement a parser to extract and analyze data from each line, identifying key attributes for processing.
- **Logic for Handling Duplicates**: Develop logic to detect and correctly handle duplicate or closely related entries, ensuring accurate representation of transactions.
- **Dynamic Description Generation**: Utilize templates to dynamically generate descriptions based on the transaction details, ensuring flexibility and scalability of the solution.

## Testing and Validation

- **Sample Data Testing**: Test the feature using a diverse set of real trade data to ensure accurate detection of duplicates and correct description generation.
- **User Feedback**: Obtain feedback from a sample user group to validate the clarity and usefulness of the generated descriptions.

## Expected Outcome

The implementation of this specification will result in the generation of simplified, easily understandable trade descriptions from detailed and potentially complex trade data, enhancing user experience by providing clear insights into trading activities.

