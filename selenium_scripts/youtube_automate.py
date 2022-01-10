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

class YoutubeAutomate(object):
    def __init__(self, username, password, channels_url, driver_path, driver_mode='firefox'):
        self.logger = logging.getLogger()

        self.logger.info(
            "\n\n------------------------------------------------------\n\n")

        if not os.environ.get('DISPLAY'):
            os.environ['DISPLAY'] = ':0'

        if driver_mode == 'firefox':
            self._firefox_options = webdriver.FirefoxOptions()
            self._firefox_options.add_argument("-incognito")
            self.driver = webdriver.Firefox(
                executable_path=driver_path, options=self._firefox_options)
            self.logger.info("Firefox Driver initiated.\n")
        else:
            self._chrome_options = webdriver.ChromeOptions()
            self._chrome_options.add_argument("-incognito")
            self._chrome_options.add_argument("disable-infobars")
            self._chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(
                executable_path=driver_path, options=self._chrome_options)
            self.logger.info("Chrome Driver initiated.\n")

        self.driver.maximize_window()
        self.logger.info("Driver window maximized.\n")

        self.driver.get("https:\\www.youtube.com")
        self.driver.implicitly_wait(30)
        self.logger.debug("opening Youtube.\n")

        self.username = username
        self.password = password
        self.channels_url = channels_url

    # Login to your youtube account
    def login(self):

        # Finding and click on login link on youtube home page
        try:
            self.logger.debug(
                'Finding login link on youtube homepage element by xpath: //*[@id="text"].')
            self._login_link = self.driver.find_element_by_xpath(
                '//*[@id="text"]')
            self._login_link.click()
            self.logger.debug(f"Element Found: {self._login_link} ")
        except:
            self.logger.exception("Error found when finding login link.")
            self.logger.debug(
                'Finding login link on youtube homepage element with explicit wait by xpath: //*[@id="text"] ')
            self._login_link = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="text"]'))
            )
            self._login_link.click()
            self.logger.debug(f"Element Found: {self._login_link}\n")

        # Finding, entering and clicking on email form found on login page
        try:
            self.logger.debug("Finding email element by name: identifier.")
            self._email = self.driver.find_element_by_name("identifier")
            self._email.send_keys(self.username + Keys.ENTER)
            self.logger.debug(
                f"Element Found: {self._email}\nEntered email: {self.username} and pressed enter.")
        except:
            self.logger.exception("Error found in finding email link: ")
            self.logger.debug(
                "\n\nFinding email element by id: identifierId.\n")
            self._email = self.driver.find_element_by_id("identifierId")
            self._email.send_keys(self.username + Keys.ENTER)
            self.logger.debug(
                f"Element Found: {self._email}\nEntered email: {self.username} and pressed enter.\n")

        try:
            self.logger.debug("Finding password element by name: password\n")
            self._pas = self.driver.find_element_by_name("password")
            self._pas.send_keys(self.password + Keys.ENTER)
            self.logger.debug(
                f"Password Element Found: {self._pas}\nPressed enter.\n")
        except:
            self.logger.exception(
                "Error found in finding password link:  \n\n")

            # wait for transition then continue to fill items
            self.logger.debug(
                "Finding password element by name with explicit wait: password\n")
            self._pas = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'password')))
            self._pas.send_keys(self.password)

            self.logger.debug(f"Password Element Found: {self._pas}\n")

        try:
            self.logger.debug("Finding next element by id: passwordNext\n")
            # nex = driver.find_element_by_id('passwordNext')
            # nex.click()
            # nex.send_keys(Keys.ENTER)
            self._next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, 'passwordNext')))
            self._next_button.click()
            self.logger.debug(f"Element Found: {self._next_button}\n")
        except:
            self.logger.exception("Error found in finding next link:  \n\n")

            self.logger.debug(
                "Finding next element by id with explicit wait: passwordNext\n")
            self._next_button = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span')
            self._next_button.click()
            self.logger.debug(
                f"Next Button Element Found: {self._next_button}\n")

        time.sleep(3)
        for self.url in self.channels_url:
            self.subscribe_user(self.url)
            time.sleep(2)

        time.sleep(2)
        self.driver.quit()

    # Search Users and follow them
    def subscribe_user(self, channels_url):
        self.driver.get(channels_url)
        self.logger.info(f"\nOpening {channels_url}\n")
        time.sleep(2)

        # Finding Subscribe Button
        try:
            self.logger.debug(
                'Finding subscribe button element by xpath: //*[@id="text"]\n')
            self._subscribe = self.driver.find_element_by_xpath(
                '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string')
            self._subscribe.click()
            self.logger.info(
                f'Found the link {self._subscribe} and clicked on it.\n\n')
        except:
            self.logger.exception(
                "Error found during finding subscribe button: \n\n")
            self.logger.debug(
                'Finding subscribe button element with explicit wait by xpath: //*[@id="text"]\n')
            self._subscribe = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string'))
            )
            self._subscribe.click()
            self.logger.info(
                f'Found the link {self._subscribe} and clicked on it.\n\n')


if __name__ == "__main__":
    gecko_driver_path = os.path.join(ROOT_DIR, 'geckodriver')

    youtube_username = 'your_google_username'
    youtube_userpassword = 'your_google_userpassword'

    users_list = ['https://www.youtube.com/amitbhawani',
                  'https://www.youtube.com/phoneradar', 'https://www.youtube.com/triprazer']

    youtube = YoutubeAutomate(
        username=youtube_username,
        password=youtube_userpassword,
        channels_url=users_list,
        driver_path=gecko_driver_path,
        driver_mode='firefox'
    )
    youtube.login()
