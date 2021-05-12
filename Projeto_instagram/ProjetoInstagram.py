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
    pyautogui.hotkey('ctrl','shift','i')
    time.sleep(5)
    pyautogui.hotkey('ctrl','shift','m')
    time.sleep(3)
    driver.refresh()
    time.sleep(10)
    # pyautogui.click('imagem.png')
    # pyautogui.doubleClick()
    # driver.quit()


all_execute(user = '', password= '')
