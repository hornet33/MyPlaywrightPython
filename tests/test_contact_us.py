from playwright.sync_api import Playwright, expect
from page_objects.contact_us_objects import ContactUs
import pytest


def test_contact_us_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()

    # Initializing the page object
    contact_us_page = ContactUs(page)

    contact_us_page.navigate()
    expect(contact_us_page.name_field).to_be_visible()
    contact_us_page.fill_form("Test", "Address", "abc@def.com", "1234567890",
                              "Test Sub", "This is a test message.")
    contact_us_page.submit_form()

    # Just to print a message at the end of a successful run
    print("Test Run Completed")
    # ---------------------
    context.close()
    browser.close()


@pytest.mark.skip  # This is a pytest annotation/marker to skip this test during execution
def test_demo_run(playwright: Playwright) -> None:
    print("This is just a pytest mark.skip demo function - doesn't do anything")
