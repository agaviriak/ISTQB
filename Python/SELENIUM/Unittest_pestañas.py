import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_ventana(self):
        driver=self.driver
        driver.get("https://google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://eltiempo.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
        
        


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




