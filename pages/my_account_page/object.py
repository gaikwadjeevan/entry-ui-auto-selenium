import time

from core.data_classes import Config
from core.base_page import BaseScreen
from pages.my_account_page.elements import MyAccountPageEle
from assertpy import assert_that


class MyAccountPage(BaseScreen):
    # username = "jeevangaikwad2@gmail.com"
    # password = "Test@123456#"

    def __init__(self, config: Config):
        super().__init__(config)
        self.resource_url = "my-account"
        self.myAccount_page_ele = MyAccountPageEle

    # Page actions

    def open(self):
        self.log.info(f"Open the {self.url} page")
        self.driver.get(self.url)

    def setUsername(self, username):
        self.log.info(f"Enter the {self.myAccount_page_ele.textbox_username_id.name}")
        self.se_helper.get_element(self.myAccount_page_ele.textbox_username_id).clear()
        self.se_helper.get_element(self.myAccount_page_ele.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.log.info(f"Enter the {self.myAccount_page_ele.textbox_password_id.name}")
        self.se_helper.get_element(self.myAccount_page_ele.textbox_password_id).clear()
        self.se_helper.get_element(self.myAccount_page_ele.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.log.info(f"Click on the {self.myAccount_page_ele.button_login_xpath.name} button")
        self.se_helper.get_element(self.myAccount_page_ele.button_login_xpath).click()
        time.sleep(5)

    def select_Orders(self):
        self.log.info(f"Click the {self.myAccount_page_ele.link_Order.name} link to check the placed orders")
        self.se_helper.get_element(self.myAccount_page_ele.link_Order).click()

    # Page assertions

    def verify_MyAccountPage_title(self):
        self.log.info("Verify the My Account Page title")
        title = self.driver.title
        assert_that(title).contains("My Account")
