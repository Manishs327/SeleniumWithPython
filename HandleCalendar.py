from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Calendar:

    def calendar_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        ele1=driver.find_element(By.ID,"BE_flight_origin_city")
        ele1.click()
        time.sleep(1)
        ele1.send_keys("New Delhi")
        time.sleep(1)
        ele1.send_keys(Keys.ENTER)
        time.sleep(1)
        ele2=driver.find_element(By.ID,"BE_flight_arrival_city")
        ele2.click()
        time.sleep(1)
        ele2.send_keys("Mumbai")
        time.sleep(1)
        ele2.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element(By.NAME,"flight_origin_date").click()
        time.sleep(1)
        elements=driver.find_elements(By.XPATH,"//tr/td")
        for ele in elements:
            if(ele.get_attribute("id")=="28/12/2023"):
                ele.click()
                break
        time.sleep(10)

cal = Calendar()
cal.calendar_demo()


