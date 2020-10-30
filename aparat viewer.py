from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)
counter = 0
while True:
    try:
        counter+=1
        driver.get('https://www.aparat.com/v/IbcVT')
        time.sleep(40)
        driver.delete_all_cookies()
        print(counter)
    except:
        print('erore')
        time.sleep(10)
