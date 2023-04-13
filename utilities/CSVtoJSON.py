# The code loads a CSV file into a Pandas DataFrame and then
# converts the DataFrame into a sorted and formatted JSON file.

import json
import pandas as pd 

# Load the CSV file into a DataFrame
df = pd.read_csv('csvNew.csv')

# Convert the filtered DataFrame to a sorted and formatted JSON file
df.sort_values(by=['Organization Name'], inplace=True)
df.to_json('myJSON.json', orient='records', indent=4)
