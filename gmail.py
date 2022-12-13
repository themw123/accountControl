from person import Person
from request import Request
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
import time

from selenium.webdriver.support.ui import WebDriverWait


class Gmail:
    # Class attribute
    person: Person
    request: Request

    # Constructor
    def __init__(self, request, person):
        self.request = request
        self.person = person

    def create_account(self):
        # with selenium
        recovery_email = "lol.loli1517@web.de"
        browser = webdriver.Chrome()
        browser.delete_all_cookies()
        browser.get("https://accounts.google.com/SignUp?hl=en")

        #!!!!!!!!!!!!!!!!!!first page!!!!!!!!!!!!!!!!!!
        browser.find_element(By.CSS_SELECTOR, 'input[id="firstName"]').send_keys(
            self.person.first_name
        )

        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[id="lastName"]').send_keys(
            self.person.last_name
        )
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[id="username"]').send_keys(
            self.person.user_name
        )
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'input[name="Passwd"]').send_keys(
            self.person.password)
        time.sleep(1 + 3 * random.random())
        browser.find_element(By.CSS_SELECTOR, 'input[name="ConfirmPasswd"]').send_keys(
            self.person.password
        )
        browser.find_element(
            By.CSS_SELECTOR, 'div[id="accountDetailsNext"]').click()
        browser.implicitly_wait(10)

        try:
            browser.find_element(By.CSS_SELECTOR,
                                 "#month > option:nth-child(%d)" % random.randint(
                                     1, 13)
                                 ).click()
        except:
            browser.quit()
            exit("\nIP Mac Limited. Stop the Script...")

        #!!!!!!!!!!!!!!!!!!second page!!!!!!!!!!!!!!!!!!
        else:
            time.sleep(1 + 3 * random.random())
            # browser.find_element_by_css_selector(r'div.fQxwff:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)').send_keys(self.recovery_email)
            # time.sleep(1)
            browser.find_element(By.CSS_SELECTOR, 'input[id="day"]').send_keys(
                random.randint(1, 28)
            )
            time.sleep(1)
            browser.find_element(By.CSS_SELECTOR, 'input[id="year"]').send_keys(
                random.randint(1990, 2000)
            )
            time.sleep(1)
            try:
                browser.find_element(By.CSS_SELECTOR, "#gender").click()
            except:
                print(
                    "Cannot locate Gender Blockm Please manually click it. Sleep 1 min...")
                time.sleep(60)
                pass
            try:
                time.sleep(0.5)
                try:
                    browser.find_element(By.CSS_SELECTOR, "#gender > option:nth-child(%d)" % random.randint(1, 4)
                                         ).click()
                except:
                    browser.quit()
                    exit(1)
                    browser.find_elements_by_xpath("").click()
            except:
                time.sleep(0.5)
                browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[2]/form/div[2]/div/div[4]/div[1]/div/div[2]/select/option[%d]"
                                     % random.randint(1, 4)
                                     ).click()
            time.sleep(1 + 3 * random.random())
            browser.find_element(
                By.CSS_SELECTOR, 'div[id="personalDetailsNext"]').click()
            browser.implicitly_wait(10)
            time.sleep(1)
            while True:
                try:
                    browser.find_element(By.CSS_SELECTOR, ".mUbCce").click()
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    break
            browser.find_element(
                By.CSS_SELECTOR, "#termsofserviceNext").click()
            browser.implicitly_wait(10)

            print("Success :)")
            browser.quit()

            print("adding account to database... \n")

    def create_account_not_working(self):
        # with request not working
        url = "https://accounts.google.com/signin/v2/challenge/password/empty"
        headers = {
            'User-Agent': self.person.create_user_agent(),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'firsName': self.person.first_name,
            'lastName': self.person.last_name,
            'Username': self.person.user_name,
            'Passwd': self.person.password,
            'ConfirmPasswd': self.person.password
        }
        response = self.request.make_request(url, headers, body)
