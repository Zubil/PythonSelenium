from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)

driver.save_screenshot("C:\Screenshot\pic.png")

time.sleep(3)
driver.get_screenshot_as_file("C:\Screenshot\pic2.png")
