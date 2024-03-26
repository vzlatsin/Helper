# Asynchronous Dividend Loading Specification

## Objective
To implement asynchronous fetching and processing of dividend information, ensuring efficient data handling and updating the database without duplicating entries.

## Workflow
1. **Data Fetching**: Leverage `aiohttp` in `flex_query.py` for async API calls.
2. **Data Processing**: Use async functions in `data_access.py` to interact with the database.
3. **Real-Time Updates**: Employ Flask-SocketIO in `app_async.py` for communication.

## Key Functions
- Async API request and response handling.
- Checking for existing database entries before inserting new data.
- Emitting real-time status updates to the client.

## Implementation Steps
1. Modify `flex_query.py` to support async operations.
2. Adapt `data_access.py` for async database interactions.
3. Update `app_async.py` to manage the async workflow and SocketIO events.

## Testing
- Unit tests for new async functions.
- Integration tests for the overall async data loading process.

## Deployment
- Update deployment scripts to include new async components.

