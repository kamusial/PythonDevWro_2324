from selenium import webdriver
from selenium4_POM import LoginPage
from selenium2 import make_screenshot
import time
import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()

    assert driver.current_url == 'https://www.saucedemo.com/'
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == url
    except AssertionError:
        print('Logowanie nie powiodlo sie')
        raise
    else:
        print('logowanie poprawne')
    finally:
        print('koniec')
        driver.quit()
