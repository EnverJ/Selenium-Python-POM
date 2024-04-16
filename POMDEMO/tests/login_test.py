import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POMDEMO.pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("username,password", [
    ("test", "test"),
    ("test", "test"),
    ("test", "test")
])
def test_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/index.html")
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_submitBtn()
    time.sleep(2)
    assert "Successful" in driver.page_source
