# Page Object Model
from selenium import webdriver

class LoginPage:
    def __init__(self, okno):
        self.moje_okno = okno
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'

    def open(self):
        self.moje_okno.get('https://saucedemo.com')