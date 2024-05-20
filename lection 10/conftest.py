import pytest
import datetime


@pytest.fixture(scope='class')
def print_times():
    print('Время начала выполнения класса: ', datetime.datetime.now())
    yield
    print('Время окончания выполнения класса: ', datetime.datetime.now())


@pytest.fixture(scope='function')
def print_run_time():
    tine_stat = datetime.datetime.now()
    yield
    print('Время выполнения теста: ', datetime.datetime.now() - tine_stat)
