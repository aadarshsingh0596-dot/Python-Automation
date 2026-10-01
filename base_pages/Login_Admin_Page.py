
from selenium.webdriver.common.by import By

class Login_Admin_Page:
    text_by_username = "Username"
    text_by_password = "Password"
    text_by_login_by_type = "//*[@type='submit']"


    def __init__(self,driver):
        self.driver = driver


    def user_name(self,username):
        self.driver.findElement(By.ID,self.text_by_username).send_keys(username)

    def user_pass(self, password):
        self.driver.findElement(By.ID, self.text_by_password).send_keys(password)

    def click(self):
        self.driver.findElement(By.XPATH, self.text_by_login_by_type).click()






