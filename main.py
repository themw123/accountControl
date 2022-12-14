
import time

from consolemenu import *
from consolemenu.items import *

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
        time.sleep(2)
    elif number_database == "n":
        print("not saved.")
    return number_database


def gen_fake_person():
    person.create_names()
    person.print_person()
    print("\n")
    number_database = ""
    while not number_database or (number_database not in ["y", "n"]):
        number_database = save_person_in_database()


mongodb = Mongodb()
person = Person()

menu = ConsoleMenu("Welcome to AccountGen", "Version 1.0")
function_item = FunctionItem(
    "Generate Fake Person", gen_fake_person)
selection_menu = SelectionMenu(["Show all", "item2", "item3"])
submenu_item = SubmenuItem("Accounts", selection_menu, menu)

menu.append_item(function_item)
menu.append_item(submenu_item)
menu.show()
