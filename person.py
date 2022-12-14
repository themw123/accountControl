import json
import random
import string
import time

from faker import Faker

from gmail import Gmail
from mongodb import Mongodb


class Person:

    fake: Faker
    mongodb: Mongodb
    first_name: str
    last_name: str
    user_name: str
    password = "***REMOVED***"

    day: int
    month: int
    year: int
    gender: str

    def __init__(self):
        self.fake = Faker()
        self.mongodb = Mongodb()

    def gen_fake_person(self):
        self.create_names()
        self.print_person()
        print("\n")
        number_database = ""
        while not number_database or (number_database not in ["y", "n"]):
            number_database = self.save_person_gmail_database()

    def create_names(self):
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.user_name = self.fake.user_name()
        letter1 = random.choice(string.ascii_letters)
        number1 = random.randint(0, 10)
        letter2 = random.choice(string.ascii_letters)
        number2 = random.randint(0, 10)
        self.user_name = letter1 + str(number1) + \
            self.user_name + letter2 + str(number2)

        self.day = random.randint(1, 28)
        self.month = random.randint(1, 12)
        self.year = random.randint(1990, 2000)
        genders = ["male", "female"]
        r = random.randint(0, 1)
        self.gender = genders[r]

    def save_person_gmail_database(self):
        number_database = input("Save to Database? [y/n]: ")
        if number_database == "y":
            data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "user_name": self.user_name + "@gmail.com",
                "password": self.password,
            }
            self.mongodb.set_collection("gmail")
            self.mongodb.insert(data)
            print("saved.")
            time.sleep(2)
        elif number_database == "n":
            print("not saved.")
        return number_database

    def show_all_gmail_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        for person in cursor:
            print(json.dumps(person, default=str, indent=2) + "\n")
        input("\nEnter to continue...")

    def get_all_gmail_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        return cursor

    def show_all_latest_inbox_gmail_database(self):
        self.mongodb.set_collection("gmail")
        cursor = self.mongodb.find("")
        # create empty array
        for person in cursor:
            gmail = Gmail()
            gmail.print_inbox(person["user_name"])
        input("\nEnter to continue...")

    def save_token_gmail_database(self, token):
        self.mongodb.set_collection("gmail")
        self.mongodb.update({"user_name": self.user_name},
                            {"$set": {"token": token}})

    def print_person(self):
        print("\n")
        print(self.first_name)
        print(self.last_name)
        print(self.user_name)
        print(self.password)
        print("\n")
        print(self.day)
        print(self.month)
        print(self.year)
        print(self.gender)
