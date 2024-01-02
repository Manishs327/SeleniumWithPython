import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class Alert:

    def js_alert_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
        driver.switch_to.frame(driver.find_element(By.ID,"iframeResult"))
        driver.find_element(By.XPATH,"//button[text()='Try it']").click()
        time.sleep(5)
        driver.switch_to.alert.accept()
        time.sleep(5)

alt = Alert()
alt.js_alert_demo()
