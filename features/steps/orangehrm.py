import time

from behave import given, then, when
from playwright.sync_api import sync_playwright

Locators = {
    "USERNAME": "xpath=//input[@placeholder='Username']",
    "PASSWORD": "//input[@placeholder='Password']",
    "LOGIN": "//button[@type='submit']",
    "PIM_BUTTON": "//span[contains(@class, 'oxd-main-menu-item--name') and text()='PIM']",
    "ADD": "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']",
    "SAVE": "//button[@type='submit']",
    "FIRST_NAME": "//input[@name='firstName']",
    "MIDDLE_NAME": "//input[@name='middleName']",
    "LAST_NAME": "//input[@name='lastName']",
    "NOTIFICATION": "//p[contains(.,'Successfully')]"
}

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


def initialize_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, timeout=8000)
    pw_context = browser.new_context().new_page()
    return pw_context


@given("the user logs in to the application")
def login_browser(context):
    context.page = initialize_browser()
    context.page.goto(URL)
    for data in context.table:
        context.page.locator(Locators["USERNAME"]).fill(data["username"])
        context.page.locator(Locators["PASSWORD"]).fill(data["password"])
        context.page.locator(Locators["LOGIN"]).click()


@when("fill the employee details")
def employee_details(context):
    context.page.locator(Locators["PIM_BUTTON"]).click()
    context.page.locator(Locators["ADD"]).click()
    for data in context.table:
        context.page.locator(Locators["FIRST_NAME"]).fill(data["firstname"])
        context.page.locator(Locators["MIDDLE_NAME"]).fill(data["middlename"])
        context.page.locator(Locators["LAST_NAME"]).fill(data["lastname"])

    context.page.locator(Locators["SAVE"]).click(timeout=10000)
    time.sleep(2)


@then("the user details are recorded successfully")
def notification_status(context):
    status = context.page.is_visible(Locators["NOTIFICATION"])
    assert status is True
