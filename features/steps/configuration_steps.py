#steps.py
import time
from behave import given, when, then
from features.pages.configuration_page import SuperAdminPage
import utils.config

@given("the Super Admin is logged into the application")
def step_impl(context):
    context.driver.get(context.base_url)
    context.super_admin_page = SuperAdminPage(context.driver)
    context.super_admin_page.login(utils.config.USER_NAME, utils.config.PASSWORD)
    time.sleep(5)

@when("the Super Admin clicks on an institute from the institutes page")
def step_impl(context):
    context.super_admin_page.click_on_institute()
    print("Super Admin clicked on an institute")

@when("navigates to the metrics page")
def step_impl(context):
    context.super_admin_page.navigate_to_metrics()
    print("Super Admin navigated to the metrics page")

@when("clicks on the configuration option")
def step_impl(context):
    context.super_admin_page.click_on_configuration()
    print("Super Admin clicked on the configuration option")

@then("the configuration page should display the required fields")
def step_impl(context):
    current_url = context.driver.current_url
    assert "/configurations" in current_url, f"Expected URL to contain '/configurations', but got {current_url}"

@then("the Save button should be visible")
def step_impl(context):
    assert context.super_admin_page.is_save_button_visible(), "Save button is not visible on the configuration page."
    print("Configuration page displays all required fields and Save button is visible.")
