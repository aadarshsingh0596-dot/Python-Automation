
from selenium.webdriver.common.by import By

class Login_Admin_Page:
    text_by_username = "Username"
    text_by_password = "Password"
    text_by_login_by_type = "//*[@type='submit']"


    def __init__(self,driver):
        self.driver = driver





