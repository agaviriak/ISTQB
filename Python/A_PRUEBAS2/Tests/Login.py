from selenium import webdriver
import time
import unittest
from Objetos_POM.Pagina_login import *
from Objetos_POM.PARAMETROS import datos

class casosdeprueba(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=datos.executable_path)
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get(datos.Page_test)
        time.sleep(1)
        login=login_page(self.driver)
        login.enter_username(datos.username)
        login.enter_password(datos.password)
        login.submit_click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
