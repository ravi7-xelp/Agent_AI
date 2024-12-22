import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.config

class AdminPage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def login(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[1]/div/input').send_keys(
            utils.config.USER_NAME)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[2]/div/input').send_keys(
            utils.config.PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[3]/button').click()
        time.sleep(5)
        print("Super Admin logged into the application")

    def select_institute(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[3]/div').click()
        time.sleep(2)
        print("Super Admin clicked on an institute")

    def verify_metrics_page_navigation(self):
        current_url = self.driver.current_url
        assert "metrics" in current_url, f"URL does not contain 'metrics': {current_url}"
        time.sleep(3)
        print("Super Admin navigated to the metrics page")

    def click_settings(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[1]/a[7]').click()
        time.sleep(3)
        print("Super Admin clicked on the configuration option")

    def click_create_admin(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/button').click()
        time.sleep(3)
        print("Create admin form displayed")

    def fill_create_admin_form(self):
        popup_form = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]'))
        )

        self.driver.find_element(By.XPATH, '/html/body/div[3]/form/div[1]/input').send_keys('John')  # First Name
        self.driver.find_element(By.XPATH, '/html/body/div[3]/form/div[2]/input').send_keys('Doe')   # Last Name
        self.driver.find_element(By.XPATH, '/html/body/div[3]/form/div[3]/input').send_keys('john.doe@example.com')  # Email
        self.driver.find_element(By.XPATH, '/html/body/div[3]/form/div[4]/input').send_keys('9876543210')  # Contact

        submit_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/form/div[5]/button[2]')
        submit_button.click()
        print("Form submitted successfully!")
