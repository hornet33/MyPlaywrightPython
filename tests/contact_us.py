from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.contact_us_objects import ContactUs


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    # Initializing the page object
    contact_us_page = ContactUs(page)

    contact_us_page.navigate()

    expect(contact_us_page.name_field).to_be_visible()

    contact_us_page.submit_form("Test")

    # Just to print a message at the end of a successful run
    print("Test Run Completed")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
