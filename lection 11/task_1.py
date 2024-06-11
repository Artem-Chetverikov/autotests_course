# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Настройка браузера
options = Options()
options.add_argument("--window-size=1800,950")
driver = webdriver.Chrome(options=options)

sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:
    driver.get(sbis_site)
    sleep(1)

    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4

    print('Проверить текст, атрибут и видимость вкладки Контакты')
    link_txt = 'Контакты'
    contact_link = driver.find_element(By.LINK_TEXT, link_txt)

    print('Перейти на вкладку Контакты')
    contact_link.click()
    sleep(1)

    print('Проверить текст, атрибут и видимость баннера Тензор')
    banner_txt = 'Разработчик системы СБИС — компания «Тензор»'
    banner_link = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-12"]')

    print('Перейти на страницу Тензор')
    banner_link.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])

    print('Найти блок Сила в людях')
    news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    print('Проверить текст, атрибут и видимость новости')
    news_txt = 'Сила в людях'
    assert news_txt in news.text, 'Неверный текст'

    print('Найти ссылку Подробнее')
    link_about = driver.find_element(By.XPATH, '//a[@href="/about" and text()="Подробнее" ]')
    print('Проверить текст, атрибут и видимость ссылки Подробнее')

    link_about_txt = 'Подробнее'

    # ВАРИАНТ 1
    # driver.get(link_about.get_attribute('href'))

    # ВАРИАНТ 2
    driver.execute_script("arguments[0].scrollIntoView(true);", link_about)
    sleep(2)
    link_about.click()

    sleep(5)
    print('Проверить адрес сайта и заголовок страницы "О компании"')
    assert 'tensor.ru/about' in driver.current_url, 'Неверный адрес'
    assert driver.title == 'О компании | Тензор — IT-компания'

finally:
    driver.quit()
