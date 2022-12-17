
from __future__ import print_function

import base64
import json
from email.message import EmailMessage

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from Gmail.GmailDatabase import GmailDatabase
from Gmail.GmailSession import GmailSession
from Helper.Mongodb import Mongodb
from Helper.Person import Person


class Gmail:
    # Class attribute
    person: Person
    mongodb: Mongodb
    gmaildatabase: GmailDatabase
    gmailsession: GmailSession
    # Constructor

    def __init__(self):
        self.person = Person()
        self.mongodb = Mongodb()
        self.gmailsession = GmailSession(self.mongodb)
        self.gmaildatabase = GmailDatabase(
            self.mongodb, self.person, self.gmailsession)

    def gen_fake_person(self):
        self.person.gen_fake_person()
        self.gmaildatabase.save_person_gmail_database()

    def show_all_database(self):
        cursor = self.gmaildatabase.get_all_gmail_database()
        for person in cursor:
            token = person["creds"]["token"]
            person.pop("creds", None)
            person.pop("_id", None)
            person["token"] = token
            print(json.dumps(person, default=str, indent=2) + "\n")
        print("\n Insgesammt: " + str(cursor.retrieved) + "\n")
        input("\nEnter to continue...")

    def show_all_latest_inbox(self):
        cursor = self.gmaildatabase.get_all_gmail_database()
        for person in cursor:
            self.gmailsession.set_creds(person["creds"], person["user_name"])
            self.show_inbox(person["user_name"])
        input("\nEnter to continue...")

    def show_one_latest_inbox(self):
        user_name = input("Input Email: ")
        print()

        cursor = self.gmaildatabase.get_all_gmail_database()
        for person in cursor:
            if person["user_name"] == user_name:
                self.gmailsession.set_creds(
                    person["creds"], person["user_name"])
                self.show_inbox(user_name)
        input("\nEnter to continue...")

    def send_all_mail(self):
        cursor = self.gmaildatabase.get_all_gmail_database()
        toUser = input("to: ")
        subject = input("subject: ")
        body = input("body: ")
        print()
        for person in cursor:
            self.gmailsession.set_creds(person["creds"], person["user_name"])
            self.send_mail(person["user_name"], toUser, subject, body)

        input("\nEnter to continue...")

    def send_one_mail(self):
        fromUser = input("from: ")
        toUser = input("to: ")
        subject = input("subject: ")
        body = input("body: ")
        print("")

        cursor = self.gmaildatabase.get_all_gmail_database()
        for person in cursor:
            if person["user_name"] == fromUser:
                self.gmailsession.set_creds(
                    person["creds"], person["user_name"])
                self.send_mail(fromUser, toUser, subject, body)
        input("\nEnter to continue...")

    ###############helper###########################################################

    def show_inbox(self, user_name):
        try:
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=self.gmailsession.creds)
            response = service.users().messages().list(
                userId="me", labelIds=["INBOX"], maxResults=1).execute()
            try:
                message = response.get("messages")[0]
            except:
                pass

            # Print the subject and body of the email
            message_details = service.users().messages().get(
                userId="me", id=message["id"]).execute()
            print(user_name + ":")
            # Get value of 'payload' from dictionary 'txt'
            payload = message_details['payload']
            headers = payload['headers']

            # Look for Subject and Sender Email in the headers
            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']

            try:
                data = payload['body']['data']
                body = base64.urlsafe_b64decode(data)
                body = str(body)
                body = body.replace("b'", "").replace("\\r\\n'", "")
            except:
                body = message_details.get("snippet")

            print("\tSubject: ", subject)
            print("\tFrom: ", sender)
            print("\tMessage: ", body)
            print('\n')
        except HttpError as error:
            print(f'An error occurred: {error}')

    def send_mail(self, fromUser, toUser, subject, body):
        try:
            service = build('gmail', 'v1', credentials=self.gmailsession.creds)
            message = EmailMessage()

            message.set_content(body)

            message['To'] = toUser
            message['From'] = fromUser
            message['Subject'] = subject

            # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            create_message = {
                'raw': encoded_message
            }
            # pylint: disable=E1101
            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            # print(F'Message Id: {send_message["id"]}')
            print("Message sent!")
        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None
