from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://www.facebook.com/")

ele=driver.find_element_by_name("email")
print(ele.is_displayed())
print(ele.is_enabled())

ele2=driver.find_element_by_name("pass")
print(ele2.is_displayed())
print(ele2.is_enabled())


ele.send_keys("user")
ele2.send_keys("user")


driver.find_element_by_name("login").click()

