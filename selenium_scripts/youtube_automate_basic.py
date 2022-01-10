from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.common.action_chains import ActionChains


def login(gmail_username, gmail_password,):
    driver = webdriver.Firefox(
        executable_path='/home/kartikey/anaconda3/envs/automate/geckodriver')

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(executable_path='/home/kartikey/anaconda3/envs/automate/chromedriver', chrome_options=chrome_options)
    driver.maximize_window()

    driver.get('https://www.youtube.com/watch?v=CtgD91Ev4NU')
    driver.implicitly_wait(10)

    title = driver.find_element_by_class_name('title')
    driver.execute_script("arguments[0].scrollIntoView();", title)

    # html = driver.find_element_by_tag_name('html')
    # html.send_keys(Keys.DOWN)

    # subscribe = driver.find_element_by_id('subscribe-button')

    # subscribe = driver.find_element_by_id('subscribe-button')
    # subscribe = driver.find_element_by_css_selector('.style-scope.ytd-subscribe-button-renderer')

    # print("Done", subscribe)
    sub = driver.find_element_by_xpath('//*[@id="text"]')
    sub.click()

    email = driver.find_element_by_css_selector('#identifierId')
    email.send_keys(gmail_username)

    buton = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span')
    buton.click()

    # password = driver.find_element_by_name('password')

    pas = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, 'password')))
    pas.send_keys(gmail_password)
    # password = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input')
    # password.send_keys(gmail_password)

    buton = driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span')
    buton.click()
    # driver.execute_script("arguments[0].scrollIntoView();", subscribe)
    # driver.execute_script("arguments[0].scrollIntoView();", subscribe)

    # subscribe.click()
    print('Done Again')


if __name__ == '__main__':
    gmail_username = ''
    gmail_password = ''
    login(
        gmail_username,
        gmail_password,
    )


# subscribe '//*[@id="subscribe-button"]'
# '//*[@id="text"]'

# Next '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span'


# pass '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input'
