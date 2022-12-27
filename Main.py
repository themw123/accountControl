

from consolemenu import *
from consolemenu.items import *

from Gmail.Gmail import Gmail
from Proton.Proton import Proton

gmail = Gmail()
proton = Proton()

menu = ConsoleMenu("Welcome to AccountControl", "Version 1.0")
function_item1 = FunctionItem(
    "Generate new Person", gmail.gen_new_person)
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


function_item8 = FunctionItem(
    "Generate new Account", proton.gen_new_account)
function_item9 = FunctionItem(
    "Show accounts", proton.show_all_database)
function_item10 = FunctionItem(
    "Show one latest inbox", proton.show_one_latest_inbox)
selection_menu_proton = SelectionMenu("", "Proton")
selection_menu_proton.append_item(function_item8)
selection_menu_proton.append_item(function_item9)
selection_menu_proton.append_item(function_item10)

submenu_item_proton = SubmenuItem("Proton", selection_menu_proton, menu)

menu.append_item(submenu_item_gmail)
menu.append_item(submenu_item_proton)

menu.show()
