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
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/simple-form")
        time.sleep(5)
        #caso1.11
        mensaje="Hola mundo... @123 #*"
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
    
        #caso2
        Nro1=6
        Nro2=9
        time.sleep(5)
        casilla1=driver.find_element_by_xpath("//*[@id='sum1']")
        casilla2=driver.find_element_by_xpath("//*[@id='sum2']")    
        boton_s=driver.find_element_by_xpath("//*[@id='simple-form']/div[2]/div[2]/button")    
        casilla1.send_keys(Nro1)
        casilla2.send_keys(Nro2)
        boton_s.send_keys(Keys.ENTER)
        time.sleep(5)
        salida2=driver.find_element_by_xpath("//*[@id='simple-form']/div[2]/div[2]/div[2]/span").text
        if str(Nro1+Nro2)==salida2:
            print("Prueba caso2: Sum of Input exitosa... Sumatoria: " +  salida2)
        else:
            print("Prueba caso2: Sum of Input Fallida... Sumatoria: " +  salida2)
        
       
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

