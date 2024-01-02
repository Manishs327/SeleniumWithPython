import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class Sliders:

    def handle_slider_demo(self):
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.snapdeal.com/products/mobiles-printed-back-covers?sort=plrty")
        driver.implicitly_wait(20)
        driver.find_element(By.XPATH,"//div[text()='Mobiles & Tablets']").click()
        time.sleep(5)
        act=ActionChains(driver)
        ele1=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        act.drag_and_drop_by_offset(ele1,40,0).perform()
        time.sleep(4)
        ele2=driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
        act.drag_and_drop_by_offset(ele2,-40,0).perform()
        time.sleep(8)

slide = Sliders()
slide.handle_slider_demo()
