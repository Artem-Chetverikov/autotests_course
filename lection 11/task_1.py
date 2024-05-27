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

driver = webdriver.Chrome()
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

    print('Проверить текст, атрибут и видимость вкладки Контакты')
    link_txt = 'Контакты'
    contact_link = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    assert contact_link.text == link_txt, 'Неверный текст'
    assert contact_link.is_displayed(), 'Элемент не отображается'

    print('Перейти на вкладку Контакты')
    contact_link.click()
    sleep(1)
    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4

    print('Проверить текст, атрибут и видимость баннера Тензор')
    banner_txt = 'Разработчик системы СБИС — компания «Тензор»'
    banner_link = driver.find_element(By.CSS_SELECTOR, '[src="/static/resources/SabyRuPages/_contacts/images/logo.svg?x_module=7a60fd27b3032e3a7f861198d93499ab"]')
    assert banner_link.get_attribute('alt') == banner_txt
    assert banner_link.is_displayed(), 'Элемент не отображается'

    print('Перейти на страницу Тензор')
    banner_link.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[1])

    print('Проверить адрес сайта и заголовок страницы')
    assert 'tensor.ru' in driver.current_url
    assert driver.title == 'Тензор — IT-компания'


    print('Найти блок Сила в людях')
    news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card > [class="tensor_ru-Index__card-title tensor_ru-pb-16"]')
    print('Проверить текст, атрибут и видимость новости')
    news_txt = 'Сила в людях'
    assert news.text == news_txt, 'Неверный текст'
    assert news.is_displayed(), 'Элемент не отображается'

    print('Найти ссылку Подробнее')
    link_about = driver.find_element(By.XPATH, '//a[@href="/about" and text()="Подробнее" ]')
    print('Проверить текст, атрибут и видимость ссылки Подробнее')

    link_about_txt = 'Подробнее'
    assert link_about.text == link_about_txt, 'Неверный текст'
    assert link_about.is_displayed(), 'Элемент не отображается'

    driver.get(link_about.get_attribute('href'))

    # Не хочет так работать:
    # action_chains = ActionChains(driver)
    # action_chains.move_to_element(link_about).perform()
    # action_chains.click(link_about)
    # action_chains.perform()

    sleep(5)
    print('Проверить адрес сайта и заголовок страницы "О компании"')
    assert 'tensor.ru/about' in driver.current_url, 'Неверный адрес'
    assert driver.title == 'О компании | Тензор — IT-компания'

finally:
    driver.quit()