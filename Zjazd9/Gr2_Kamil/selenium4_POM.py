# Page Object Model
from selenium import webdriver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'

    def open(self):
        self.moje_okno.get('https://saucedemo.com')
        print(self.moje_okno.title)
        print(self.moje_okno.current_url)

    def enter_username(self, username):
        field = self.moje_okno.find_element('id', self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.moje_okno.find_element('id', self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.moje_okno.find_element('name', self.login_button_name)
        button.click()
