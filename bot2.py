from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

#reading email and pass and getting input from user
f=open("mailandpass.txt","r")
email,pw=f.read().split()
minut=float(input("Enter minutes to stay in meeting:"))
team=input("Enter class name:")


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

PATH=r"C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(options=opt, executable_path=PATH)
driver.get("https://teams.microsoft.com")



#login
signin=driver.find_element_by_id("i0116")
signin.send_keys(email)
signin.send_keys(Keys.RETURN)
passw=driver.find_element_by_id("i0118")
passw.send_keys(pw)
time.sleep(3)
button1=driver.find_element_by_id("idSIButton9").click()
time.sleep(3)
button2=driver.find_element_by_id("idSIButton9").click()
time.sleep(3)
button3=driver.find_element_by_link_text("Use the web app instead").click()
time.sleep(5)

#choosing team
teams=driver.find_element_by_xpath('//*[@id="searchInputField"]')
teams.send_keys(team)
time.sleep(5)
teams.send_keys(Keys.ARROW_DOWN)
teams.send_keys(Keys.ENTER)
time.sleep(5)

#entering call
joinbutton=driver.find_element_by_xpath('//*[@id="m1600884646226"]/calling-join-button/button').click() #have to hardcode the xpath of the join element present inside team
time.sleep(2)

#to turn off camera and audio
camera=driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]').click()
time.sleep(2)
audio=driver.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button').click()
time.sleep(10)

#to join the meeting
joinnow=driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()



#staying
time.sleep(60*minut)
driver.quit()





