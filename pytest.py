
# login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        self.password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "pass"))
        )
        self.login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )

    def enter_username(self, username):
        self.username_input.clear()
        self.username_input.send_keys("username")

    def enter_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys("password")

    def click_login_button(self):
        self.login_button.click()
