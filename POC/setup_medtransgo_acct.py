from openpyxl.worksheet import page
from playwright.sync_api import Page, expect
class MtgCustAccountSetUp:
    def __init__(self):
        self.page= page

        self.accHeading=self.page.get_by_role("heading", name="Set Up your MedTrans Go AccountJoin us to serve you")

    def verify_accHeading(self):
        heading= self.accHeading.is_displayed()