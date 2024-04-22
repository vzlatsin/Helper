from gmail_utils import get_gmail_service
import datetime

def fetch_emails(service, query):
    """
    Fetch and print details of emails from Gmail based on a provided query.
    
    Parameters:
        service (Resource): Authenticated Gmail service object.
        query (str): Gmail search query to filter messages.
    """
    try:
        # Initialize the list to hold all messages
        response = service.users().messages().list(userId='me', q=query, maxResults=10).execute()
        messages = response.get('messages', [])
        print(f"Fetched {len(messages)} messages.")

        # Paginate through results if more than 10 emails match the query
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId='me', q=query, pageToken=page_token, maxResults=10).execute()
            messages.extend(response.get('messages', []))

        # Print details of each message
        for message in messages:
            msg_id = message['id']
            msg = service.users().messages().get(userId='me', id=msg_id).execute()
            print(f"Message ID: {msg_id} - Snippet: {msg['snippet']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    service = get_gmail_service()
    seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y/%m/%d')
    query = f'from:donotreply@interactivebrokers.com after:{seven_days_ago} subject:"Deposit Activity Update"'
    fetch_emails(service, query)
