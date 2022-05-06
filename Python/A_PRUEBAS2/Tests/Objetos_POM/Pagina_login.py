from Objetos_POM.PARAMETROS import datos

class login_page():

    #Constructor
    def __init__(self, driver):
        self.driverO=driver
        self.username_id=datos.username_id
        self.password_id=datos.password_id
        self.submit_id=datos.submit_id
    
    #Método Ingresar username 
    def enter_username(self, username):
        self.driverO.find_element_by_id(self.username_id).send_keys(username)

    #Método Ingresar password
    def enter_password(self, password):
        self.driverO.find_element_by_id(self.password_id).send_keys(password)

    #Método clickear botón
    def submit_click(self):
        self.driverO.find_element_by_id(self.submit_id).click()