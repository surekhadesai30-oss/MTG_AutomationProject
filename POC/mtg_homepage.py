from playwright.sync_api import Page, expect
class HomePage:
    def __init__(self,page:Page):
        self.page= page

        self.SignInlink=self.page.locator("p:has-text('Sign In')")
        self.customerLoginLink=self.page.locator(":text-is('Customer')")
        self.signInPageLogo=self.page.get_by_role("img", name="logo")

    def get_homePage_title(self)-> str:
        title=self.page.title()
        return title()

    def click_signInlink(self):
        self.SignInlink.click()

    def click_CustomerLogin(self):
        try:
            self.customerLoginLink.click()
        except  Exception as e:
            print(f"Exception occured while Customer login):{e}")
            raise 