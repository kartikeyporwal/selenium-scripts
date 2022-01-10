import time

from selenium import webdriver


def main(twitter_user_email, twitter_user_password, ):
    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument("-incognito")
    # driver = webdriver.Firefox(
    #     executable_path='/home/kartikey/anaconda3/envs/automate/geckodriver'
    # )

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("-incognito")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        executable_path='/home/kartikey/anaconda3/envs/automate/chromedriver',
        chrome_options=chrome_options
    )

    driver.maximize_window()
    driver.get('https://twitter.com/login')
    driver.implicitly_wait(20)
    email = driver.find_element_by_css_selector(
        '.js-username-field.email-input.js-initial-focus')
    pas = driver.find_element_by_class_name('js-password-field')

    login = driver.find_element_by_css_selector(
        '.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')

    email.send_keys(twitter_user_email)
    pas.send_keys(twitter_user_password)
    login.click()

    search = driver.find_element_by_class_name('search-input')
    search.send_keys('Deepika Padukone')

    search_enter = driver.find_element_by_css_selector(
        '.Icon.Icon--medium.Icon--search.nav-search')
    search_enter.click()

    people_link = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[3]/a")
    people_link.click()

    driver.find_element_by_link_text("People").click()

    people_home = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div/div/a")
    people_home.click()

    time.sleep(1)
    driver.get(driver.current_url)

    # people_follow = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div/ul/li[6]/div/div/span[2]")
    # people_follow.click()

    # people_follow = driver.find_element_by_css_selector(".user-actions-follow-button.js-follow-btn.follow-button")
    # people_follow.click()

    people_follow = driver.find_element_by_class_name(
        "user-actions-follow-button").click()

    # for i in driver.find_element_by_tag_name('a'):
    # people_tag = driver.find_elements_by_css_selector('.AdaptiveFiltersBar-target.AdaptiveFiltersBar-target--link.js-nav.u-textUserColorHover')[2]
    # for i in people_tag:
    #     print(i)
    #
    # people_tag.click()


if __name__ == '__main__':
    twitter_user_email = ''
    twitter_user_password = ''
    main(twitter_user_email,
         twitter_user_password,)

