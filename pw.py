from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/search?q=google&oq=google&aqs=chrome..69i57.2697j0j2&sourceid=chrome&ie=UTF-8")
    page.get_by_role("link", name="Google Google https://google.com").click()
    page.locator(".a4bIc").click()
    page.get_by_role("combobox", name="Search").fill("ts")
    page.get_by_text("tsunami").click()
    page.get_by_role("link", name="Tsunami - Wikipedia Wikipedia https://en.wikipedia.org › wiki › Tsunami").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
