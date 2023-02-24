import pytest

from code import utils


def test_get_data():
    assert utils.get_data('../code/test.json') == [{'a number': ['a', 'number'], 'is': 'is', 'one': 1}]
    with pytest.raises(FileNotFoundError):
        utils.get_data('name.json')
