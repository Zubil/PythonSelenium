from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.facebook.com/")

driver.implicitly_wait(10)

assert "ce" in driver.title

driver.find_element_by_name("email").send_keys("user")
driver.find_element_by_name("pass").send_keys("user")

driver.find_element_by_name("login").click()