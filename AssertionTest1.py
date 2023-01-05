import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def Test(self):
        driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        driver.get("https://www.google.com/")
        webpage_title=driver.titles

    #Assert equal
        self.assertEqual("Google",webpage_title,"Error")
        self.assertNotEqual("Google123",webpage_title=driver.title)


if __name__ == "__main__":
   unittest.main()