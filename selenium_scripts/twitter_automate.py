import logging
import os
import time
from logging.config import fileConfig

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
log_config_file_path = os.path.join(ROOT_DIR, "logging_config.ini")
logging.config.fileConfig(log_config_file_path)
logger = logging.getLogger()


# Youtube Sign it link xpath: //*[@id="text"]
# Youtube Subscribe xpath:  //*[@id="text"] or //*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string

class TwitterAutomate(object):
    def __init__(self, username, password, user_url):
        self.logger = logging.getLogger()

        self.logger.info(
            "\n\n------------------------------------------------------\n\n")

        # self._firefox_options = webdriver.FirefoxOptions()
        # self._firefox_options.add_argument("-incognito")
        # self.driver = webdriver.Firefox(executable_path='/home/kartikey/anaconda3/envs/automate/geckodriver', options=self._firefox_options)
        # self.logger.info("Firefox Driver initiated.\n")

        self._chrome_options = webdriver.ChromeOptions()
        self._chrome_options.add_argument("-incognito")
        self._chrome_options.add_argument("disable-infobars")
        self._chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            executable_path='/home/kartikey/anaconda3/envs/automate/chromedriver', options=self._chrome_options)
        self.logger.info("Chrome Driver initiated.\n")

        self.driver.maximize_window()
        self.logger.info("Driver window maximized.\n")

        self.driver.get("https:\\www.twitter.com\login")
        self.logger.debug("opening Twitter.\n")

        self.username = username
        self.password = password
        self.user_url = user_url

    # Login to your youtube account
    def login(self):
        # # Finding and click on login link on youtube home page
        # try:
        #     self.logger.debug('Finding login link on twitter homepage element by link_text: Log in.\n')
        #     self._login_link.find_element_by_link_text('Log in')
        #     self._login_link.click()
        #     self.logger.debug(f"Login Element Found: {self._login_link}\n")
        # except:
        #     self.logger.exception("\nError found when finding login link.\n\n")
        #     self.logger.debug('Finding login link on twitter homepage element with explicit wait by link_text: Log in\n')
        #     self._login_link = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.LINK_TEXT, 'Log in'))
        #     )
        #     self._login_link.click()
        #     self.logger.debug(f"Login Element Found: {self._login_link}\n")

        # Finding, entering and clicking on email form found on login page
        try:
            self.logger.debug(
                "Finding username element by css selector: .js-username-field.email-input.js-initial-focus.\n")
            self._email = self.driver.find_element_by_css_selector(
                '.js-username-field.email-input.js-initial-focus')
            self._email.send_keys(self.username)
            self.logger.debug(
                f"Element Found: {self._email}\nEntered email/username: {self.username}\n")
        except:
            self.logger.exception("Error found in finding email link:  \n\n")
            self.logger.debug(
                "\n\nFinding email/username element by css selector: .js-username-field.email-input.js-initial-focus.\n")
            self._email = self.driver.find_element_by_css_selector(
                '.js-username-field.email-input.js-initial-focus')
            self._email.send_keys(self.username)
            self.logger.debug(
                f"Element Found: {self._email}\nEntered email: {self.username} \n")

        try:
            self.logger.debug(
                "Finding password element by class: js-password-field\n")
            self._pas = self.driver.find_element_by_class_name(
                "js-password-field")
            self._pas.send_keys(self.password + Keys.ENTER)
            self.logger.debug(
                f"Password Element Found: {self._pas}\nPressed enter.\n")
        except:
            self.logger.exception(
                "Error found in finding password link:  \n\n")

            # wait for transition then continue to fill items
            self.logger.debug(
                "Finding password element by name with explicit wait - class: js-password-field\n")
            self._pas = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'js-password-field')))
            self._pas.send_keys(self.password, Keys.ENTER)

            self.logger.debug(f"Password Element Found: {self._pas}\n")

        # try:
        #     self.logger.debug("Finding next element by id: passwordNext\n")
        #     # nex = driver.find_element_by_id('passwordNext')
        #     # nex.click()
        #     # nex.send_keys(Keys.ENTER)
        #     self._next_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'passwordNext')))
        #     self._next_button.click()
        #     self.logger.debug(f"Element Found: {self._next_button}\n")
        # except:
        #     self.logger.exception("Error found in finding next link:  \n\n")

        #     self.logger.debug("Finding next element by id with explicit wait: passwordNext\n")
        #     self._next_button = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span')
        #     self._next_button.click()
        #     self.logger.debug(f"Next Button Element Found: {self._next_button}\n")

        time.sleep(0.5)
        for self.url in self.user_url:
            self.follow_user(self.url)
            time.sleep(2)

        time.sleep(2)
        self.driver.quit()

    # Search Users and follow them
    def follow_user(self, user_url):
        self.driver.get(user_url)
        self.logger.info(f"\nOpening {user_url}\n")
        time.sleep(2)

        # Finding Subscribe Button
        try:
            self.logger.debug(
                'Finding follow button element by class name: user-actions-follow-button\n')
            self._follow = self.driver.find_element_by_class_name(
                "user-actions-follow-button")
            self._follow.click()
            self.logger.info(
                f'Found the link {self._follow} and clicked on it.\n\n')
        except:
            self.logger.exception(
                "Error found during finding follow button: \n\n")
            self.logger.debug(
                'Finding follow button element with explicit wait by class name: user-actions-follow-button\n')
            self._follow = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, 'user-actions-follow-button'))
            )
            self._follow.click()
            self.logger.info(
                f'Found the link {self._follow} and clicked on it.\n\n')


if __name__ == "__main__":

    demo_list = ['https://twitter.com/hello',
                 'https://twitter.com/mikeolicious']

    twitter_user_name = ''
    twitter_user_password = ''

    twitter = TwitterAutomate(
        twitter_user_name, twitter_user_password, demo_list)
    twitter.login()
