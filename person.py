import random
import string

from faker import Faker


class Person:

    fake: Faker
    first_name: str
    last_name: str
    user_name: str
    password = "***REMOVED***"

    def __init__(self):
        self.fake = Faker()
        self.create_names()

    def create_names(self):
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.user_name = self.fake.user_name()
        letter = random.choice(string.ascii_letters)
        number = random.randint(0, 10)
        self.user_name = self.user_name + letter + str(number)

        print("Person: ")
        print(self.first_name)
        print(self.last_name)
        print(self.user_name)
        print(self.password)
        print("\n")
