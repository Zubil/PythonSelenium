from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.expedia.com/")
