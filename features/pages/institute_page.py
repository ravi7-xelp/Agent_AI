from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstitutePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_institute_details(self):
        # Fill in the institute name and address
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div[1]/div/input").send_keys("New Institute")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div[2]/div/textarea').send_keys("123 Institute Lane")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[1]/div/input').send_keys("First name")
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[2]/div/input').send_keys("Last Name")
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[3]/div/input").send_keys("email@gmail.com")
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div[4]/div/input").send_keys(int("912324232"))
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div[3]/div/input").send_keys(r"D:\xelpmoc\AI_Agent_testing\AI_Agent\GlcLogo.png")

    def submit_form(self):
        # Click the submit button
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/form/div[2]/button").click()

    def wait_for_institute_creation(self):
        # Wait for the page to load and verify redirection
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("institutes")  # Wait until URL contains 'institutes'
        )

    def get_current_url(self):
        return self.driver.current_url

    def get_success_message(self):
        try:
            success_message = self.driver.find_element(By.ID, "success-msg").text
            return success_message
        except Exception as e:
            return None
