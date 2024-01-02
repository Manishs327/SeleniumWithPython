from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class AttVal:

    def get_att_val(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        driver.implicitly_wait(20)
        text_get=driver.find_element(By.XPATH,"//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(text_get)

at_val = AttVal()
at_val.get_att_val()
