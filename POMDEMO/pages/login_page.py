from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_txt = (By.XPATH, "//input[@id='uname']")
        self.password_txt = (By.XPATH, "//input[@id='pwd']")
        self.submitBtn = (By.XPATH, "//input[@value='Login']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_txt).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_txt).send_keys(password)

    def click_submitBtn(self):
        self.driver.find_element(*self.submitBtn).click()
