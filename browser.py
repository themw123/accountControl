# -*- coding: utf-8 -*-
# @Author: Chao
# @Date:   2018-08-23 22:57:28
# @Last Modified by:   Chao
# @Last Modified time: 2018-11-02 10:04:50

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd
import random
import time
import sys


class CreateGmail:
    """Auto Create Gmail Accounts with popular names"""

    def __init__(self, firstname, lastname, username, pswd):
        self._firstname = firstname
        self._lastname = lastname
        self._username = username
        self._pswd = pswd
        self._Donefile = open("./data/CreatedAccounts.csv", "a")
        self.Initialize()

    def Initialize(self):
        self._browser = webdriver.Chrome()
        self._browser.delete_all_cookies()
        self._browser.get("https://accounts.google.com/SignUp?hl=en")

    def SetRecoveryEmail(self):
        self.recovery_email = "lol.loli1517@web.de"

    def CreateAccount(self):
        # self.SetRecoveryEmail()
        self._browser.find_element_by_css_selector(r'input[id="firstName"]').send_keys(
            self._firstname
        )
        time.sleep(1)
        self._browser.find_element_by_css_selector(r'input[id="lastName"]').send_keys(
            self._lastname
        )
        time.sleep(1)
        self._browser.find_element_by_css_selector(r'input[id="username"]').send_keys(
            self._username
        )
        time.sleep(1)
        self._browser.find_element_by_css_selector(
            r'input[name="Passwd"]').send_keys(self._pswd)
        time.sleep(1 + 3 * random.random())
        self._browser.find_element_by_css_selector(r'input[name="ConfirmPasswd"]').send_keys(
            self._pswd
        )
        self._browser.find_element_by_css_selector(
            r'div[id="accountDetailsNext"]').click()
        self._browser.implicitly_wait(10)

        try:
            self._browser.find_element_by_css_selector(
                "#month > option:nth-child(%d)" % random.randint(1, 13)
            ).click()
        except:
            self._browser.quit()
            # raise ValueError("IP Mac Limited. Stop the Script...")
            # sys.exit(0)
            sys.exit("IP Mac Limited. Stop the Script...")
        else:
            time.sleep(1 + 3 * random.random())
            # self._browser.find_element_by_css_selector(r'div.fQxwff:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(self.recovery_email)
            # time.sleep(1)
            self._browser.find_element_by_css_selector(r'input[id="day"]').send_keys(
                random.randint(1, 28)
            )
            time.sleep(1)
            self._browser.find_element_by_css_selector(r'input[id="year"]').send_keys(
                random.randint(1990, 2000)
            )
            time.sleep(1)
            try:
                self._browser.find_element_by_css_selector("#gender").click()
            except:
                print(
                    "Cannot locate Gender Blockm Please manually click it. Sleep 1 min...")
                time.sleep(60)
                pass
            try:
                time.sleep(0.5)
                try:
                    self._browser.find_element_by_css_selector(
                        "#gender > option:nth-child(%d)" % random.randint(1, 4)
                    ).click()
                except:
                    self._browser.quit()
                    sys.exit(1)
                    self._browser.find_elements_by_xpath("").click()
            except:
                time.sleep(0.5)
                self._browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[4]/div[1]/div/div[2]/select/option[%d]"
                    % random.randint(1, 4)
                ).click()
            time.sleep(1 + 3 * random.random())
            self._browser.find_element_by_css_selector(
                r'div[id="personalDetailsNext"]').click()
            self._browser.implicitly_wait(10)
            time.sleep(1)
            while True:
                try:
                    self._browser.find_element_by_css_selector(
                        ".mUbCce").click()
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    break
            self._browser.find_element_by_css_selector(
                "#termsofserviceNext").click()
            self._browser.implicitly_wait(10)

            self._Donefile.write(self._username + "," + self._pswd + "\n")
            print(self._username + ": Success")
            self._browser.quit()
