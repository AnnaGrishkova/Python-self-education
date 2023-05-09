from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chromedriver_path = "/Users/annagrishkova/Documents/chromedriver_mac64/chromedriver"
service = Service(executable_path=chromedriver_path)

options = webdriver.ChromeOptions()
options.headless = False  # отключаем headless режим, чтобы увидеть открытую страницу
driver = webdriver.Chrome(service=service, options=options)

# открываем страницу
driver.get("https://rozetka.com.ua")
time.sleep(10)

# Найти кнопку входа в аккаунт по классу
login_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > app-root > div > div > rz-header > rz-main-header > header > div > div > ul > li.header-actions__item.header-actions__item--user > rz-user > button'))
    )
login_button.click()

register_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > app-root > rz-single-modal-window > div.modal__holder.modal__holder_show_animation.modal__holder--medium > div.modal__content > rz-user-identification > rz-auth > div > form > fieldset > div.form__row.auth-modal__form-bottom > button.auth-modal__register-link.button.button--link.ng-star-inserted'))
    )
register_button.click()

name_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#registerUserName'))
)
name_field.send_keys("Ім'я")

surname_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#registerUserSurname'))
)
surname_field.send_keys("Користувач")

phone = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#registerUserPhone'))
)
phone.send_keys("0999990000")

email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#registerUserEmail'))
)
email.send_keys("example@qwerty.com")

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#registerUserPassword'))
)
password.send_keys("password123My")

submit_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > app-root > rz-single-modal-window > div.modal__holder.modal__holder_show_animation.modal__holder--medium > div.modal__content > rz-user-identification > rz-register > div > form > fieldset > div.form__row.auth-modal__form-bottom > button.button.button--large.button--green.auth-modal__submit'))
    )
submit_button.click()

time.sleep(20)
driver.quit()