import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.config
from features.pages.institute_page import InstitutePage

@given('the Super Admin is logged in')
def step_login(context):
    # Navigate to the login page
    context.driver.get(context.base_url)

    # Enter username and password
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[1]/div/input').send_keys(utils.config.USER_NAME)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[2]/div[2]/div/input').send_keys(utils.config.PASSWORD)
    context.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div[3]/button').click()

    # Wait for the login to complete and for the "Create Institute" button to appear
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/button'))
    )

@when('the Super Admin clicks on "Create Institute" button')
def step_click_create_institute(context):
    # Locate and click the "Create Institute" button
    create_institute_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/button'))
    )
    create_institute_button.click()

@when('fills in the institute details')
def step_fill_institute_details(context):
    # Initialize the InstitutePage class
    institute_page = InstitutePage(context.driver)
    institute_page.fill_institute_details()

@when('submits the form')
def step_submit_form(context):
    # Initialize the InstitutePage class
    institute_page = InstitutePage(context.driver)
    institute_page.submit_form()

    # Wait for the page to load and verify redirection
    institute_page.wait_for_institute_creation()

@then('the new educational institute should be created successfully')
def step_verify_institute_creation(context):
    time.sleep(3)  # Optional, just in case there is any delay

    # Initialize the InstitutePage class
    institute_page = InstitutePage(context.driver)

    # Get the current URL and verify it contains 'institutes' and 'metrics'
    current_url = institute_page.get_current_url()
    assert "institutes" in current_url, f"URL does not contain 'institutes': {current_url}"
    assert "metrics" in current_url, f"URL does not contain 'metrics': {current_url}"

    # Optionally, verify the success message if needed
    success_message = institute_page.get_success_message()
    if success_message:
        assert "Institute created successfully" in success_message, "Institute creation failed!"
    else:
        print("Success message verification failed")

    print("Test Passed: New educational institute successfully created, and redirected to the correct URL.")
