from code.utils import Data, ReformattedData, main

# Path to the file with data
PATH = 'data.json'

data = Data(PATH)
text = data.get_data()

new_text = ReformattedData(text)
reformatted_text = new_text.reformat_data()

# Final data for output
final_output = main(reformatted_text)[:5]

for operation in final_output:
    print(operation)
    print()
