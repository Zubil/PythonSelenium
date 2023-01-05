from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)

element=driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")

actions=ActionChains(driver)

actions.double_click(element).perform()