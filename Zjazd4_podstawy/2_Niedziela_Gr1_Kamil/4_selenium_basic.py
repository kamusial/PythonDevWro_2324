from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://google.com')
print(f'Nazwa strony {driver.title}')
sleep(1)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
sleep(1)
search_field = driver.find_element('name','q')
search_field.send_keys('Czy github dziala z MACem?')
sleep(1)
search_field.send_keys(Keys.ENTER)
# search_button = driver.find_element('name', 'btnK')
# search_button.submit()
sleep(1)
driver.quit()