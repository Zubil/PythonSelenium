from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# select an option from dropdown

element=driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)

drp.select_by_visible_text('Morning')

time.sleep(5)

drp.select_by_index(2)

time.sleep(5)

drp.select_by_value("Radio-2")

# Count number of options

print(len(drp.options))

# Capture all the options and print them as outputs

all_options=drp.options

for option in all_options:
    print(option.text)
