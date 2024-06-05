# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
import requests
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options

# Настройка браузера
options = Options()
preferences = {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", preferences)

options.add_argument("--window-size=1800,950")

driver = webdriver.Chrome(options=options)

sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:

    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4

    link_txt = 'Скачать локальные версии'
    download_link = driver.find_element(By.CSS_SELECTOR, '[href="/download"]')

    print('Перейти на страницу скачивания')
    driver.execute_script("arguments[0].scrollIntoView(true);", download_link)
    sleep(2)
    driver.execute_script("arguments[0].click();", download_link)
    sleep(1)

    tabs = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"] .controls-TabButton__inner')
    print('Перейти на вкладку СБИС Плагин')
    driver.execute_script("arguments[0].click();", tabs)
    sleep(1)

    print('Проверить отображение вкладки Windows')
    win_tabs = driver.find_element(By.CSS_SELECTOR, '[data-id="default"]')
    assert win_tabs.is_displayed(), 'Элемент не отображается'
    assert win_tabs.text == 'Windows', 'Неверный текст'

    link_txt = 'Скачать (Exe 7.21 МБ)'
    download_link = driver.find_element(By.LINK_TEXT, link_txt)

    print('Скачать в папку')
    # file_url = download_link.get_attribute("href")
    # driver.get(file_url)
    download_link.click()

    # Вариант 2
    # Отправка GET-запроса на получение файла
    # response = requests.get(file_url)
    # response.raise_for_status()
    #
    # # Сохранение файла на диск
    # with open('file_name.extension', 'wb') as file:
    #     file.write(response.content)

    sleep(7)

    # Проверяем последний по времени файл
    structure = os.listdir()
    file_last = None
    time_last = 0
    for file in structure:
        if os.stat(file).st_ctime > time_last:
            time_last = os.stat(file).st_ctime
            file_last = file

    assert 'sbisplugin-setup-web' in file_last, 'Требуемый файл не найден'

    # Напечатаем размер файла в Мб
    print(f"Размер файла {file_last}: {round(os.stat(file_last).st_size/1024/1024, 2)} Мб")

    # Удалим скачанный файл
    os.remove(file_last)

finally:
    driver.quit()
