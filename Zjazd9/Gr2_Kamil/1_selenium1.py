from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
time.sleep(1)
driver.get('https://google.com')
time.sleep(1)
print(f'tytul strony {driver.title}')
button1_accept = driver.find_element('id', 'L2AGLb')
# print(button1_accept)
# print(type(button1_accept))
button1_accept.click()
time.sleep(1)
search_field = driver.find_element('name', 'q')
search_field.send_keys('Dokad noca tupta jez?')
time.sleep(1)
# search_button = driver.find_element('name', 'btnK')
search_field.send_keys(Keys.ENTER)
# search_button.submit()
time.sleep(1)

driver.quit()
