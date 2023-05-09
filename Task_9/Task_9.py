from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = "/Users/annagrishkova/Documents/chromedriver_mac64/chromedriver"
service = Service(executable_path=chromedriver_path)

options = webdriver.ChromeOptions()
options.headless = False  # отключаем headless режим, чтобы увидеть открытую страницу
driver = webdriver.Chrome(service=service, options=options)

# открываем страницу
driver.get("https://www.random.org/coins/")
time.sleep(6)

# выбираем количество монет для броска
select_flip = Select(driver.find_element(By.CSS_SELECTOR,'select[name="num"]'))
select_flip.select_by_value('1')

# ждем появления кнопки
try:
    roll_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[value='Flip Coin(s)']"))
    )
except:
    print("Ошибка: кнопка не найдена на странице")
    driver.quit()
    exit()

# нажимаем на кнопку
roll_button.click()
time.sleep(20)
driver.quit()
