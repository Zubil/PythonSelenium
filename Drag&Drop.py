from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(3)

source_element=driver.find_element_by_xpath("//*[@id='box6']")

target_element=driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]")

action=ActionChains(driver)

action.drag_and_drop(source_element,target_element).perform()