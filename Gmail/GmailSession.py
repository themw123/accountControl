import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from Helper.Mongodb import Mongodb


class GmailSession():
    mongodb: Mongodb
    creds: Credentials

    def __init__(self, mongodb):
        self.mongodb = mongodb

    def create_creds(self):
        SCOPES = ['https://mail.google.com/']
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        self.creds = flow.run_local_server(port=0)
        creds = self.creds.to_json()
        self.creds = json.loads(creds)

    def set_creds(self, creds, user_name):
        self.creds = Credentials.from_authorized_user_info(creds)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
                self.update_creds_gmail_database(user_name)

    def update_creds_gmail_database(self, user_name):
        creds = self.creds.to_json()
        creds = json.loads(creds)
        self.mongodb.set_collection("gmail")
        query = {"user_name": user_name}
        update = {"$set": {"creds": creds}}
        self.mongodb.update(query, update)
        # print("\ncreds updatetd\n")

    # not in use because in Gmail it is more cleverer to use get_all_gmail_database()
    def get_creds_gmail_database(self, user_name):
        self.mongodb.set_collection("gmail")
        query = {"user_name": user_name}
        cursor = self.mongodb.find(query)
        for person in cursor:
            if person["user_name"] == user_name:
                creds = person["creds"]
                return creds
        return None
