import json
import socket
import logging

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)
    
def connect_to_tws_simulator(host, port):
    """ Connect to the TWS simulator and perform basic interaction. """
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            logging.info(f"Connecting to TWS simulator at {host}:{port}")
            s.connect((host, port))
           
            # Send some data (as an example)
            message = "Hello TWS Simulator"
            s.sendall(message.encode())

            # Receive response from the server
            response = s.recv(1024)
            logging.info(f"Received: {response.decode()}")

    except Exception as e:
        logging.error(f"Error connecting to TWS simulator: {e}")

def main():
    logging.basicConfig(level=logging.INFO)
    config = load_config('config.json')
    HOST = config['server_ip']           # The server's hostname or IP address
    PORT = config['server_port']         # The port used by the server

    connect_to_tws_simulator(HOST, PORT)

if __name__ == "__main__":
    main()