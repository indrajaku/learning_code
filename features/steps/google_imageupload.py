import os
import pdb
import time

from behave import given, then, when
from playwright.sync_api import sync_playwright


def initialize_browser():
    """Open Desktop|FSE application or a specific URL
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, timeout=8000)
    pw_context = browser.new_context().new_page()
    return pw_context


@given("Indraja is on google search page")
def google_page(context):
    """Open Desktop|FSE application or a specific UR

    """
    context.page = initialize_browser()
    context.page.goto("https://www.google.com/search?q=upload+image")
    context.page.wait_for_load_state("networkidle")


@when("she clicks on upload image icon")
def click_google_image(context):
    """Open Desktop|FSE application or a specific URL
    """
    context.page.locator("//div[@role='button' and @data-base-lens-url='https://lens.google.com']").click()


@when("she uploads the image")
def upload_image(context):
    with context.page.expect_file_chooser() as fc_info:
        context.page.locator("//span[text()='upload a file  ']").click()
    file_chooser = fc_info.value
    context.img_name = (os.listdir("sample_images/"))[0]
    file_chooser.set_files(f"sample_images/{context.img_name}")



@then("she saves tops {n} results")
def save_images(context,n):
    """Open Desktop|FSE application or a specific URL

    :param context: context object
    :type context: behave.runner.Context
    :param host: Application type or the specific URL
    :type host: str
    """
    context.page.wait_for_selector("//*[.='Visual matches']")
    context.page.wait_for_load_state("networkidle")
    similar_image = context.page.query_selector_all("//div[@class='G19kAf ENn9pd']")
    similar_image = similar_image[:int(n)]
    for index,image in enumerate(similar_image):
        image.screenshot(path=f'result_images/{context.img_name}_{index + 1}.png')



