from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[1]/div/input')
        self.password_field = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[2]/div/input')
        self.login_button = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[3]/button')
        self.logout_button = (By.XPATH,'/html/body/div/div[1]/div[3]')

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, username, password):
        """
        Combines username input, password input, and login button click.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    def log_out(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()