
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.current_url)
print(driver.title)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#driver.close() #c loses focused browser

driver.quit() # closes all the brosers