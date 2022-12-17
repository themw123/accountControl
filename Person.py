import random
import string

from faker import Faker


class Person:

    fake: Faker
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

    def gen_fake_person(self):
        self.create_names()
        self.print_person()

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
        print("\n")
