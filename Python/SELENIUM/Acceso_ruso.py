from selenium import webdriver
from time import sleep

class Google:

 def __init__(self,username,password):
  self.driver=webdriver.Chrome('C:\chromedriver.exe')
  self.driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
  sleep(3)
  self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
  self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
  self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
  sleep(3)
  self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
  self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
  sleep(2)
  self.driver.get('https://youtube.com')
  sleep(5)

#passw=open("C:\Selenium\passw.TXT","r",encoding="utf-8")   
#password=str(passw.read())
password="Berichame1"
#user=open("C:\Selenium\user.TXT","r",encoding="utf-8")   
#username=str(user.read())
username="gaviria.alberto@gmail.com"
mylike= Google(username,password)