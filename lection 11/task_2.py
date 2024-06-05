# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
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

sbis_site = 'https://fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'

try:
    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert 'fix-online.sbis.ru' in driver.current_url
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Авторизоваться')
    user_login, user_password = 'chet1', 'Chet123'
    login = driver.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled')
    login.send_keys(user_login, Keys.ENTER)
    sleep(1)
    assert login.get_attribute('value') == user_login, 'Неверный текст'
    password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled')
    password.send_keys(user_password, Keys.ENTER)
    sleep(2)

    print('Переходим в раздел Контакты')
    driver.get('https://fix-online.sbis.ru/page/dialogs')
    sleep(3)

    print('Навести курсор на + и сделать клик')
    add_message = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')

    action_chains = ActionChains(driver)
    action_chains.move_to_element(add_message)
    action_chains.click(add_message)
    action_chains.perform()
    sleep(3)

    print('Ищем по ФИО')
    fio = 'Четвериков Артем Васильевич'
    search = driver.find_element(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] input')

    search.send_keys(fio)
    sleep(1)

    send_all = driver.find_elements(By.CSS_SELECTOR, '[data-qa="item"] .ws-flex-column')

    send_self = None
    for item in send_all:
        if "Четвериков Артем" in item.text:
            send_self = item

    assert send_self.is_displayed(), 'ФИО не отображается'

    print('Кликаем по нужному ФИО')
    action_chains.move_to_element(send_self)
    action_chains.click(send_self)
    action_chains.perform()
    sleep(3)

    print('Отправляем текст')
    send_text = 'Текст себе'
    search = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    search.send_keys(send_text, Keys.ENTER)
    sleep(1)

    print('Навести курсор на Отправить и сделать клик')
    button_send = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"] span')
    action_chains.move_to_element(button_send)
    action_chains.click(button_send)
    action_chains.perform()
    sleep(2)

    print('Навести курсор на Закрыть и сделать клик')
    button_close = driver.find_element(By.CSS_SELECTOR, '.icon-Close')
    action_chains.move_to_element(button_close)
    action_chains.click(button_close)
    action_chains.perform()
    sleep(2)

    all_dialogs = driver.find_elements(By.CSS_SELECTOR, '.controls-ListView__itemContent_withCheckboxes_default')

    dialog_self = None
    for item in all_dialogs:
        if "Четвериков Артем" in item.text:
            dialog_self = item

    print('Навести курсор на диалог и кликнуть ПКМ')
    action_chains.move_to_element(dialog_self)
    action_chains.context_click(dialog_self)
    action_chains.perform()
    sleep(2)

    print('Кликнуть по Удалить')
    menu_delete = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
    action_chains.move_to_element(menu_delete)
    action_chains.click(menu_delete)
    action_chains.perform()
    sleep(3)

    # проверим, отображается ли текст сообщения
    # ВАРИАНТ 1
    # get_source = driver.page_source
    # assert not (send_text in get_source), "Сообщение не удалено"

    # ВАРИАНТ 2
    all_dialogs = driver.find_elements(By.CSS_SELECTOR, '.controls-ListView__itemContent_withCheckboxes_default')
    dialog_self = None
    for item in all_dialogs:
        assert not("Четвериков Артем" in item.text)

finally:
    driver.quit()
