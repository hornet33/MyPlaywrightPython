from playwright.sync_api import expect
from page_objects.contact_us_objects import ContactUs
import pytest


# Using a custom pytest marker 'smoke' for smoke tests in my suite
# To execute specific markers from CLI: pytest -m <nameOfMarker>
@pytest.mark.smoke
def test_contact_us_run(set_up) -> None:
    page = set_up  # Getting the page instance from the set_up fixture in conftest.py

    # Initializing the page object
    contact_us_page = ContactUs(page)

    contact_us_page.navigate()
    page.wait_for_load_state(state="networkidle")  # This is like a wait statement in Playwright
    expect(contact_us_page.name_field).to_be_visible()
    contact_us_page.fill_form("Test", "Address", "abc@def.com", "1234567890",
                              "Test Sub", "This is a test message.")
    contact_us_page.submit_form()

    # Just to print a message at the end of a successful run
    print("Test Run Completed")
    # ---------------------


@pytest.mark.skip(reason="Skip demo only")  # This pytest annotation/marker is to skip this test during execution
def test_skip_demo() -> None:
    print("This will never be printed - just a pytest mark.skip demo function that doesn't do anything")


@pytest.mark.xfail(reason="XFail demo only")  # This pytest marker is to mark tests which are expected to fail
def test_xfail_demo(set_up) -> None:
    page = set_up  # Getting the page instance from the set_up fixture in conftest.py

    # Initializing the page object
    contact_us_page = ContactUs(page)
    contact_us_page.navigate()
    page.wait_for_load_state(state="networkidle")  # This is like a wait statement in Playwright
    expect(contact_us_page.name_field).to_be_hidden()  # Expect() will fail
