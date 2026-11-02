from idlelib import config

from playwright.sync_api import expect

from POC.mtg_homepage import HomePage
from POC.mtg_LoginPage import LoginPage
from utilities.randomDataUtills import RandomDataUtills
from config import Config
from POC.setup_medtransgo_acct import MtgCustAccountSetUp
def test_mtg_homepage(page):
    homepage=HomePage(page)
    loginpage=LoginPage(page)


    #homepage.customerLoginLink.click()
    #homepage.customerLoginLink.click()
    #invalid data
    '''
    random_data=RandomDataUtills()
    email=random_data.get_random_email_id()
    password=random_data.get_random_pwd()
    '''
    loginpage.enter_email(Config.email)
    LoginPage.enter_password((Config.password))
    loginpage.signInButton.click()

    custaccSetup = MtgCustAccountSetUp()
    heading=custaccSetup.verify_accHeading()
    expect(heading).to_have_text("Set Up your MedTrans Go AccountJoin us to serve you")

