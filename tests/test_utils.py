import pytest
from code.utils import Data, ReformattedData, main


def test_data_get_data_good():
    data = Data('../code/test.json')
    assert data.get_data() == [{'a number': ['a', 'number'], 'is': 'is', 'one': 1}]


def test_data_get_data_error():
    data = Data('name.json')
    with pytest.raises(FileNotFoundError):
        data.get_data()

def test_data_repr():
    expected = 'Python Path: test'
    data = Data('test')
    assert expected == data.__repr__()
def test_sort_good():
    date = ReformattedData([{"date": "2019-08-26 10:50"}, {"date": "2022-09-11 17:30"}, {"date": "2019-12-03 04:27"}])
    assert date.sort() == [{"date": "2022-09-11 17:30"}, {"date": "2019-12-03 04:27"}, {"date": "2019-08-26 10:50"}]


def test_sort_error():
    date = ReformattedData([{"date": "2019-08-26 10:"}, {"date": "2022-09-11 17:30"}, {"date": "2019-12-03 04:27"}])
    with pytest.raises(ValueError):
        date.sort()


def test_reformat_data_success():
    date = ReformattedData([{"date": "2019-08-26T10:50:58.294041"}])
    assert date.reformat_data() == [{"date": "2019-08-26 10:50"}]


def test_reformat_data_fail():
    date = ReformattedData([{"not_date": "2019-08-26T10:50:58.294041"}])
    assert date.reformat_data() == [{"not_date": "2019-08-26T10:50:58.294041"}]

def test_ReformattedData_repr():
    expected = 'Python Data: test'
    data = ReformattedData('test')
    assert expected == data.__repr__()

def test_main_good():
    data = [{"state": "EXECUTED",
             "date": "2019-08-26 10:50",
             "operationAmount": {"amount": "31957.58",
                                 "currency": {"name": "руб."}},
             "description": "Перевод организации",
             "from": "Maestro 1596837868705199",
             "to": "Счет 64686473678894779589"
             }]
    assert main(data) == ['26.08.2019 Перевод организации\n'
                          'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                          '31957.58 руб.']

def test_main_no_date():
    data = [{"date": "2019-08-26 10:50"}]
    assert main(data) == []

def test_main_canceled():
    data = [{"state": "CANCELED"}]
    assert main(data) == []

def test_main_key_error():
    data = [{"state": "EXECUTED",
             "date": "2019-08-26 10:50",
             "description": "Перевод организации",
             "from": "Maestro 1596837868705199",
             "to": "Счет 64686473678894779589"
             }]
    with pytest.raises(KeyError):
        main(data)

def test_main_open_account():
    data = [{"state": "EXECUTED",
             "date": "2019-08-26 10:50",
             "operationAmount": {"amount": "31957.58",
                                 "currency": {"name": "руб."}},
             "description": "Открытие вклада",
             "to": "Счет 64686473678894779589"
             }]
    assert main(data) == ['26.08.2019 Открытие вклада\n'
                          'Счет **9589\n'
                          '31957.58 руб.']
