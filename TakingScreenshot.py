from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class TakeScreenshot:

    def takeScreenshot(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.yatra.com")
        driver.implicitly_wait(20)
        driver.get_screenshot_as_file("./ScreenshotFile/screenshot1.png")
        driver.save_screenshot("./ScreenshotFile/ss1.png")
        driver.get_screenshot_as_base64()

ts = TakeScreenshot()
ts.takeScreenshot()
