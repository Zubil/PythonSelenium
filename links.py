from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/")

#How many links present in a page

links=driver.find_elements(By.TAG_NAME,"a")

print("Number of links present",len(links))

# How to print all the links present
#for link in links:
#    print(link.text)


time.sleep(5)
driver.find_element(By.LINK_TEXT,"No, thanks!").click()

time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"Input ").click()