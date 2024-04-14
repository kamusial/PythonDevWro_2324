from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.w3schools.com/')
time.sleep(1)
# accept = driver.find_element(By.ID, 'accept-choices')
# accept.click()
try:
    driver.find_element(By.ID, 'accept-choices').click()
except NoSuchElementException:
    print('nie ma ciasteczek')

time.sleep(1)
menu = driver.find_element(By.ID, 'navbtn_tutorials')
# menu.click()
# time.sleep(1)
HTMLtutorial = driver.find_element(By.XPATH, '//*[@id="tutorials_html_css_links_list"]/div[1]/a[2]')
# HTMLtutorial.click()
# time.sleep(1)

webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
time.sleep(1)

#HTML_forms_attributes = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[41]')
HTML_forms_attributes = driver.find_element(By.LINK_TEXT, 'HTML Form Attributes')
HTML_forms_attributes.click()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()
time.sleep(3)

currentWindowName = driver.current_window_handle
windowNames = driver.window_handles
print(currentWindowName)
print(windowNames)

for okno in windowNames:
    if okno != currentWindowName:
        driver.switch_to.window(okno)

# driver.switch_to.window(windowNames[1])
time.sleep(3)

driver.switch_to.frame(driver.find_element(By.ID, 'iframeResult'))
firstName = driver.find_element(By.ID, 'fname')
if firstName.is_enabled():
    firstName.clear()
    firstName.send_keys('Kamil')
else:
    print('Nie da się kliknąć')

time.sleep(3)

driver.quit()