from selenium import webdriver #подключение библиотеки
driver = webdriver.Chrome() #получение объекта веб-драйвера для нужного браузера

import time

driver = webdriver.Chrome()
driver.get('https://google.com')

time.sleep(10)

