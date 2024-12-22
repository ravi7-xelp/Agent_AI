from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChatbotPage:
    def __init__(self, driver):
        self.driver = driver
        self.chat_flow_id_field = (By.XPATH, '//*[@id="radix-:ri:-content-general"]/div/div/div/form/div/div[1]/input')

    def get_chat_flow_id_value(self):
        # Get the value of the chat flow ID field
        chat_flow_id_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.chat_flow_id_field)
        )
        return chat_flow_id_element.get_attribute('value')

