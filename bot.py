from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import time

email=input("Enter email:")
pw=input("Enter password:")


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})

PATH="C:\Program Files (x86)\chromedriver.exe" #enter the path of chromedriver.exe
driver=webdriver.Chrome(chrome_options=opt, executable_path=PATH)
driver.get("https://teams.microsoft.com")



#Login
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

#choosing team
choose_team=driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[2]/div[6]/div/ng-include/div').click()
time.sleep(3)
joinbutton=driver.find_element_by_xpath('//*[@id="m1605624438686"]/calling-join-button/button').click()


camera=driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]').click()
#joinnow=driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').clic()





