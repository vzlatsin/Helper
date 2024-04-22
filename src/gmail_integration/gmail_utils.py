from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request  # Import Request properly
import pickle
import os

def get_gmail_service():
    """Authenticate the user and return a service object to interact with Gmail."""
    creds = None
    token_path = 'credentials/token.pickle'
    scopes = ['https://www.googleapis.com/auth/gmail.readonly']
    client_secret_file = 'credentials/client_secret.json'

    # Load credentials from file if they exist
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    # If credentials are not valid, obtain new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service
