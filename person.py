import names


class Person:

    first_name: str
    last_name: str
    user_name: str
    password = "ge3nEratePass!er43e3"

    def __init__(self):
        self.create_names()

    def create_names(self):
        self.first_name = names.get_first_name()
        self.last_name = names.get_last_name()
        self.user_name = self.first_name + self.last_name
