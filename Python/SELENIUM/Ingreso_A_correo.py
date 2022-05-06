from selenium import webdriver
from selenium.webdriver.chrome import options
#from selenium.webdriver.chrome.options import Options
#option=Options()
#option.add_experimental_option("debuggerAddress","localhost:9222")
#driver = webdriver.Chrome(options=option)
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")
session=driver.session_id
print(session)
driver.get("https://gmail.com")

usuario=driver.find_element_by_id("identifierId")
usuario.send_keys("gaviria.alberto@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(4)
print(usuario)
#for i in usuario:
#    print(i.text)
#    print("hola mundo")