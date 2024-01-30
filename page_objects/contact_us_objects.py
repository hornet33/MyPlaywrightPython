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

    def fill_form(self, name, address, email, phone, subject, msg):
        self.name_field.fill(name)
        self.address_field.fill(address)
        self.email_field.fill(email)
        self.phone_field.fill(phone)
        self.subject_field.fill(subject)
        self.msg_field.fill(msg)

    def submit_form(self):
        self.submit_btn.click()
