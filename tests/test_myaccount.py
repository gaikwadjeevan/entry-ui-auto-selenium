from pytest import mark
from core.data_classes import Config
from core.readProperties import readConfig
from pages.my_account_page.object import MyAccountPage


# Scenario:
# 1. Go to “http://practice.automationtesting.in/”
# 2. Click on MyAccount Page
# 3. And Click on Orders link to see the orders product
# 4. Verify the MyAccount page title


@mark.myaccount
def test_myaccount(config: Config):
    username = readConfig.getUsername()
    password = readConfig.getPassword()
    config.log.info("Test the Login functionality and Orders items ")
    my_account_page = MyAccountPage(config)
    my_account_page.open()
    my_account_page.setUsername(username)
    my_account_page.setPassword(password)
    my_account_page.clickLogin()
    my_account_page.select_Orders()
    my_account_page.verify_MyAccountPage_title()
