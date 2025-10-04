import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

binary_yandex_driver_file = 'yandexdriver.exe'

options = webdriver.ChromeOptions()
service = ChromeService(executable_path=binary_yandex_driver_file)

driver = webdriver.Chrome(service=service, options=options, keep_alive=True)

driver.get('https://ya.ru')


try:
    while True:
        _ = driver.window_handles
        time.sleep(1)
except Exception:
    print("Браузер был закрыт пользователем")
    driver.quit()
    os.system("shutdown /l")