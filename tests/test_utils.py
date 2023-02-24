import pytest

from code import utils


def test_get_data():
    assert utils.get_data('../code/test.json') == [{'a number': ['a', 'number'], 'is': 'is', 'one': 1}]
    with pytest.raises(FileNotFoundError):
        utils.get_data('name.json')

def test_sort():
    assert utils.sort([{"date": "2019-08-26 10:50"}, {"date": "2022-09-11 17:30"}, {"date": "2019-12-03 04:27"}]) == [{"date": "2022-09-11 17:30"}, {"date": "2019-12-03 04:27"}, {"date": "2019-08-26 10:50"}]
    with pytest.raises(ValueError):
        utils.sort([{"date": "2019-08-26 10:"}, {"date": "2022-09-11 17:30"}, {"date": "2019-12-03 04:27"}])

def test_reformat_data():
    assert utils.reformat_data([{"date": "2019-08-26T10:50:58.294041"}]) == [{"date": "2019-08-26 10:50"}]
    assert utils.reformat_data([{"not_date": "2019-08-26T10:50:58.294041"}]) == [{"not_date": "2019-08-26T10:50:58.294041"}]
