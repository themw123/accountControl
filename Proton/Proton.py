import imaplib
import json
import time

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By

from Helper.Mongodb import Mongodb
from Helper.Person import Person


class Proton:
    person: Person
    mongodb: Mongodb

    def __init__(self):
        self.person = Person()
        self.mongodb = Mongodb()

    def gen_new_account(self):
        #driver = uc.Chrome()
        # driver.get('https://proton.me/mail')
        self.person.gen_new_person()
        # self.send_mail_for_clipboard_handy()
        self.save_person_proton_database()
        input("\nEnter to continue...")

    ############HELPER############

    def save_person_proton_database(self):
        self.mongodb.set_collection("proton")

        choose = ""
        while not choose or (choose not in ["y", "n"]):
            choose = input(
                "\nsave to database? yes [y] or no [n]\n")
        if choose == "n":
            return

        data = {
            "user_name": self.person.user_name + "@proton.me",
            "password": self.person.password,
        }
        self.mongodb.insert(data)
        print("Saved to database!\n")

    def show_all_database(self):
        self.mongodb.set_collection("proton")
        cursor = self.mongodb.find("")
        for person in cursor:
            person.pop("_id")
            print(json.dumps(person, default=str, indent=2) + "\n")
        print("\n total: " + str(cursor.retrieved) + "\n")
        input("\nEnter to continue...")

    def show_one_latest_inbox(self):
        self.mongodb.set_collection("proton")
        user_name = input("Input Email: ")
        print()
        cursor = self.mongodb.find("")

        for person in cursor:
            if person["user_name"] == user_name:
                self.show_inbox(user_name, person["password"])
        input("\nEnter to continue...")

    def show_inbox(self, user_name, password):
        print('\n')
