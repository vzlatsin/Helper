from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.connection import Connection
import logging
import time

class MyTradingApp(EWrapper, EClient):
    def __init__(self):
        logging.info("Starting app")
        EClient.__init__(self, self)

    def connect_to_tws(self):
        try:
            logging.info("Connection to TWS")
            self.connect("127.0.0.1", 7496, 0)

        except Exception as e:
            logging.error(" Error connecting to TWS: %s", e)

        # Add logic to handle connection (e.g., start a separate thread to run the message loop)

    # Implement necessary methods from EWrapper
    # ...

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('ibapi')
    logger.setLevel(logging.WARNING)
    app = MyTradingApp()
    app.connect_to_tws()

    time.sleep(10)
    logging.info("Disconnect!")
    app.disconnect()

if __name__ == "__main__":
    main()


