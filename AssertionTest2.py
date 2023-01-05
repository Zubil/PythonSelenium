import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        driver.get("https://www.google.com/")

        titleweb=driver.title

        self.assertTrue(titleweb == "Google")
