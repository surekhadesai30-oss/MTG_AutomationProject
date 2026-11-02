from playwright.sync_api import Page,expect
import pytest
class LoginPage:
    def __init__(self,page:Page):
        self.page= page

        self.email_txt_box=self.page.locator("#email")
        self.password_txt_box=self.page.locator("#passInput")
        self.signInPageLogo = self.page.get_by_role("img", name="logo")
        self.signInButton=self.page.get_by_role("button", name="Sign in")

    def verify_loginpage_logo(self):
        logostatus = self.signInPageLogo.is_displayed()
        return logostatus

    def enter_email(self,email:str):
        try:
            self.email_txt_box.fill(email)
        except Exception as e:
            print(f"Exception occured while entering email:{e}")
            raise

    def enter_password(self,password:str):
        try:
            self.password_txt_box.fill(password)
        except Exception as e:
            print(f"Exception occured while entering password:{e}")
            raise
    def click_SignIn(self):
        try:
            self.signInButton.click()
        except Exception as e:
            print(f"Exception occured while clicking SignIn button:{e}")









