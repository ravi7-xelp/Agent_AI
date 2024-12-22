from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """Setup before running all tests."""
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()

    # Check if running in CI environment
    if os.getenv('CI'):
        # Add headless argument for CI environment
        chrome_options.add_argument('--headless')
        # Add no-sandbox argument for CI environment
        chrome_options.add_argument('--no-sandbox')
        # Add disable-dev-shm-usage argument for CI environment
        chrome_options.add_argument('--disable-dev-shm-usage')
    else:
        # Maximize window for local environment
        chrome_options.add_argument('--start-maximized')

    # Initialize the Chrome driver with options
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    context.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    context.base_url = "https://devagentadmin.glcredentials.com/"  # Replace with your app's URL
    print("Before All: Browser session started.")

def before_feature(context, feature):
    """Setup before each feature file."""
    print(f"Starting feature: {feature.name}")
    # Navigate to the base URL before starting each feature
    context.driver.get(context.base_url)

def before_scenario(context, scenario):
    """Setup before each scenario."""
    print(f"Starting scenario: {scenario.name}")
    # Clear cookies and refresh the browser session for a clean slate
    context.driver.delete_all_cookies()
    context.driver.refresh()

def before_step(context, step):
    """Log steps being executed."""
    print(f"Executing step: {step.name}")

def after_step(context, step):
    """Check the result of each step."""
    if step.status == "failed":
        # Capture a screenshot on failure for debugging
        context.driver.save_screenshot(f"screenshots/{step.name.replace(' ', '_')}.png")
    print(f"Step status: {step.status}")

def after_scenario(context, scenario):
    """Cleanup after each scenario."""
    print(f"Finished scenario: {scenario.name}")
    # Clear session data and refresh for the next scenario
    context.driver.delete_all_cookies()
    context.driver.execute_script("window.localStorage.clear();")
    context.driver.execute_script("window.sessionStorage.clear();")
    context.driver.refresh()

def after_feature(context, feature):
    """Cleanup after each feature."""
    print(f"Finished feature: {feature.name}")

def after_all(context):
    """Cleanup after all tests."""
    # Close the browser session at the end of all tests
    context.driver.quit()
    print("After All: Browser session closed.")
