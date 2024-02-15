from src.data_fetcher import DataFetcher

class MockDataFetcher(DataFetcher):
    def fetch(self):
        # Return a fixed response suitable for testing
        return{"key", "mocked value"}