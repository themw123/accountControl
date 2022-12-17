import time

from Gmail.GmailSession import GmailSession
from Helper.Mongodb import Mongodb
from Helper.Person import Person


class GmailDatabase():

    mongodb: Mongodb
    person: Person
    gmailsession: GmailSession

    def __init__(self, mongodb, person, gmailsession):
        self.mongodb = mongodb
        self.person = person
        self.gmailsession = gmailsession

    def save_person_gmail_database(self):
        self.mongodb.set_collection("gmail")
        print("If you have created your Gmail Account, please add this accound to your Google Console Project(The one from credentials.json)\n")

        choose1 = ""
        while not choose1 or (choose1 not in ["y", "n"]):
            choose1 = input("enter [y] to generate creds and [n] for cancel\n")
        if choose1 == "n":
            return
        self.gmailsession.create_creds()
        data = {
            "first_name": self.person.first_name,
            "last_name": self.person.last_name,
            "user_name": self.person.user_name + "@gmail.com",
            "password": self.person.password,
            "creds": self.gmailsession.creds,
        }
        self.mongodb.insert(data)
        input("\nSaved account to database. Press enter to go back.")

    def get_all_gmail_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        return cursor

    ###########helper#################
