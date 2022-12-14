
from consolemenu import *
from consolemenu.items import *

from person import Person


def meine_funktion():
    print("Dies ist meine Funktion")


person = Person()
menu = ConsoleMenu("Welcome to AccountGen", "Version 1.0")
function_item1 = FunctionItem("Generate Fake Person", person.gen_fake_person)
function_item2 = FunctionItem("Show_all", person.show_all)

selection_menu = SelectionMenu("")
selection_menu.append_item(function_item2)
submenu_item = SubmenuItem("Accounts", selection_menu, menu)


menu.append_item(function_item1)
menu.append_item(submenu_item)
menu.show()
