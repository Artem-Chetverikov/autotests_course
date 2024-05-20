# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import pytest


@pytest.mark.usefixtures('print_times')
class TestPrint:
    def test_print_01(self, print_run_time):
        assert print(' Тест 1') is None

    def test_print_02(self):
        assert print(' Тест 2') is None

    def test_print_03(self):
        assert print(' Тест 3') is None
