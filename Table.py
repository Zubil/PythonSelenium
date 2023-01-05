from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://sqengineer.com/practice-sites/practice-tables-selenium/")

time.sleep(5)

rows=len(driver.find_elements_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/main[1]/article[1]/div[1]/table[1]/tbody[1]/tr"))
cols=len(driver.find_elements_by_xpath('//*[@id="table1"]/tbody/tr[1]/th'))

print(rows)
print(cols)

print("Product"+"            "+"Article"+"              "+"Price")

for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/main/article/div/table[1]/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end='            ')
    print()
