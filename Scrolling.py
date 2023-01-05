from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

time.sleep(3)


#1. Scroll Down by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#2. Scroll down page till element is visible
#flag=driver.find_element_by_xpath("//td[text()='India']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#3. How to scroll till the end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")