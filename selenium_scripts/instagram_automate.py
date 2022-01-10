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


class InstagramAutomate(object):
    def __init__(self, username, password, insta_user_list):
        self.logger = logging.getLogger()

        self.logger.info(
            "\n\n------------------------------------------------------\n\n")

        # self._firefox_options = webdriver.FirefoxOptions()
        # self._firefox_options.add_argument("-incognito")
        # self.driver = webdriver.Firefox(
        #     executable_path='/home/kartikey/anaconda3/envs/automate/geckodriver', options=self._firefox_options)
        # self.logger.info("Firefox Driver initiated.\n")

        self._chrome_options = webdriver.ChromeOptions()
        self._chrome_options.add_argument("-incognito")
        self._chrome_options.add_argument("disable-infobars")
        self._chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(
            executable_path='/home/kartikey/anaconda3/envs/automate/chromedriver',
            options=self._chrome_options
        )
        self.logger.info("Chrome Driver initiated.\n")

        self.driver.maximize_window()
        self.logger.info("Driver window maximized.\n")

        self.driver.get("https:\\www.instagram.com")
        self.logger.debug("opening instagram.\n")

        self.username = username
        self.password = password
        self.insta_user_list = insta_user_list

    # Login to your account
    def login(self):

        # Finding and clicking on login button found on homepage which redirects to login form
        try:
            self.logger.debug(
                "Finding login link from homepage - element by Link Text: Log in.\n")
            # self._link = self.driver.find_element_by_link_text('Log in')
            self._link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
            )
            self._link.click()
            self.logger.debug(
                f"Link Element Found: {self._link} \t and clicked.\n")

        except:
            self.logger.exception('Error found in finding link. \n\n')
            self.logger.debug(
                "\n\nFinding login link from homepage using wait - element by Link Text: Log in.\n")
            self._link = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
            )
            self._link.click()
            self.logger.debug(
                f"Link Element Found: {self._link} \t and clicked.\n")

        time.sleep(2)

        # Finding Email link
        try:
            self.logger.debug(
                "Finding email/username field from login form - element by name: username.\n")
            # self._username = self.driver.find_element_by_name('username')
            self._username = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            self._username.send_keys(self.username)
            self.logger.debug(
                f"email/username Element Found: {self._username} \t and entered username: {self.username}.\n")

        except:
            self.logger.exception(
                'Error found in finding email/user element. \n\n')
            self.logger.debug(
                "Finding email/username field from login form using wait - element by name: username.\n")
            self._username = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            self._username.send_keys(self.username)
            self.logger.debug(
                f"email/username Element Found: {self._username} \t and entered username: {self.username}.\n")

        # Finding Password link
        try:
            self.logger.debug(
                "Finding password field from login form - element by name: password.\n")
            # self._pas = self.driver.find_element_by_name('password')
            self._pas = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            self._pas.send_keys(self.password + Keys.ENTER)
            self.logger.debug(f"password field Element Found: {self._pas} \n")

        except:
            self.logger.exception(
                'Error found in finding password field element. \n\n')
            self.logger.debug(
                "Finding password field link from login form using wait - element by name: password.\n")
            self._pas = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            self._pas.send_keys(self.password + Keys.ENTER)
            self.logger.debug(f"Password field Element Found: {self._pas} .\n")

        # Press notification off
        try:
            self.logger.debug(
                "Finding Not Now Button field from timeline - element by class: aOOlW HoLwm.\n")
            self._not_now = self.driver.find_element_by_css_selector(
                ".aOOlW.HoLwm")
            self._not_now.click()
            self.logger.debug(
                f"Not Now Button field Element Found: {self._not_now} and clicked on it.\n")
        except:
            self.logger.exception(
                'Error found in finding Not Now Button field element. \n\n')
            self.logger.debug(
                "Finding Not Now Button field link from timeline using wait - element by class: aOOlW HoLwm.\n")
            self._not_now = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".aOOlW.HoLwm"))
            )
            self._not_now.click()
            self.logger.debug(
                f"Not Now Button field Element Found: {self._not_now} and clicked on it.\n")

        # insta_user_list = ['phoneradar', 'amitbhawani', 'triprazer']
        for self.i in self.insta_user_list:
            self.search_and_follow(self.i)
            time.sleep(2)

        time.sleep(2)
        self.driver.quit()

    # Search Users and follow them

    def search_and_follow(self, user_to_be_followed):

        try:
            self.logger.debug(
                "Finding Search field from timeline - element by xpath: //*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input\n")
            self._search = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
            self._search.send_keys(
                user_to_be_followed + Keys.ENTER + Keys.ENTER)
            self.logger.debug(
                f"Search field Element Found: {self._search} and clicked on it.\n")
        except:
            self.logger.exception(
                'Error found in finding Search field element. \n\n')
            self.logger.debug(
                "Finding Search field link from timeline using wait - element by xpath: //*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input\n")
            self._search = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
            )
            self._search.send_keys(
                user_to_be_followed + Keys.ENTER + Keys.ENTER)
            self.logger.debug(
                f"Search field Element Found: {self._search} and clicked on it.\n")

        time.sleep(2)

        # clicking on user link
        try:
            self.logger.debug(
                'Finding user field from timeline - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button')
            # self.fl = driver.find_element_by_xpath(f'//a[@href={url}]')
            self._click_user = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
            self._click_user.click()
            self.logger.debug(
                f"User field Element Found: {self._click_user} and clicked on it.\n")
        except:
            self.logger.exception(
                'Error found in finding User field element. \n\n')
            self.logger.debug(
                'Finding User field link from timeline using wait - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button\n')
            # fl = WebDriverWait(driver,20).until(
            #     EC.presence_of_element_located((By.XPATH, f'//a[@href={url}]'))
            # )
            self._click_user = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]'))
            )
            self._click_user.click()
            self.logger.debug(
                f"User field Element Found: {self._click_user} and clicked on it.\n")

        time.sleep(1)
        # Follow User
        try:
            self.logger.debug(
                'Finding follow user field from timeline - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button')
            self._follow_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button')
            self._follow_button.click()
            self.logger.debug(
                f"Follow field Element Found: {self._follow_button} and clicked on it.\n")
        except:
            self.logger.exception(
                'Error found in finding follow button field element. \n\n')
            try:
                self.logger.debug(
                    'Finding Follow field link from timeline using wait - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button\n')
                self._follow_button = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button'))
                )
                self._follow_button.click()
                self.logger.debug(
                    f"Follow field Element Found: {self._follow_button} and clicked on it.\n")
            except:
                self.logger.exception(
                    'Error found in finding follow button field element. \n\n')
                self.logger.debug(
                    'Finding Follow field link from timeline using wait - element by css selector:  ._5f5mN.jIbKX._6VtSN.yZn4P\n')

                self._follow_button = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '._5f5mN.jIbKX._6VtSN.yZn4P'))
                )
                self._follow_button.click()
                self.logger.debug(
                    f"Follow field Element Found: {self._follow_button} and clicked on it.\n")

            # _5f5mN       jIbKX  _6VtSN     yZn4P   //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button
# //*[@id="react-root"]/section/main/div/header/section/div[1]/button
# _5f5mN       jIbKX  _6VtSN     yZn4P


if __name__ == "__main__":
    insta_user_name = ""
    insta_user_password = ""

    user_list = ['google', ]
    insta = InstagramAutomate(insta_user_name, insta_user_password, user_list)
    insta.login()

    for i in user_list:
        insta.search_and_follow(i)
        time.sleep(2)
