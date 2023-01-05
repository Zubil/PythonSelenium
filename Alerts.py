from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button').click()

time.sleep(5)

alert_obj = driver.switch_to.alert
alert_obj.accept()
#alert_obj.dismiss()