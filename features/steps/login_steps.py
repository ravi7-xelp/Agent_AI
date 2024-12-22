import time

from behave import given, when, then
from pyexpat import features

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages import login_page


import utils.config
from features.pages.login_page import LoginPage


@given('the Super Admin is on the login page')
def step_impl(context):
    context.driver.get(utils.config.BASE_URL)  # URL for the login page
    context.login_page = LoginPage(context.driver)
    time.sleep(2)

@when('the Super Admin enters valid credentials')
def step_impl(context):
   context.login_page.enter_username(utils.config.USER_NAME)
   context.login_page.enter_password(utils.config.PASSWORD)
   context.login_page.click_login()
   time.sleep(2)

@when('the Super Admin should be redirected to the institutes page')
def step_impl(context):
    # Wait for the institutes page to load or perform any necessary actions
    WebDriverWait(context.driver, 10).until(
        EC.url_contains("/institutes")
    )
    current_url = context.driver.current_url
    assert "/institutes" in current_url, f"Expected URL to contain '/institutes', but got {current_url}"

@when('the user click on Logout')
def step_impl(context):
    context.login_page.log_out()

@then('Redirected to Login page')
def step_impl(context):
    current_url = context.driver.current_url
    expected_url = "https://devagentadmin.glcredentials.com/"
    assert expected_url in current_url, f"Expected URL to contain '{expected_url}', but got '{current_url}'"

@when('the Super Admin enters invalid credentials')
def step_impl(context):
   context.login_page.enter_username(utils.config.INVALID_USERNAME)
   context.login_page.enter_password(utils.config.INVALID_PASSWORD)
   context.login_page.click_login()

@then('the login should fail and an error message should be displayed')
def step_impl(context):
    try:
        error_message = context.driver.find_element(By.CSS_SELECTOR, '.grid.gap-1').text  # Update with actual selector
        assert "Error" in error_message, f"Expected error message, but got {error_message}"
    except NoSuchElementException:
        assert False, "Error message not found on the page"

    #context.driver.quit()


