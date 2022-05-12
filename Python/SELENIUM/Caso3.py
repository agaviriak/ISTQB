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
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/javascript-alert")
        time.sleep(5)
    
        mensaje1=driver.find_element_by_xpath("//*[@id='javascript-alert']/div/div[2]/p/strong").text
        boton=driver.find_element_by_xpath("//*[@id='javascript-alert']/div/div[2]/button")
        boton.click()
        time.sleep(2)
        
        alerta = driver.switch_to.alert
        mensaje2= alerta.text
        alerta.accept()
        if mensaje1==mensaje2:
            print("Prueba Exitosa!!!... Los Mensajes son Iguales.")
            print("Alerta Aceptada")
            print("Mensaje de Página: "+ mensaje1)
            print("Mensaje de Alerta: "+ mensaje2)
        else:
            print("Prueba Fallida!!!... Los Mensajes son Distintos.")
            print("Alerta Rechazada")
            print("Mensaje de Página: "+ mensaje1)
            print("Mensaje de Alerta: "+ mensaje2)
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
