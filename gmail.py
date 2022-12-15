
from __future__ import print_function

import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from mongodb import Mongodb
from person import Person


class Gmail:
    # Class attribute
    person: Person
    mongodb: Mongodb
    # Constructor

    def __init__(self, person, mongodb):
        self.person = person
        self.mongodb = mongodb

    def print_inbox(self, user_name, token):
        try:
            # create google.oauth2.credentials.Credentials object with token
            creds = Credentials.from_authorized_user_info(json.loads(token))
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                    # save new the token to the database
                    !!!!!!!!!!!!!!!!!!!
                    !!!!!!!!!!!!!!!!!!!
                    !!!!!!!!!!!!!!!!!!!
                    !!!!!!!!!!!!!!!!!!!
                    !!!!!!!!!!!!!!!!!!!
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=creds)
            response = service.users().messages().list(
                userId="me", labelIds=["INBOX"], maxResults=1).execute()
            message = response.get("messages")[0]
            # Print the subject and body of the email
            message_details = service.users().messages().get(
                userId="me", id=message["id"]).execute()
            print(user_name + ":")
            print("Subject:", message_details["snippet"])
            print("\n")
        except HttpError as error:
            print(f'An error occurred: {error}')

    def show_all_latest_inbox_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        # create empty array
        for person in cursor:
            self.print_inbox(person["user_name"], person["token"])
        input("\nEnter to continue...")

    def show_all_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        for person in cursor:
            print(json.dumps(person, default=str, indent=2) + "\n")
        input("\nEnter to continue...")

    def get_all_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        return cursor
