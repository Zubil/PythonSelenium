from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)

driver.switch_to.frame(0)

driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:/Pictures/apple.jpg")