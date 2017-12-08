import os

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

print DRIVER_BIN



driver = webdriver.Chrome(executable_path = DRIVER_BIN)
driver.get('http://www.google.com')
driver.find_element_by_name("q").send_keys("how to search in google")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.close()
