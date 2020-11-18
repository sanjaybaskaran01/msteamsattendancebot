from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import time

email=input("Enter email:") #mail of msteams
pw=input("Enter password:") #pass of msteams


PATH="C:\Program Files (x86)\chromedriver.exe" #Enter path of chromedriver saved in your computer
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
time.sleep(5)
#button4=driver.find_element_by_id("stv-item-desc-")
#button4.click()
button5=driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[6]/div[3]/div/ng-include/div').click()
time.sleep(3)
button6=driver.find_element_by_xpath('//*[@id="m1605691047669"]/calling-join-button/button/span').click()




