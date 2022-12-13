import random
import time

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

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

    def set_sessions(self):
        pass

    def check_sessions(self):
        pass
