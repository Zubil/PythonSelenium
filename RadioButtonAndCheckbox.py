from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Working with Radio Buttons

status=driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
print(status)
time.sleep(5) # Sleep for 5 seconds

driver.find_element_by_xpath("/html/body/form/div[2]/div[15]/table/tbody/tr[1]/td/label").click()

status=driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected()
print(status)


# Working with Check Boxes

driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_6").click()

status1=driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status1)

