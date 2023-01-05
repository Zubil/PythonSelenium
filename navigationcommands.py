
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("http://newtours.demouat.com/")
time.sleep(5)
print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)

driver.back()

print(driver.title)
time.sleep(5)

driver.forward()

time.sleep(5)
print(driver.title)
