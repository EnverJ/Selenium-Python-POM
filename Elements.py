import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# https://pypi.org/project/webdriver-manager/
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://google.com")
# googleSearchBox = driver.find_element(By.ID, "APjFqb")
# googleSearchBox.send_keys("Automation")
# time.sleep(2)
# searchBtn = driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
# # searchBtn.click()
# searchBtn.send_keys(Keys.RETURN)
# time.sleep(2)

driver.get("https://trytestingthis.netlify.app/index.html")
firstName = driver.find_element(By.ID, "fname")
lastName = driver.find_element(By.ID, "lname")
submitBtn = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
firstName.send_keys("Auto")
lastName.send_keys("nation")
submitBtn.click()
time.sleep(2)
