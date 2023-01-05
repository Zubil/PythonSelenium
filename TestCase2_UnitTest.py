import unittest
from selenium import webdriver

class SearchEnginetest(unittest.TestCase):
    def test_Goggle(self):
        self.driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Page title is" +self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Page title is" + self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()