import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_caso1(self):
        driver=self.driver
        driver.get("https://sugarcrm.com/au/request-demo")
        
        # Get all the elements available with tag name 'p'
        elements = driver.find_elements_by_name("firstname")
        elements.send_keys("Alberto")
                       
        for i in elements:
            print(i.text)
            print("hola mundo")
  
                
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
