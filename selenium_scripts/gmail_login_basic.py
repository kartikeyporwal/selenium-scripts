import logging
import os
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


def login(email, password):
    logger.info("\n\n------------------------------------------------------\n\n")

    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument("-incognito")
    # driver = webdriver.Firefox(executable_path=os.path.join(ROOT_DIR, 'geckodriver'))
    # logger.info("Firefox Driver initiated.\n")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("-incognito")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        executable_path=os.path.join(ROOT_DIR, 'chromedriver'),
        chrome_options=chrome_options
    )
    logger.info("Chrome Driver initiated.\n")

    driver.maximize_window()
    logger.info("Driver window maximized.\n")

    driver.get("https:\\www.gmail.com")
    logger.debug("opening gmail.\n")

    try:
        logger.debug("Finding email element by name: identifier.\n")
        em = driver.find_element_by_name("identifier")
        em.send_keys(email + Keys.ENTER)
        logger.debug(
            f"Element Found: {em}\nEntered email: {email} and pressed enter.\n")
    except:
        logger.exception("Error found in finding email link:  \n\n")
        logger.debug("\n\nFinding email element by id: identifierId.\n")
        em = driver.find_element_by_id("identifierId")
        em.send_keys(email + Keys.ENTER)
        logger.debug(
            f"Element Found: {em}\nEntered email: {email} and pressed enter.\n")

    try:
        logger.debug("Finding password element by name: password\n")
        pas = driver.find_element_by_name("password")
        pas.send_keys(password + Keys.ENTER)
        logger.debug(f"Element Found: {pas}\nPressed enter.\n")
    except:
        logger.exception("Error found in finding password link:  \n\n")

        # wait for transition then continue to fill items
        logger.debug(
            "Finding password element by name with explicit wait: password\n")
        pas = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'password')))
        pas.send_keys(password)

        logger.debug(f"Element Found: {pas}\n")

    try:
        logger.debug("Finding next element by id: passwordNext\n")
        # nex = driver.find_element_by_id('passwordNext')
        # nex.click()
        # nex.send_keys(Keys.ENTER)
        nex = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'passwordNext')))
        nex.click()
        logger.debug(f"Element Found: {nex}\n")
    except:
        logger.exception("Error found in finding next link:  \n\n")

        logger.debug(
            "Finding next element by id with explicit wait: passwordNext\n")
        nex = driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span')
        nex.click()
        logger.debug(f"Element Found: {nex}\n")

    logger.info("\n\n------------------------------------------------------\n\n")


if __name__ == "__main__":
    gmail_username = r''
    gmail_password = r''

    login(
        email=gmail_username,
        password=gmail_password
    )
