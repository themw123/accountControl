import os.path
import random
import string
import time

from faker import Faker
from google_auth_oauthlib.flow import InstalledAppFlow

from mongodb import Mongodb


class Person:

    fake: Faker
    mongodb: Mongodb
    first_name: str
    last_name: str
    user_name: str
    password = "***REMOVED***"

    token: str

    day: int
    month: int
    year: int
    gender: str

    def __init__(self, mongodb):
        self.fake = Faker()
        self.mongodb = mongodb

    def gen_fake_person(self):
        self.create_names()
        self.print_person()
        print("\n")
        self.save_person_database()

    def set_token(self):
        SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        self.token = creds.to_json()

    def save_person_database(self):
        input("Enter to generate token")
        self.set_token()
        number_database = ""
        while not number_database or (number_database not in ["y", "n"]):
            number_database = input("Save to Database? [y/n]: ")
        if number_database == "y":
            data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "user_name": self.user_name + "@gmail.com",
                "password": self.password,
                "token": self.token,
            }
            self.mongodb.set_collection("gmail")
            self.mongodb.insert(data)
            print("saved.")
            time.sleep(2)
        elif number_database == "n":
            print("not saved.")
        return number_database

    def get_token_from_person_database(self, user_name):
        self.mongodb.set_collection("gmail")
        query = {"user_name": user_name}
        try:
            result = self.mongodb.find_one(query)
            token = result["token"]
            return token
        except:
            print("")
            print("Error: Token from Email not found")
            return None

    def create_names(self):
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.user_name = self.fake.user_name()
        letter1 = random.choice(string.ascii_letters)
        number1 = random.randint(0, 10)
        letter2 = random.choice(string.ascii_letters)
        number2 = random.randint(0, 10)
        self.user_name = letter1 + \
            str(number1) + self.user_name + letter2 + str(number2)

        self.day = random.randint(1, 28)
        self.month = random.randint(1, 12)
        self.year = random.randint(1990, 2000)
        genders = ["male", "female"]
        r = random.randint(0, 1)
        self.gender = genders[r]

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
