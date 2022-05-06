import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_caso1(self):
        mensaje="Hola mundo... @123 #*"
        driver=self.driver
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/simple-form")
        time.sleep(5)
        casilla=driver.find_element_by_xpath("//*[@id='user-message']")
        casilla.send_keys(mensaje)
        boton=driver.find_element_by_xpath("//*[@id='simple-form']/div[1]/div[2]/button")
        boton.click()
        time.sleep(5)
        salida=driver.find_element_by_xpath("//*[@id='simple-form']/div[1]/div[2]/div[2]/span").text
        if mensaje==salida:
            print("Prueba caso1: Input message exitosa... Mensaje: " +  salida)
        else:
            print("Prueba caso1: Input message Fallida... Mensaje: " +  salida)
        

    def test_caso2(self):
        Nro1=6
        Nro2=9
        driver=self.driver
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/simple-form")
        time.sleep(5)
        casilla1=driver.find_element_by_xpath("//*[@id='sum1']")
        casilla2=driver.find_element_by_xpath("//*[@id='sum2']")    
        boton_s=driver.find_element_by_xpath("//*[@id='simple-form']/div[2]/div[2]/button")    
        
        casilla1.send_keys(Nro1)
        casilla2.send_keys(Nro2)
        boton_s.click()
        time.sleep(5)
        salida=driver.find_element_by_xpath("//*[@id='simple-form']/div[2]/div[2]/div[2]/span").text
        if str(Nro1+Nro2)==salida:
            print("Prueba caso2: Sum of Input exitosa... Mensaje: " +  salida)
        else:
            print("Prueba caso2: Sum of Input Fallida... Mensaje: " +  salida)

        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

