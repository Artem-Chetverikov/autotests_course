# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.skip('скипаем этот тест')
def test_01():
    with pytest.raises(KeyError):
        all_division(1, 0)


@pytest.mark.parametrize('a, b, result', [(2, 2, 1), (6, 5, 1.2), (1, -1, -1)])
def test_02(a, b, result):
    assert all_division(a, b) == result, "Неверный результат"


@pytest.mark.smoke
def test_dec_03():
    assert all_division(100, 5, 10) == 2, "Неверный результат"


def test_04():
    assert all_division(-1, -1) == 1, "Неверный результат"


def test_dec_05():
    assert all_division(1000000000, 200000000) == 5, "Неверный результат"
