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
        print(self.person.first_name)
        print(self.person.last_name)
        print(self.person.user_name)
        print(self.person.password)
        body = ""
        response = self.make_request(url, body)

    def make_request(self, url, body):
        response = requests.get(url)
        if response.status_code != 200:
            print("\nRequest was invalid: \n"
                  "status code: " + str(response.status_code) + "\n"
                  "url: " + url + "\n"
                  "response: " + response.text + "\n"
                  )
            quit()
        return response
