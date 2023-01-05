from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")

driver.find_element_by_xpath("//*[@id='btnLogin']").click()

time.sleep(5)

admin=driver.find_element_by_xpath('//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]')
usermgnt=driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
usr=driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(usr).click().perform()