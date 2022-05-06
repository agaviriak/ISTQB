import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_xpath(self):
        driver=self.driver
        driver.get("https://google.com")
        #time.sleep(5)
        xpath=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        xpath.send_keys("energia", Keys.ENTER)
        time.sleep(17)
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




