import requests

from person import Person


class Gmail:
    # Class attribute
    person: Person

    # Constructor
    def __init__(self, person):
        self.person = person

    def create_account(self):
        url = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
        result = self.make_request(url)

    def make_request(self, url):
        print(self.person.first_name)
        print(self.person.last_name)
        print(self.person.user_name)
        print(self.person.password)
        response = requests.get(url)
        if response.status_code != 200:
            print("Request was invalid: " + url + "\n")
