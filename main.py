
from gmail import Gmail
from person import Person
from request import Request


def choose_gen():
    options = "[1]: create Gmail account\n[2]: comming soon"
    print("What do you want to do?")
    while True:
        user_input = input(options + "\n" + "choose: ")

        if not user_input.isdigit():
            print("!!!Please enter a number!!!\n")
            continue

        number = int(user_input)

        if number == 1:
            print("create Gmail account ...")
            break
        elif number == 2:
            print("comming soon ...")
            break
        else:
            print("!!!no option found!!!")
        print("\n")
    return number


print("\nWelcome to AccountGen 1.0\n")
""" number = choose_gen()
if number == 1:
    gmail = Gmail()
    gmail.create_account() """
request = Request()
person = Person()
gmail = Gmail(request, person)
gmail.create_account()
