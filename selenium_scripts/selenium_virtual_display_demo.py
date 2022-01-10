import os

from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=1, size=(1100, 500))
display.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    executable_path=os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "chromedriver"
    ),
    chrome_options=chrome_options
)

driver.delete_all_cookies()
# driver.set_window_size(800, 800)
# driver.set_window_position(0, 0)

print('arguments done')

driver.get('http://google.com')
