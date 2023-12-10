from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://google.com')
print(f'Nazwa strony {driver.title}')
sleep(1)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
sleep(1)

driver.quit()