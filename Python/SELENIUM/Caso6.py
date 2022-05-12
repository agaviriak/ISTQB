import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_casos(self):
        driver=self.driver
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/data-loading")
        time.sleep(1)
        #CASO DATA LOADING
        lista=["WALL·E", "Interstellar", "Ratatouille"]
        lista2=[]
        sw=0
        for i in lista:
            driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/data-loading")
            casilla=driver.find_element_by_xpath("//*[@id='data-loading']/div/div[2]/div[3]/input")
            casilla.send_keys(i)
            time.sleep(3)
            peliculas=driver.find_elements_by_xpath("//*[@id='data-loading']/div/div[2]/div[4]/a")
            for y in peliculas:
                lista2.append(y.text)
            if i in lista2:
                print(i, " SI está en la lista!")
            else:
                print(i, " NO está en la lista!")
                sw=1
        if sw==0:
            print("RESUMEN EXITOSO: Todas las peliculas están listadas!")
        else:
            print("RESUMEN FALLIDO: NO Todas las peliculas están listadas!")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

