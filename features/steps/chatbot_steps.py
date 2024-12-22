import time
from behave import given, when, then
from features.pages.chatbot_page import ChatbotPage
import utils.config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("Admin is logged into the application")
def step_impl(context):
    context.driver.get(context.base_url)
    # Enter username and password
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[1]/div/input').send_keys(
        utils.config.USER_NAME)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[2]/div/input').send_keys(
        utils.config.PASSWORD)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[3]/button').click()
    time.sleep(5)
    print("Admin logged into the application")

@when("Admin clicks on an institute from the institutes page")
def step_impl(context):
    # Simulate navigation to an institute
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[3]/div').click()
    time.sleep(3)
    print("Admin clicked on an institute")

@when("Admin navigates to the Chatbot page")
def step_impl(context):
    # Wait until the Chatbot page link is clickable
    chatbot_link = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div/div[1]/a[4]'))
    )
    chatbot_link.click()  # Click the Chatbot link
    print("Admin navigated to the Chatbot page")

@then("Enter the Question in the chat bot field and send")
def step_impl(context):
    # Wait for the question input field to be present in the DOM
    question_field = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/flowise-chatbot//div/div/div/div[2]/div[3]/div/div/textarea'))
    )
    question_field.send_keys('Hai')  # Enter the question

    # Wait for the send button to be clickable
    send_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/flowise-chatbot//div/div/div/div[2]/div[2]/div/div/button'))
    )
    send_button.click()  # Click the send button
    print("Question sent to the Chatbot")