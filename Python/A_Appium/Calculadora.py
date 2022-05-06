from appium import webdriver

celu_calculadora={
  "platformName": "Android",
  "appium:platformVersion": "10",
  "appium:deviceName": "P731F50",
  "appium:automationName": "UiAutomator1",
  "appium:appPackage": "com.google.android.calculator",
  "appium:appActivity": "com.android.calculator2.Calculator",
  "appium:autoGrantPermissions": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", celu_calculadora)
driver.find_element_by_id("com.google.android.calculator:id/digit_7").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_5").click()
driver.find_element_by_id("com.google.android.calculator:id/op_mul").click()
driver.find_element_by_id("com.google.android.calculator:id/digit_4").click()
driver.find_element_by_id("com.google.android.calculator:id/eq").click()

driver.find_element_by_accessibility_id("Más opciones").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").click()


