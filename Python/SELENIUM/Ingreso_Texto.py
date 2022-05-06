from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")
session=driver.session_id
print(session)
driver.get("https://sugarcrm.com/au/request-demo")
time.sleep(3)    
# Get all the elements available with tag name 'p'
elements = driver.find_elements_by_name("firstname")
time.sleep(3)
elements.send_keys("Alberto")
                       
for i in elements:
    print(i.text)
    print("hola mundo")
