import json


def get_data(path):
    """Get the data in json format
    :return: dict"""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

