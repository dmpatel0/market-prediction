import pandas as pd
import json

# Download cik_to_tickers.json from 
# https://github.com/jadchaar/sec-cik-mapper/tree/main/mappings/stocks 
# The online json provides some companies with multiple tickers, this simplifies the json down to a one-to-one mapping
with open('cik_to_tickers.json') as json_data:
    data = json.load(json_data)
    keys = []
    items = []
    for key, item in data.items():
        keys.append(key)
        items.append(item[0])

    df = pd.DataFrame(zip(keys, items), columns=['CIK', 'Ticker'])
    df.to_json('cik_mapping.json', orient='records', lines=True)