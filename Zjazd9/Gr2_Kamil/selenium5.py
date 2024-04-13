from selenium import webdriver
from selenium4_POM import LoginPage
from selenium2 import make_screenshot
import time

def test_login_page():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()

    assert driver.current_url == 'https://www.saucedemo.com/'
    page.enter_username('standard_user')
    page.enter_password('secret_sauce')
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    except AssertionError:
        print('Logowanie nie powiodlo sie')
        raise
    else:
        print('logowanie poprawne')
    finally:
        print('koniec')
        driver.quit()

def test_login_page2():
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()

    assert driver.current_url == 'https://www.saucedemo.com/'
    page.enter_username('standard_user1')
    page.enter_password('secret_sauce')
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == 'https://www.saucedemo.com/'
    except AssertionError:
        print('Logowanie nie powiodlo sie')
        raise
    else:
        print('logowanie poprawne')
    finally:
        print('koniec')
        driver.quit()