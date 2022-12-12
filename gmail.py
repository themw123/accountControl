from person import Person
from request import Request


class Gmail:
    # Class attribute
    person: Person
    request: Request

    # Constructor
    def __init__(self, request, person):
        self.request = request
        self.person = person

    def create_account(self):
        url = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"
        headers = {
            'User-Agent': self.request.create_user_agent(),
            'From': 'youremail@domain.example'
        }
        print(self.person.first_name)
        print(self.person.last_name)
        print(self.person.user_name)
        print(self.person.password)
        body = ""
        response = self.request.make_request(url, headers, body)
