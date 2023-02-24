import json
from datetime import datetime


def get_data(path) -> list:
    """Get the data in json format"""

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def sort(data) -> list:
    """Sort the data"""

    data.sort(key=lambda x: datetime.strptime(x.get('date', '2000-01-01 00:00'), "%Y-%m-%d %H:%M"), reverse=True)
    return data

def reformat_data(data) -> list:
    """Reformat date and time data"""
    
    for dictionary in data:
        for key, value in dictionary.items():
            if key == 'date':
                new_value = value.replace('T', ' ')
                dictionary[key] = new_value[:16]
    return data
