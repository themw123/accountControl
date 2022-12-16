import json
import time

from google_auth_oauthlib.flow import InstalledAppFlow

from Mongodb import Mongodb
from Person import Person


class GmailDatabase():

    mongodb: Mongodb
    person: Person
    cred: json

    def __init__(self, mongodb):
        self.mongodb = mongodb
        self.person = Person()

    def gen_fake_person(self):
        self.person.gen_fake_person()
        self.save_person_gmail_database()

    def save_person_gmail_database(self):
        self.mongodb.set_collection("gmail")
        print("If you have created your Gmail Account, please add this accound to your Google Console Project(The one from credentials.json)")
        input("press enter to generate creds\n")
        self.create_creds()
        number_database = ""
        while not number_database or (number_database not in ["y", "n"]):
            number_database = input("\nSave to Database? [y/n]: \n")
        if number_database == "y":
            data = {
                "first_name": self.person.first_name,
                "last_name": self.person.last_name,
                "user_name": self.person.user_name + "@gmail.com",
                "password": self.person.password,
                "creds": self.creds,
            }
            self.mongodb.insert(data)
            print("saved.")
            time.sleep(2)
        elif number_database == "n":
            print("not saved.")
        return number_database

    def update_creds_gmail_database(self, user_name, newcreds):
        self.mongodb.set_collection("gmail")
        query = {"user_name": user_name}
        update = {"$set": {"creds": newcreds}}
        self.mongodb.update(query, update)
        #print("\ncreds updatetd\n")

    def get_token_from_person_gmail_database(self, user_name):
        self.mongodb.set_collection("gmail")
        query = {"user_name": user_name}
        try:
            result = self.mongodb.find_one(query)
            creds = result["creds"]
            return creds
        except:
            print("Error: Creds from Email not found")
            return None

    def get_all_gmail_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        return cursor

    ###########helper#################

    def create_creds(self):
        SCOPES = ['https://mail.google.com/']
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        creds = creds.to_json()
        self.creds = json.loads(creds)
