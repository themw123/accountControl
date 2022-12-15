

from consolemenu import *
from consolemenu.items import *

from gmail import Gmail
from mongodb import Mongodb
from person import Person

mongodb = Mongodb()
person = Person(mongodb)
gmail = Gmail(person, mongodb)


menu = ConsoleMenu("Welcome to AccountGen", "Version 1.0")
function_item1 = FunctionItem("Generate Fake Person", person.gen_fake_person)
function_item2 = FunctionItem("Show Accounts", gmail.show_all_database)
function_item3 = FunctionItem(
    "Show all latest Inbox", gmail.show_all_latest_inbox_database)
function_item4 = FunctionItem(
    "Send Mail with Account", gmail.send_mail_with_account)


selection_menu_gmail = SelectionMenu("", "Gmail")
selection_menu_gmail.append_item(function_item2)
selection_menu_gmail.append_item(function_item3)
selection_menu_gmail.append_item(function_item4)


submenu_item_gmail = SubmenuItem("Gmail", selection_menu_gmail, menu)


menu.append_item(function_item1)
menu.append_item(submenu_item_gmail)
menu.show()
