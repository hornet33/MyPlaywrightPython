import os
from playwright.sync_api import expect
from page_objects.home_page_objects import HomePage
import pytest

# To toggle between local/remote runs - there are two ways
# ------------ OPTION 1 ------------
# Save the password in a local file (here it is in utils/secrets.py)
# Then use a try/except block to check if os.environ returns a successful password (in case of Github secret)
# If not, initialize PASSWORD var to the local utils.secrets.PASSWORD value (in case of local run)
# This is to ensure that the script runs on both local as well as remote (Github actions) successfully.
# try:
#     PASSWORD = os.environ['PASSWORD']
# except KeyError:
#     import utils.secrets
#
#     PASSWORD = utils.secrets.PASSWORD
# ------------ OPTION 2 ------------
# Use a local env variable in the ".env" file
# Then a single os.environ statement will work in both local & remote runs
PASSWORD = os.environ['PASSWORD']

# Using a custom pytest marker 'smoke' for smoke tests in my suite
# To execute specific markers from CLI: pytest -m <nameOfMarker>
@pytest.mark.smoke
#  @pytest.mark.parametrize("email, password",
#                         [("symon.storozhenko@gmail.com", "test123"),
#                          pytest.param("invalidemail", "invalidpwd", marks=pytest.mark.xfail)])
# Instead of 1 parametrize function as shown above, we can stack them as follows:
@pytest.mark.parametrize("email",
                         ["symon.storozhenko@gmail.com",
                          pytest.param("invalidemail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password",
                         [PASSWORD,
                          pytest.param("invalidpwd", marks=pytest.mark.xfail)])
# Difference is the second "stacking" parametrize will run multiple combinations for the parameters defined
# Email1 with Pwd1, then Email1 with Pwd2, then Email2 with Pwd1, and finally Email2 with Pwd2
def test_login_run(set_up, email, password) -> None:
    page = set_up  # Getting the page instance from the set_up fixture in conftest.py

    # Initializing the home page object
    home_page = HomePage(page)

    # Username variable
    user_name = "symon.storozhenko"  # Name of the Udemy instructor :-)

    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    page.wait_for_load_state(state="networkidle")  # This is like a wait statement in Playwright

    home_page.login.click()
    home_page.signup.click()
    home_page.login_email.click()
    home_page.email_input.click()
    home_page.email_input.fill(email)
    home_page.email_input.press("Tab")
    home_page.password_input.fill(password)
    home_page.login_submit.click()

    page.wait_for_load_state(state="networkidle")

    # Assertion - Log In button should be hidden after successful login
    expect(home_page.login).to_be_hidden()

    # Chaining of locators
    product = page.get_by_text('$85').first.locator('xpath=../../../../..//h3').text_content()
    assert product != 'Socks'

    # Using the all() function to get a list of all webelements (similar to 'findElements')
    list_of_links = page.get_by_role("link").all()
    for link in list_of_links:
        print(link.text_content())
        if link.text_content() == '$85':
            assert 'socks' not in link.text_content().lower()

    # Navigate to the My Orders section
    page.get_by_label(f"{user_name} account menu").click()
    # page.get_by_role("link", name="My Orders").click()
    home_page.my_orders.click()

    # Assertion - username should be displayed
    expect(page.get_by_text(f"{user_name}", exact=True)).to_be_visible()

    # Logout
    page.get_by_label(f"{user_name} account menu").click()
    # page.get_by_text("Log Out").click()
    home_page.logout.click()

    # Just to print a message at the end of a successful run
    print("Test Run Completed")
    # ---------------------
