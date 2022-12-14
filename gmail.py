
from __future__ import print_function

import base64
import os.path
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Gmail:
    # Class attribute

    # Constructor

    def print_inbox(self):
        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                token = input("enter token.json as string: ")
                self.person.save_token_gmail_database(token)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=creds)
            response = service.users().messages().list(
                userId="me", labelIds=["INBOX"], maxResults=1).execute()
            message = response.get("messages")[0]
            # Print the subject and body of the email
            message_details = service.users().messages().get(
                userId="me", id=message["id"]).execute()
            # print(self.person["user_name"])
            print("Subject:", message_details["snippet"])
            print("\n")
        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')
