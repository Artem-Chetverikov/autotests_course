# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_01():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


def test_02():
    assert all_division(6, 5) == 1.2, "Неверный результат"


def test_dec_03():
    assert all_division(100, 5, 10) == 2, "Неверный результат"


def test_04():
    assert all_division(-1, -1) == 1, "Неверный результат"


def test_dec_05():
    assert all_division(1000000000, 200000000) == 5, "Неверный результат"


# 1) запуск всех тестов
# pytest -v 'lection 10\task_2.py'

# 2) запуск смоков
# pytest -m smoke -v 'lection 10\task_2.py'

# 3) запуск по маске
# pytest -k test_dec 'lection 10\task_2.py'
