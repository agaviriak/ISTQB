import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_caso1(self):
        driver=self.driver
        driver.get("https://google.com")
        self.assertIn("Google", driver.title)
        buscador=driver.find_element_by_name("q")
        buscador.send_keys("selenium")
        buscador.send_keys(Keys.RETURN)
        time.sleep(15)
        assert "No se encontró el elemento" not in driver.page_source

    #def tearDown(self):
    #    self.driver.close()

if __name__ == '__main__':
    unittest.main()




