from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()
    page = context.new_page()

    # Username variable
    user_name = "symon.storozhenko"  # Name of the Udemy instructor :-)

    # Set the default timeout at the page level (similar to implicit wait)
    page.set_default_timeout(30000)  # 30 seconds timeout set

    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    page.wait_for_load_state(state="networkidle")  # This is like a wait statement in Playwright

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(f"{user_name}@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    page.wait_for_load_state(state="networkidle")

    # Assertion - Log In button should be hidden after successful login
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()

    # Navigate to the My Orders section
    page.get_by_label(f"{user_name} account menu").click()
    page.get_by_role("link", name="My Orders").click()

    # Assertion - username should be displayed
    expect(page.get_by_text(f"{user_name}", exact=True)).to_be_visible()

    # Chaining of locators
    product = page.get_by_text('$85').first.locator('xpath=../../../../..//h3').text_content()
    assert product != 'Socks'

    # Using the all() function to get a list of all webelements (similar to 'findElements')
    list_of_links = page.get_by_role("link").all()
    for link in list_of_links:
        if link.text_content() == '$85':
            assert 'socks' not in link.text_content().lower()

    # Just to print a message at the end of a successful run
    print("Test Run Completed")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
