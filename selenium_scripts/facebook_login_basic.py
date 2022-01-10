from selenium import webdriver


def login(fb_login_email, fb_login_password):
    driver = webdriver.Firefox(
        executable_path='/home/kartikey/anaconda3/envs/automate/geckodriver'
    )
    # driver = webdriver.Chrome(executable_path='/home/kartikey/anaconda3/envs/automate/chromedriver')

    driver.maximize_window()
    driver.get('https://www.facebook.com')

    email = driver.find_element_by_id('email')
    pas = driver.find_element_by_id('pass')

    login = driver.find_element_by_name('login')

    email.send_keys(fb_login_email)
    pas.send_keys(fb_login_password)
    login.click()


if __name__ == '__main__':

    fb_login_email = r''
    fb_login_password = r''

    login(
        fb_login_email=fb_login_email,
        fb_login_password=fb_login_password,
    )
