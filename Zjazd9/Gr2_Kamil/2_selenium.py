from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
print('Nazwa strony', driver.title)
time.sleep(1)

username_field = driver.find_element('id', 'user-name')
username_field.clear()
username_field.send_keys('standard_user')

password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
password_field.clear()
password_field.send_keys('secret_sauce')

time.sleep(1)
login_button = driver.find_element('name', 'login-button')

if not login_button.get_attribute('disabled'):
    print('Przycisk aktywny')
    login_button.click()

time.sleep(1)
driver.quit()