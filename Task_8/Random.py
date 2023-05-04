import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = "/Users/annagrishkova/Documents/chromedriver_mac64/chromedriver"
service = Service(executable_path=chromedriver_path)

options = webdriver.ChromeOptions()
options.headless = False  # отключаем headless режим, чтобы увидеть открытую страницу
driver = webdriver.Chrome(service=service, options=options)

# открываем страницу
driver.get("https://www.random.org/dice/")
time.sleep(4)

# ждем, пока кнопка загрузится и станет кликабельной
try:
    roll_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Roll Dice']"))
    )
except:
    print("Ошибка: кнопка не найдена на странице")
    driver.quit()
    exit()

# нажимаем на кнопку
roll_button.click()

# ждем несколько секунд, чтобы увидеть результат
time.sleep(20)
