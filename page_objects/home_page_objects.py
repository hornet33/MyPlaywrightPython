class HomePage:

    def __init__(self, page):
        self.tag_line = page.get_by_text("Fashion You’ll Love")
        self.login = page.get_by_role("button", name="Log In")
        self.signup = page.get_by_test_id("signUp.switchToSignUp")
        self.login_email = page.get_by_role("button", name="Log in with Email")
        self.email_input = page.get_by_test_id("emailAuth").get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.login_submit = page.get_by_test_id("submit")
        self.my_orders = page.get_by_role("link", name="My Orders")
        self.logout = page.get_by_text("Log Out")
