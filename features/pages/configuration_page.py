# pages.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SuperAdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[1]/div/input')
        self.password_field = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[2]/div/input')
        self.login_button = (By.XPATH, '//*[@id="root"]/div[1]/div/div/div[3]/button')
        self.institute_link = (By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[3]/div')
        self.metrics_page_url = "/metrics"
        self.configuration_button = (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/a[2]')
        self.save_button = (By.XPATH, '//*[@id="root"]/div[2]/div/div/form/div[2]/button')

    def login(self, username, password):
        self.driver.get(self.driver.current_url)  # Go to the login page
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
        time.sleep(5)

    def click_on_institute(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.institute_link)
        ).click()
        time.sleep(2)

    def navigate_to_metrics(self):
        current_url = self.driver.current_url
        assert "metrics" in current_url, f"URL does not contain 'metrics': {current_url}"
        time.sleep(3)

    def click_on_configuration(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.configuration_button)
        ).click()
        time.sleep(3)

    def is_save_button_visible(self):
        try:
            save_button = self.driver.find_element(*self.save_button)
            return save_button.is_displayed()
        except:
            return False
