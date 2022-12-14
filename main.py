
from consolemenu import *
from consolemenu.items import *

from person import Person

person = Person()
menu = ConsoleMenu("Welcome to AccountGen", "Version 1.0")
function_item1 = FunctionItem("Generate Fake Person", person.gen_fake_person)
function_item2 = FunctionItem("Show All", person.show_all_gmail_database)
function_item3 = FunctionItem(
    "Show all latest Inbox", person.show_all_latest_inbox_gmail_database)

selection_menu_gmail = SelectionMenu("", "Gmail")
selection_menu_gmail.append_item(function_item2)
selection_menu_gmail.append_item(function_item3)

submenu_item_gmail = SubmenuItem("Gmail", selection_menu_gmail, menu)


menu.append_item(function_item1)
menu.append_item(submenu_item_gmail)
menu.show()
