from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

Chromeoptions=Options()
Chromeoptions.add_experimental_option("prefs", {"download.default_directory": "C:\Zubil"})


driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe",options=Chromeoptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(3)


# Download text File

driver.find_element_by_id("textbox").send_keys("Testing1244")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

