from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class JsClick:

    def jsclick_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        ele=driver.find_element(By.ID,"BE_flight_flsearch_btn")
        #ele.click()
        driver.execute_script("arguments[0].click();",ele)
        time.sleep(20)

js=JsClick()
js.jsclick_demo()
