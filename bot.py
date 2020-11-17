from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
email=input("Enter email:")
pw=input("Enter password:")
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://teams.microsoft.com")
signin=driver.find_element_by_id("i0116")
signin.send_keys(email)
signin.send_keys(Keys.RETURN)
passw=driver.find_element_by_id("i0118")
passw.send_keys(pw)
time.sleep(3)
button1=driver.find_element_by_id("idSIButton9")
button1.click()
time.sleep(3)
button2=driver.find_element_by_id("idSIButton9")
button2.click()
time.sleep(3)
button3=driver.find_element_by_link_text("Use the web app instead")
button3.click()

