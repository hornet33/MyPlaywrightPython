from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Set the default timeout at the page level (similar to implicit wait)
    page.set_default_timeout(30000)

    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    page.wait_for_load_state(state="networkidle")  # This is like a wait statement in Playwright

    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("symon.storozhenko@gmail.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("test123")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    page.wait_for_load_state(state="networkidle")

    # Assertion - Log In button should be hidden after successful login
    expect(page.get_by_role("button", name="Log In")).to_be_hidden()

    # Navigate to the My Orders section
    page.get_by_label("symon.storozhenko account menu").click()
    page.get_by_role("link", name="My Orders").click()

    # Just to print a message at the end of a successful run
    print("Test Run Completed")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
