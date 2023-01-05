from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# How to verify how many input boxes in a web page

inputboxes=driver.find_elements(By.CLASS_NAME,"text_field")
print(len(inputboxes))

# How to find status of the element

status=driver.find_element_by_id('RESULT_TextField-1').is_displayed()
print("Status is present:",status)

# How to find element is enabled or not

enabled=driver.find_element_by_id('RESULT_TextField-1').is_enabled()
print("Enabled or Not:",enabled)




# How to provide value into textbox


driver.find_element(By.ID,'RESULT_TextField-1').send_keys("Zubil")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Chhokra")

driver.find_element_by_id('RESULT_TextField-3').send_keys("3165965753")
