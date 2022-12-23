

from consolemenu import *
from consolemenu.items import *

from Gmail.Gmail import Gmail

gmail = Gmail()

menu = ConsoleMenu("Welcome to AccountControl", "Version 1.0")
function_item1 = FunctionItem(
    "Generate Fake Person", gmail.gen_fake_person)
function_item2 = FunctionItem("Show accounts", gmail.show_all_database)
function_item3 = FunctionItem(
    "Show all latest inbox", gmail.show_all_latest_inbox)
function_item4 = FunctionItem(
    "Show one latest inbox", gmail.show_one_latest_inbox)
function_item5 = FunctionItem(
    "Send all mail", gmail.send_all_mail)
function_item6 = FunctionItem(
    "Send one mail", gmail.send_one_mail)
function_item7 = FunctionItem(
    "Reset all credentials", gmail.reset_credentials_all)


selection_menu_gmail = SelectionMenu("", "Gmail")
selection_menu_gmail.append_item(function_item1)
selection_menu_gmail.append_item(function_item2)
selection_menu_gmail.append_item(function_item3)
selection_menu_gmail.append_item(function_item4)
selection_menu_gmail.append_item(function_item5)
selection_menu_gmail.append_item(function_item6)
selection_menu_gmail.append_item(function_item7)


submenu_item_gmail = SubmenuItem("Gmail", selection_menu_gmail, menu)

menu.append_item(submenu_item_gmail)
menu.show()
