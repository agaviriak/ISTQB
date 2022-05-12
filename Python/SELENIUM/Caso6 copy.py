import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as COND

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_casos(self):
        
        driver=self.driver
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/data-loading")
        time.sleep(5)
        #CASO DATA LOADING
        #lista=["WALL·E", "Interstellar", "Ratatouille"]
        casilla=driver.find_element_by_xpath("//*[@id='data-loading']/div/div[2]/div[3]/input")
        #for i in lista:
        i="WALL·E"
        casilla.send_keys(i)
        time.sleep(7)
        #peliculas=driver.find_elements_by_xpath("//*[@id='data-loading']/div/div[2]/div[4]/a")
        #for i in peliculas:
        #    print(i.text)

        try:
            peliculas=WebDriverWait(driver,10).until(
            COND.presence_of_all_elements_located         
            ((By.XPATH, "//*[@id='data-loading']/div/div[2]/div[4]/a"))
            )    
        finally:
            driver.quit()
            
        for i in peliculas:
                print(i.text)
                
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

