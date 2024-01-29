class ContactUs:

    def __init__(self, page):
        self.page = page
        self.name_field = page.get_by_placeholder("Enter your name")
        self.address_field = page.get_by_placeholder("Enter your address")
        self.email_field = page.get_by_placeholder("Enter your email")
        self.phone_field = page.get_by_placeholder("Enter your phone number")
        self.subject_field = page.get_by_placeholder("Type the subject")
        self.msg_field = page.get_by_placeholder("Type your message here...")
        self.submit_btn = page.get_by_test_id("buttonElement")

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, text):
        self.name_field.fill("Test Name")
        self.address_field.fill("Test Address")
        self.email_field.fill("abc@test.com")
        self.phone_field.fill("1234567890")
        self.subject_field.fill("Test Subject")
        self.msg_field.fill("Test Message 123")
        self.submit_btn.click()
