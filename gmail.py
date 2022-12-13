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
        # with selenium
        pass

    def create_account_not_working(self):
        # with request not working
        url = "https://accounts.google.com/signin/v2/challenge/password/empty"
        headers = {
            'User-Agent': self.request.create_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'firsName': self.person.first_name,
            'lastName': self.person.last_name,
            'Username': self.person.user_name,
            'Passwd': self.person.password,
            'ConfirmPasswd': self.person.password
        }
        response = self.request.make_request(url, headers, body)
