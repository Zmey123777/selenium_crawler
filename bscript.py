from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Настройки Chrome для headless-режима
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Включаем headless-режим
options.add_argument("--disable-gpu")  # Отключаем GPU (рекомендуется для headless)
options.add_argument("--no-sandbox")  # Отключаем sandbox (рекомендуется для Linux)
options.add_argument("--disable-dev-shm-usage")  # Решает проблемы с памятью в Docker
options.add_argument("--disable-blink-features=AutomationControlled")  # Отключаем автоматизацию

# Запуск браузера
service = Service('/path/to/chromedriver')  # Укажите путь к chromedriver
driver = webdriver.Chrome(service=service, options=options)

# Переход на сайт
driver.get("http://www.encar.com/")

# Эмуляция поведения пользователя
def emulate_behavior():
    # Случайные задержки
    time.sleep(random.uniform(1, 3))

    # Движения мыши (в headless-режиме не работают, но можно эмулировать скроллинг)
    driver.execute_script("window.scrollBy(0, 500)")
    time.sleep(random.uniform(1, 2))
    driver.execute_script("window.scrollBy(0, -250)")

# Эмуляция поведения
emulate_behavior()

# Получение содержимого страницы
content = driver.page_source
print("Содержимое страницы:", content)

# Скриншот
driver.save_screenshot("screenshot.png")

# Закрытие браузера
driver.quit()