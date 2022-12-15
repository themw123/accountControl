
from __future__ import print_function

import base64
import json
from email.message import EmailMessage

import google.auth
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
    cred: Credentials
    # Constructor

    def __init__(self, person, mongodb):
        self.person = person
        self.mongodb = mongodb

    def set_cred(self, token):
        # create google.oauth2.credentials.Credentials object with token
        self.creds = Credentials.from_authorized_user_info(json.loads(token))
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())

                # save new the token to the database
                """ !!!!!!!!!!!!!!!!!!!
                !!!!!!!!!!!!!!!!!!!
                !!!!!!!!!!!!!!!!!!!
                !!!!!!!!!!!!!!!!!!!
                !!!!!!!!!!!!!!!!!!! """

    def show_inbox(self, user_name, token):
        try:
            self.set_cred(token)
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=self.creds)
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
            self.show_inbox(person["user_name"], person["token"])
        input("\nEnter to continue...")

    def send_mail_with_account(self):
        fromUser = input("from: ")
        toUser = input("to: ")
        subject = input("subject: ")
        body = input("body: ")

        token = self.person.get_token_from_person_database(fromUser)
        if token is not None:
            self.send_mail(token, fromUser, toUser, subject, body)
        input("\nEnter to continue...")

    def send_mail(self, token, fromUser, toUser, subject, body):
        try:
            self.set_cred(token)

            # create gmail api client
            service = build('gmail', 'v1', credentials=self.creds)
            message = EmailMessage()
            message.set_content(body)

            message['From'] = fromUser
            message['To'] = toUser
            message['Subject'] = subject
            # encoded message
            encoded_message = base64.urlsafe_b64encode(
                message.as_bytes()).decode()

            create_message = {
                'message': {
                    'raw': encoded_message
                }
            }
            # pylint: disable=E1101
            draft = service.users().drafts().create(userId="me",
                                                    body=create_message).execute()

            print(
                F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

        except HttpError as error:
            print("\n")
            print(F'An error occurred: {error}')
            draft = None

        return draft

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
