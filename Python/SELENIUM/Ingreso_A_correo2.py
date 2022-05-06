from selenium import webdriver
from selenium.webdriver.chrome.options import Options
option=Options()
option.add_experimental_option("debuggerAddress","localhost:9222")
driver=webdriver.Chrome(options=option)

driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe",options=option)
driver.get("https://gmail.com")

#usuario=driver.find_element_by_id("identifierId")
#usuario.send_keys("gaviria.alberto@gmail.com")
#usuario.send_keys(Keys.ENTER)
#time.sleep(4)
#usuario=driver.find_element_by_name("password")
#usuario.send_keys("Berichame1")
#usuario.send_keys(Keys.ENTER)
