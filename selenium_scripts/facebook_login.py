import logging
import logging.config
import os
import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
log_config_file_path = os.path.join(ROOT_DIR, "logging_config.ini")
logging.config.fileConfig(log_config_file_path)


class FacebookLogin(object):
    def __init__(self, username, password, users_url):
        """Initialises webdriver and opens the login page

        Arguments:
            username {str} -- email of the facebook user
            password {str} -- password of the facebook user
            users_url {iterable} -- list of urls of the facebook users to be followed

        """
        self.logger = logging.getLogger()

        self.initiate_chrome_webdriver
        # self.initiate_firefox_webdriver

        self.driver.maximize_window()
        self.logger.info("Driver window maximized.")

        self.driver.get(r"https:\\www.facebook.com\login")
        self.logger.debug("opening Facebook.")

        self.username = username
        self.password = password
        self.users_url = users_url
        # self.driver.save_screenshot("p.png")

    @property
    def initiate_chrome_webdriver(self):
        """Initiates a driver instance of chrome webdriver"""
        # instantiate chrome webdriver
        self._chrome_options = webdriver.ChromeOptions()

        # open in incognito mode
        self._chrome_options.add_argument("-incognito")

        # # open chrome without gui
        # self._chrome_options.add_argument("--headless")

        # This disables the message "Chrome is being is controlled by automated test software."
        # # deprecated in newer version of chrome webdriver
        # self._chrome_options.add_argument("disable-infobars")
        # this one works
        self._chrome_options.add_experimental_option(
            name="excludeSwitches",
            value=['enable-automation']
        )
        self._chrome_options.add_experimental_option("detach", True)

        # # set user agent
        # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
        # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/77.0.3865.90 Safari/537.36
        self._chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36")

        self.driver = webdriver.Chrome(
            executable_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "chromedriver"
            ),
            options=self._chrome_options)

        # get user agent
        agent = self.driver.execute_script("return navigator.userAgent")
        self.logger.info(f"Chrome Driver initiated with user agent: {agent}")

    @property
    def initiate_firefox_webdriver(self):
        """Initiates a driver instance of firefox webdriver"""
        # instantiating firefox webdriver
        self._firefox_options = webdriver.FirefoxOptions()
        # open in incognito mode
        self._firefox_options.add_argument("-incognito")

        # open chrome without gui
        self._firefox_options.add_argument("--headless")

        # setting user agent for firefox profile
        self._firefox_profile = webdriver.FirefoxProfile()

        # set user agent
        # Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
        # Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
        self._firefox_profile.set_preference(
            key="general.useragent.override",
            value="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
        )

        self.driver = webdriver.Firefox(
            executable_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "geckodriver"
            ),
            options=self._firefox_options,
            firefox_profile=self._firefox_profile)

        # get user agent
        agent = self.driver.execute_script("return navigator.userAgent")
        self.logger.info(f"Firefox Driver initiated with user agent: {agent}")

    # Login to fb account

    def login(self):
        """Logs in to thefb account using specified credentials and follows the users afterwards"""
        username_elem_id = "email"
        password_elem_id = "pass"

        try:
            # ----------------------------------------------------------------------------------------
            # Finding, entering and clicking on email form found on login page
            try:
                self.logger.debug("Finding username element by id:  email ")
                self._email = self.driver.find_element_by_id(username_elem_id)
                self._email.send_keys(self.username)
                self.logger.debug(
                    f"Element Found: {self._email} Entered email/username: {self.username} ")
            except:
                self.logger.exception("Error found in finding email link:  ")
                self.logger.debug(
                    "Finding email/username element using explicit time by id:  email. ")
                self._email = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, username_elem_id))
                )
                self._email.send_keys(self.username)
                self.logger.debug(
                    f"Element Found: {self._email} Entered email: {self.username}  ")

            # ----------------------------------------------------------------------------------------
            # finding password element by id
            try:
                self.logger.debug("Finding password element by id:  pass")
                self._pas = self.driver.find_element_by_id(password_elem_id)
                self._pas.send_keys(self.password + Keys.ENTER)
                self.logger.debug(
                    f"Password Element Found: {self._pas} Pressed enter. ")
            except:
                self.logger.exception(
                    "Error found in finding password link:  ")

                # wait for transition then continue to fill items
                self.logger.debug(
                    "Finding password element by name with explicit wait - id: pass ")
                self._pas = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.ID, password_elem_id)))
                self._pas.send_keys(self.password, Keys.ENTER)

                self.logger.debug(f"Password Element Found: {self._pas} ")

            # ----------------------------------------------------------------------------------------

        except:
            self.new_ui_login

        time.sleep(0.5)
        for url in self.users_url:
            self.followUser(url)
            time.sleep(2)

        time.sleep(2)
        self.driver.quit()

    @property
    def new_ui_login(self):
        username_elem_name = "email"
        password_elem_name = "pass"

        # ----------------------------------------------------------------------------------------
        # finding email element from new fb login page by name
        try:
            self.logger.info("Finding email element from new UI")
            self._email = self.driver.find_element_by_name(
                name=username_elem_name
            )
            self._email.send_keys(self.username)
            self.logger.debug(
                f"Element Found: {self._email}. Entered email/username: {self.username}")

        except Exception:
            self.logger.exception("Error found in finding email link:  ")
            self.logger.debug(
                "Finding email/username element using explicit time by name:  email")
            self._email = WebDriverWait(
                driver=self.driver,
                timeout=20
            ).until(
                EC.presence_of_element_located(
                    locator=(By.NAME, username_elem_name)
                )
            )
            self._email.send_keys(self.username)
            self.logger.debug(
                f"Element Found: {self._email}. Entered email: {self.username}")

        # ----------------------------------------------------------------------------------------
        # finding password element from new fb login page by name
        try:
            self.logger.info("Finding password element from new UI")
            self._pas = self.driver.find_element_by_name(
                name=password_elem_name
            )
            self._pas.send_keys(self.password + Keys.ENTER)
            self.logger.debug(
                f"Element Found: {self._pas}.")

        except Exception:
            self.logger.exception("Error found in finding password link:  ")
            self.logger.debug(
                "Finding password element using explicit time by name:  pass")
            self._pas = WebDriverWait(
                driver=self.driver,
                timeout=20
            ).until(
                EC.presence_of_element_located(
                    locator=(By.NAME, password_elem_name)
                )
            )
            self._pas.send_keys(self.password+Keys.ENTER)
            self.logger.debug(
                f"Element Found: {self._pas}")

    # Search Users and follow them

    def followUser(self, user_url):
        """Follows the fb user.

        Takes user's profile url, search for the element and press follow button.

        Arguments:
            user_url {str} -- profile url of the facebook page to be followed

        """
        self.driver.get(user_url)
        self.logger.info(f" Opening {user_url} ")
        time.sleep(2)

        # Finding follow Button
        try:
            self.logger.debug(
                'Finding follow button element by class name: likeButton _4jy0 _4jy4 _517h _51sy _42ft ')
            self._follow = self.driver.find_element_by_css_selector(
                ".likeButton._4jy0._4jy4._517h._51sy._42ft")
            self._follow.click()
            self.logger.info(
                f'Found the link {self._follow} and clicked on it.')
        except exceptions.NoSuchElementException:
            try:
                self.logger.exception(
                    "Error found during finding follow button: ")
                self.logger.debug(
                    'Finding follow button element with explicit wait by class name: likeButton _4jy0 _4jy4 _517h _51sy _42ft ')
                self._follow = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".likeButton._4jy0._4jy4._517h._51sy._42ft"))
                )
                self._follow.click()
                self.logger.info(
                    f'Found the link {self._follow} and clicked on it.')

            except exceptions.TimeoutException:
                self.logger.exception(
                    "Error found during finding follow button: ")
                self.logger.debug(
                    'Finding follow button element with explicit wait by class name: _42ft _4jy0 _63_s _4jy4 _4jy2 selected _51sy mrs ')
                self._follow = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "._42ft._4jy0._63_s._4jy4._4jy2.selected._51sy.mrs"))
                )
                self._follow.click()
                self.logger.info(
                    f'Found the link {self._follow} and clicked on it.')


if __name__ == "__main__":

    users_url_list = ['https://www.facebook.com/TwoOneC/',
                      'https://www.facebook.com/HappyClubWala/', 'https://www.facebook.com/santabantaRB/']

    try:
        fb = FacebookLogin(username="my_email",
                           password="my_password",
                           users_url=users_url_list)
        fb.login()
    finally:
        time.sleep(5)
        if fb.driver.service.process != None:
            fb.driver.quit()
