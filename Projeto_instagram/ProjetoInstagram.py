import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
url = "https://www.instagram.com/"

def all_execute(user, password):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys(f'{user}' + Keys.TAB)
    driver.find_element(By.NAME, "password").send_keys(f'{password}' + Keys.ENTER)
    time.sleep(5)
    #Transforma o navegador para modo mobile.
    driver.get(f'{url}{user}')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press(['i'])
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press(['m'])
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    driver.refresh()
    time.sleep(10)

    # driver.quit()


all_execute(user = '', password= '')