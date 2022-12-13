
from mongodb import Mongodb
from person import Person


def save_person_in_database():
    number_database = input("Save to Database? [y/n]: ")
    if number_database == "y":
        data = {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "user_name": person.user_name + "@gmail.com",
            "password": person.password,
        }
        mongodb.set_collection("gmail")
        mongodb.insert(data)
        print("saved.")
        print("\n")
    elif number_database == "n":
        print("not saved to database")
        print("\n")
    return number_database


print("\nWelcome to AccountGen 1.0\n")
mongodb = Mongodb()
person = Person()

options = "[1]: generate fake person \n[2]: comming soon \n[3]: exit"
while True:
    print("What do you want to do?")
    user_input = input(options + "\n" + "choose: ")

    if not user_input.isdigit():
        print("!!!Please enter a number!!!")
        print("\n")
        continue

    number = int(user_input)

    if number not in range(1, 4):
        print("!!!no option found!!!")
        print("\n")
        continue

    if number == 3:
        break

    if number == 1:
        person.create_names()
        person.print_person()
        print("\n")
        number_database = ""
        while not number_database or (number_database not in ["y", "n"]):
            number_database = save_person_in_database()
    if number == 2:
        print("comming soon")
        print("\n")
