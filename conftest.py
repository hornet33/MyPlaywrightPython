# This Python file MUST be named "conftest.py" for Pytest to recognize it as a test config file
# It will contain our fixtures for setup and teardown
import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def set_up(browser):
    # browser = playwright.chromium.launch(headless=False, slow_mo=10)
    context = browser.new_context()
    page = context.new_page()
    yield page

    page.close()
