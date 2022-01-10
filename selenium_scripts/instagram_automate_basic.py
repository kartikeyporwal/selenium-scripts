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


# On main page link - Link Text: Log in
# on login page email field - name: username
# on login page password field - name: password
# on login page to login: hit enter
# Pressing not now button on timeline page - class:  aOOlW HoLwm
# On timeline page to search - xpath:  //*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input
# Click on searched user - xpath:  //*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]
# Follow Person by - xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button
# Follow Person by - class: _5f5mN    -fzfL     _6VtSN     yZn4P


def login(email, password):
    logger.info("\n\n------------------------------------------------------\n\n")

    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument("-incognito")
    # driver = webdriver.Firefox(executable_path='/home/kartikey/anaconda3/envs/automate/geckodriver')
    # logger.info("Firefox Driver initiated.\n")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("-incognito")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        executable_path='/home/kartikey/anaconda3/envs/automate/chromedriver',
        options=chrome_options
    )
    logger.info("Chrome Driver initiated.\n")

    driver.maximize_window()
    logger.info("Driver window maximized.\n")

    driver.get("https:\\www.instagram.com")
    logger.debug("opening instagram.\n")

    # Finding and clicking on login button found on homepage which redirects to login form
    try:
        logger.debug(
            "Finding login link from homepage - element by Link Text: Log in.\n")
        link = driver.find_element_by_link_text('Log in')
        link.click()
        logger.debug(f"Link Element Found: {link} \t and clicked.\n")
    except:
        logger.exception('Error found in finding link. \n\n')
        logger.debug(
            "\n\nFinding login link from homepage using wait - element by Link Text: Log in.\n")
        link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Log in"))
        )
        link.click()
        logger.debug(f"Link Element Found: {link} \t and clicked.\n")

    time.sleep(0.5)

    # Finding Email link
    try:
        logger.debug(
            "Finding email/username field from login form - element by name: username.\n")
        username = driver.find_element_by_name('username')
        username.send_keys(email)
        logger.debug(
            f"email/username Element Found: {username} \t and entered username: {email}.\n")
    except:
        logger.exception('Error found in finding email/user element. \n\n')
        logger.debug(
            "Finding email/username field from login form using wait - element by name: username.\n")
        username = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys(email)
        logger.debug(
            f"email/username Element Found: {username} \t and entered username: {email}.\n")

    # Finding Password link
    try:
        logger.debug(
            "Finding password field from login form - element by name: password.\n")
        pas = driver.find_element_by_name('password')
        pas.send_keys(password + Keys.ENTER)
        logger.debug(f"password field Element Found: {pas} \n")
    except:
        logger.exception('Error found in finding password field element. \n\n')
        logger.debug(
            "Finding password field link from login form using wait - element by name: password.\n")
        pas = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        pas.send_keys(password + Keys.ENTER)
        logger.debug(f"Password field Element Found: {pas} .\n")

    # Press notification off
    try:
        logger.debug(
            "Finding Not Now Button field from timeline - element by class: aOOlW HoLwm.\n")
        not_now = driver.find_element_by_css_selector(".aOOlW.HoLwm")
        not_now.click()
        logger.debug(
            f"Not Now Button field Element Found: {not_now} and clicked on it.\n")
    except:
        logger.exception(
            'Error found in finding Not Now Button field element. \n\n')
        logger.debug(
            "Finding Not Now Button field link from timeline using wait - element by class: aOOlW HoLwm.\n")
        not_now = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".aOOlW.HoLwm"))
        )
        not_now.click()
        logger.debug(
            f"Not Now Button field Element Found: {not_now} and clicked on it.\n")

    logger.info("\n\n------------------------------------------------------\n\n")


def search_and_follow(user_name):
     # SEarch bar
    try:
        logger.debug(
            "Finding Search field from timeline - element by xpath: //*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input\n")
        search = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(user_name + Keys.ENTER + Keys.ENTER)
        logger.debug(
            f"Search field Element Found: {search} and clicked on it.\n")
    except:
        logger.exception('Error found in finding Search field element. \n\n')
        logger.debug(
            "Finding Search field link from timeline using wait - element by xpath: //*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input\n")
        search = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
        )
        search.send_keys(user_name + Keys.ENTER + Keys.ENTER)
        logger.debug(
            f"Search field Element Found: {search} and clicked on it.\n")

    time.sleep(2)

    # clicking on user link
    try:
        logger.debug(
            'Finding user field from timeline - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button')
        # fl = driver.find_element_by_xpath(f'//a[@href={url}]')
        fl = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
        fl.click()
        logger.debug(f"User field Element Found: {fl} and clicked on it.\n")
    except:
        logger.exception('Error found in finding User field element. \n\n')
        logger.debug(
            'Finding User field link from timeline using wait - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button\n')
        # fl = WebDriverWait(driver,20).until(
        #     EC.presence_of_element_located((By.XPATH, f'//a[@href={url}]'))
        # )
        fl = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]'))
        )
        fl.click()
        logger.debug(f"User field Element Found: {fl} and clicked on it.\n")

    # Follow User
    try:
        logger.debug(
            'Finding follow user field from timeline - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button')
        follow = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button')
        follow.click()
        logger.debug(
            f"Follow field Element Found: {follow} and clicked on it.\n")
    except:
        logger.exception(
            'Error found in finding follow button field element. \n\n')
        logger.debug(
            'Finding Follow field link from timeline using wait - element by xpath: //*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button\n')
        follow = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button'))
        )
        follow.click()
        logger.debug(
            f"Follow field Element Found: {follow} and clicked on it.\n")


if __name__ == "__main__":
    email = ''
    password = ''

    login(email, password)
