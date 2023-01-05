from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(3)

# Capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))

print(cookies)

# Adding new cookie to the browser

cookie={'name':'MyCookie','value':'123456789'}
driver.add_cookie(cookie)


# Capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))

print(cookies)


# Deleting cookie
driver.delete_cookie('MyCookie')

# Capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))

print(cookies)


# Delete aal the cookies
driver.delete_all_cookies()


# Capture all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))

print(cookies)
