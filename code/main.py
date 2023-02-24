from utils import get_data, sort, reformat_data

PATH = 'data.json'

text = get_data(PATH)
reformatted_text = reformat_data(text)
sorted_text = sort(reformatted_text)
