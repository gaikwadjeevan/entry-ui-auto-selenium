from core.form_element import FormElement


class MyAccountPageEle:
    textbox_username_id = FormElement("ID", "username", "Username")
    textbox_password_id = FormElement("ID", "password", "Password")
    button_login_xpath = FormElement("XPATH", "//input[@name='login']", "Login")
    lnk_MyAccount = FormElement("XPATH", "//a[normalize-space()='My Account']", "MyAccount")
    link_Order = FormElement("LINK_TEXT", "Orders", "Orders")
