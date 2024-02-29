from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions() 

userdatadir = 'C:/Users/Chen1/AppData/Local/Google/Chrome/User Data/Guest Profile'
options.add_argument(f"--user-data-dir={userdatadir}")

driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')

x = input()
driver.quit()