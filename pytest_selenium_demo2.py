import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


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
    driver.get("https://trytestingthis.netlify.app/index.html")
    firstName = driver.find_element(By.XPATH, "//input[@id='uname']")
    lastName = driver.find_element(By.XPATH, "//input[@id='pwd']")
    submitBtn = driver.find_element(By.XPATH, "//input[@value='Login']")
    firstName.send_keys(username)
    lastName.send_keys(password)
    submitBtn.click()
    time.sleep(2)
    assert "Successful" in driver.page_source
