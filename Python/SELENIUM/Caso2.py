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
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/checkbox")
        time.sleep(5)
        #caso1
        checklist=driver.find_element_by_xpath("//*[@id='single-checkbox']")
        checklist.click()
        time.sleep(5)
        salida=driver.find_element_by_xpath("//*[@id='checkboxes']/div[1]/div[2]/div[2]/span").text
        if salida=="success":
            print("Prueba caso1: Single Checkbox Exitosa... Mensaje: " +  salida)
        else:
            print("Prueba caso1: Single Checkbox Fallida... Mensaje: " +  salida)
       
      
        #caso2
        boton_s=driver.find_element_by_xpath("//*[@id='checkboxes']/div[2]/div[2]/button")    
        sw=0
        if boton_s.text != "Check All":
            sw=1
        boton_s.send_keys(Keys.ENTER)
        if boton_s.text != "Uncheck All":
            sw=1
        check1=driver.find_element_by_xpath("//*[@id='checkboxes']/div[2]/div[2]/label[1]")    
        check1.click()
        if boton_s.text != "Check All":
            sw=1    
        if sw==0:
            print("Prueba 2 Exitosa.. ")
        else:
            print("Prueba 2 Fallida.. ")

        print("Sin ningun chequeo... Mensaje Botón: " + boton_s.text)
        time.sleep(3)
        boton_s.send_keys(Keys.ENTER)
        print("Presionando el Botón... Mensaje botón: "+ boton_s.text)
        check1=driver.find_element_by_xpath("//*[@id='checkboxes']/div[2]/div[2]/label[1]")    
        check1.click()
        print("Chequeando una Casilla... Mensaje botón: "+ boton_s.text)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

