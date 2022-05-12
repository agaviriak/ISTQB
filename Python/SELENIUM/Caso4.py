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
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/bootstrap-modal")
        time.sleep(5)
        #CASO1
        mensaje1=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[1]/div[2]/p/strong").text
        boton=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[1]/div[2]/button")
        boton.click()
        time.sleep(2)
        #Cambio al Modal       
        driver.switch_to_active_element
        mensaje2=driver.find_element_by_xpath("//*[@id='single-modal']/div/div[2]").text

        if mensaje1==mensaje2:
            print("CASO1---------------------")
            print("Prueba Exitosa!!!... Los Mensajes son Iguales.")
            print("Modal Aceptado")
            print("Mensaje de Página: "+ mensaje1)
            print("Mensaje de Alerta: "+ mensaje2)
        else:
            print("CASO1---------------------")
            print("Prueba Fallida!!!... Los Mensajes son Distintos.")
            print("Modal Rechazado")
            print("Mensaje de Página: "+ mensaje1)
            print("Mensaje de Alerta: "+ mensaje2)
        
        #CASO2        
        driver.get("https://jesuskinto.github.io/selenium-python-testing-page/#/bootstrap-modal")
        boton2=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/button[1]")
        boton2.click()

        #Cambio al Modal       
        driver.switch_to_active_element
        nombre="Alberto"
        apellido="Gaviria"
        email="miemail@email.com"
        f_nombre=driver.find_element_by_xpath("//*[@id='formPlaintextFirstName']")
        f_nombre.send_keys(nombre)
        f_apellido=driver.find_element_by_xpath("//*[@id='formPlaintextLastname']")
        f_apellido.send_keys(apellido)
        f_email=driver.find_element_by_xpath("//*[@id='formPlaintextEmail']")
        f_email.send_keys(email)
        #Grabar datos del formulario a la página
        driver.find_element_by_xpath("//*[@id='form-modal']/div/div[3]/button[2]").click()
        time.sleep(3)
        
        #Verificar datos guardados en la página
        p_nombre=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/ul[2]/li[1]/strong").text
        p_apellido=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/ul[2]/li[2]/strong").text
        p_email=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/ul[2]/li[3]/strong").text
        if (nombre==p_nombre and apellido==p_apellido and email==p_email):
            print("CASO2---------------------")
            print("Prueba Exitosa!!!... Los Datos son Iguales.")
            print("Modal Aceptado")
            print("Nombre: "+ nombre + " es igual a " + p_nombre)
            print("Apellido: "+ apellido + " es igual a " + p_apellido)
            print("Email: "+ email + " es igual a " + p_email)
            
        else:
            print("CASO2---------------------")
            print("Prueba Fallida!!!... Los datos son Distintos.")
            print("Modal Rechazado")
            print("Nombre: "+ nombre + " es distinto a " + p_nombre)
            print("Apellido: "+ apellido + " es distinto a " + p_apellido)
            print("Email: "+ email + " es distinto a " + p_email)
        
        #CASO3: Borrado de datos de la página  
        boton2=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/button[2]")
        boton2.click()
        p_nombre=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/ul[2]/li[1]/strong").text
        p_apellido=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/ul[2]/li[2]/strong").text
        p_email=driver.find_element_by_xpath("//*[@id='bootstrap-modals']/div[2]/div[2]/ul[2]/li[3]/strong").text
        if (p_nombre=="" and p_apellido=="" and p_email==""):
            print("CASO3---------------------")
            print("Prueba Exitosa!!!... Los Datos fueron limpiados...")          
        else:
            print("CASO3---------------------")
            print("Prueba Fallida!!!... Los Datos no fueron limpiados...")
   
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
