import unittest
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

class casosdeprueba(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")

    def test_casos(self):
        
        driver=self.driver
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/jquery-date")
        time.sleep(5)
        #CASO1: calendario
        calendario=driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/div/button[2]")
        calendario.click()
        dia_i=driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/span/div/div/div[2]/div/div/div/div[2]/button[8]/abbr")
        dia_i.click()
        dia_f=driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/div[2]/span/div/div/div[2]/div/div/div/div[2]/button[12]/abbr")
        dia_f.click()
        time.sleep(12)
        #Fechas seleccionadas
        dia_ip=driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/ul[2]/li[1]/strong").text
        dia_fp=driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/div/div[2]/ul[2]/li[2]/strong").text
        #Formatear fechas del calendario
        fecha_i=datetime.strptime(dia_ip, '%a %b %d %Y')
        fecha_f=datetime.strptime(dia_fp, '%a %b %d %Y')
        
        if (fecha_f>=fecha_i):
            print("Prueba Exitosa------------------------")
            print("Fecha Inicial del calendario: "+dia_ip)
            print("Fecha Final del Calendario: "+dia_fp)
            print("Fecha Inicial Formateada datatime para comprobación: ", fecha_i)
            print("Fecha Final Formateada datatime para comprobación: ", fecha_f)
        else:
            print("prueba Fallida------------------")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
