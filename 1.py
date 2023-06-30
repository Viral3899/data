import pandas as pd



df = pd.read_parquet('ITR_sample.parquet')


import json
import pandas as pd

# Assuming you have a DataFrame named 'df' with the JSON data

# Iterate over the DataFrame rows
for index, row in df.iterrows():
    # Get the JSON data from the 'report' column
    # json_data = row['report']
    json_data = row['report'].decode('utf-8')

    # Create the file name using the index
    file_name = f'report_{index}.json'

    # Write the JSON data to a file
    with open(file_name, 'w') as file:
        json.dump(json_data, file)

print(df)