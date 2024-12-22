from behave import given, when, then
from features.pages.add_admin_page import AdminPage

@given("the Super Admin is logged into the application with valid credentials")
def step_impl(context):
    context.admin_page = AdminPage(context.driver, context.base_url)
    context.admin_page.login()

@when("the Super Admin select and click institute from the institutes page")
def step_impl(context):
    context.admin_page.select_institute()

@when("admin navigates to the metrics page")
def step_impl(context):
    context.admin_page.verify_metrics_page_navigation()

@when("clicks on the settings")
def step_impl(context):
    context.admin_page.click_settings()

@when("click on the create admin button")
def step_impl(context):
    context.admin_page.click_create_admin()

@then("fill create and form and submit")
def step_impl(context):
    context.admin_page.fill_create_admin_form()
