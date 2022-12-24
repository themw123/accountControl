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
        #print("\nIf you have created your Gmail Account, please add this accound to your Google Console Project(The one from credentials.json)\n")

        choose = ""
        while not choose or (choose not in ["y", "n"]):
            choose = input(
                "\nenter [y] to generate creds and [n] for cancel\n")
        if choose == "n":
            return choose
        self.gmailsession.create_creds()
        data = {
            "first_name": self.person.first_name,
            "last_name": self.person.last_name,
            "user_name": self.person.user_name + "@gmail.com",
            "password": self.person.password,
            "creds": self.gmailsession.creds,
        }
        self.mongodb.insert(data)
        print("Saved to database!\n")
        return choose

    def update_person_gmail_database(self, person):
        self.mongodb.set_collection("gmail")
        query = {
            "user_name": person['user_name'],
        }
        update = {"$set": {"creds": self.gmailsession.creds}}

        self.mongodb.update(query, update)
        print("updated!\n")

    def get_all_gmail_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        return cursor
