import threading
import datetime
from datetime import datetime, timedelta
import os
import json
import random
import requests
import xmltodict



rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]

def retrieve_exchange_rates (base, date):
    
    directories = f"currency_data//{base}"
    
    os.makedirs(directories, exist_ok=True)

    # URL of the XML data
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
    # Fetch the XML data
    api_response = requests.get(url)
    api_response.raise_for_status()

    try:
        # Parse the XML data to a Python dictionary
        data_dict = xmltodict.parse(api_response.text)

        # Convert the dictionary to a JSON string
        json_data = json.dumps(data_dict, indent=4)

        with open(f"{directories}//{date}_exchange_rates_{base}.json", 'w') as json_file:
            json_file.write(json_data)

    except Exception:
        print(url)
        return 

# Function to generate a list of dates between two dates
def increase_date(Starting_date, enddate):
    start_dt = datetime.strptime(Starting_date, "%Y-%m-%d")
    end_dt = datetime.strptime(enddate, "%Y-%m-%d")
    dates = []

    currentdate = start_dt
    while currentdate <= end_dt:

        dates.append(currentdate.strftime("%Y-%m-%d"))

        currentdate += timedelta(days=1)
    
    return dates
# Function to be executed in each thread
def threader(base, date): 
    threadsPool.acquire()

    retrieve_exchange_rates (base,date)
    threadsPool.release()

    #main function to run the script
if __name__ == "__main__":
    
    max_threads = 10
    threadsPool = threading.Semaphore(max_threads)

    date = "2011-05-04"
    bases = random.sample(ratesForBase, 5)

    for base in bases:
        
#        # Create a thread for each base currency
        threads = []
        for x in increase_date(date, "2025-05-16"):
            thread = threading.Thread(target=threader, args=(base,x,))
            threads.append(thread)
            thread.start()

   