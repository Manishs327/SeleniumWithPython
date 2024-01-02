import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class AutoSuggest:

    def auto_suggest(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        time.sleep(5)
        ele1=driver.find_element(By.ID,"BE_flight_origin_city")
        ele1.click()
        time.sleep(2)
        ele1.send_keys("JFK")
        time.sleep(2)
        ele1.send_keys(Keys.ENTER)
        ele2=driver.find_element(By.ID,"BE_flight_arrival_city")
        ele2.click()
        time.sleep(2)
        ele2.send_keys("DEL")
        time.sleep(2)
        ele2.send_keys(Keys.ENTER)
        time.sleep(4)
        ele1.click()
        time.sleep(2)
        ele1.send_keys("New")
        time.sleep(2)
        elements=driver.find_elements(By.XPATH,"//p[@class='ac_cityname']")
        for ele in elements:
            print(ele.text)
            if(ele.text=='New Orleans (MSY)'):
                ele.click()
                print('This is clicked')
                break
                time.sleep(2)

        time.sleep(10)



auto=AutoSuggest()
auto.auto_suggest()
