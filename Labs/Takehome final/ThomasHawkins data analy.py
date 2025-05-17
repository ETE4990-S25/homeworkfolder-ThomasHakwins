import os
import json
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd


# Target base currencies and consistent target currency
BASE_CURRENCIES = ['AUD', 'BND', 'CLP', 'DKK', 'ILS']
TARGET_CURRENCY = 'USD'
# Directory containing currency subfolders

BASE_DIR = 'currency_data'


# Data storage
currency_rates = {currency: [] for currency in BASE_CURRENCIES}


dates = []

# Iterate through each base currency directory
# and read the JSON files
for base_currency in BASE_CURRENCIES:
    dir_path = os.path.join(BASE_DIR, base_currency)
    if not os.path.exists(dir_path):
        print(f"Directory for {base_currency} not found, skipping.")
        continue
# Iterate through each JSON file in the directory
    for file_name in sorted(os.listdir(dir_path)):
        if not file_name.endswith('.json'):
            continue
        file_path = os.path.join(dir_path, file_name)

        with open(file_path, 'r') as f:
            data = json.load(f)

        # Extract date from the file name
        try:
            date_str = file_name.split('_')[0]

            date = datetime.strptime(date_str, "%Y-%m-%d").date()


        except Exception as e:

            print(f"Could not parse date from {file_name}: {e}")
            continue

        # Find exchange rate to USD
        USD_rate = None
        for item in data.get("channel", {}).get("item", []):
            if item.get("targetCurrency") == TARGET_CURRENCY:

                try:
                    USD_rate = float(item["exchangeRate"])

                except (KeyError, ValueError):
                    continue
                break

        if USD_rate is not None:
            currency_rates[base_currency].append((date, USD_rate))

# Create a DataFrame to hold the exchange rates
df_dict = {'date': sorted(set(date for pairs in currency_rates.values() for date, _ in pairs))}
df = pd.DataFrame(df_dict)

df.set_index('date', inplace=True)

# Populate exchange rates
for currency, records in currency_rates.items():
    
    rate_map = {date: USD_rate for date, USD_rate in records}

    df[currency] = df.index.map(rate_map.get)

# Reset index for Seaborn compatibility
df_clean = df.reset_index()

lond_df = df_clean.melt(id_vars='date', value_vars=BASE_CURRENCIES ,
                          var_name='Currency', value_name='ExchangeRate')

# Plot using Seaborn
sns.set(style='whitegrid')
plt.figure(figsize=(14, 7))
sns.lineplot(data=lond_df, x='date', y='Exchange Rate', hue='Currency', linewidth=2)

plt.title(f'Exchange Rate Trends to {TARGET_CURRENCY }', fontsize=16)
plt.xlabel('Date')
plt.show()

