import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://www.instagram.com/"


def all_execute(user, password):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys(f'{user}' + Keys.TAB)
    driver.find_element(By.NAME, "password").send_keys(f'{password}' + Keys.ENTER)
    time.sleep(5)
    driver.get(f'{url}{user}')
    time.sleep(15)
    driver.quit()


all_execute(user = '', password= '')