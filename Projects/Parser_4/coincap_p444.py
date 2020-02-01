import math
import json
import locale
import requests
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, "en-US.UTF-8")

global_URL = "https://api.coinmarketcap.com/v2/global"
ticker_URL = "https://api.coinmarketcap.com/v2/ticker/?structure=array"

request = requests.get(global_URL)
results = request.json()
data = results["data"]
# print(json.dumps(data, sort_keys=True, indent=4))
global_cap = int(data["quotes"]["USD"]["total_market_cap"])

table = PrettyTable(["Name", "Ticker", "% of total global cap", "Current", "7.7T (Gold)", "36.8T (Narrow Money)",
                     "73T (World Stock Markets)", "90.4T (Broad Money)", "217T (Real Estate)", "544T (Derivatives)"])

request = requests.get(ticker_URL)
results = request.json()
data = results["data"]

for currency in data:
    name = currency["name"]
    ticker = currency["symbol"]
    percentage_of_global_cap = float(currency["quotes"]["USD"]["market_cap"]) / float(global_cap)

    current_price = round(float(currency["quotes"]["USD"]["price"]), 2)
    available_supply = float(currency["total_supply"])

    trillion7price = round(7700000000000 * percentage_of_global_cap / available_supply, 2)
    trillion36price = round(36000000000000 * percentage_of_global_cap / available_supply, 2)
    trillion73price = round(73000000000000 * percentage_of_global_cap / available_supply, 2)
    trillion90price = round(90400000000000 * percentage_of_global_cap / available_supply, 2)
    trillion217price = round(217000000000000 * percentage_of_global_cap / available_supply, 2)
    trillion544price = round(544000000000000 * percentage_of_global_cap / available_supply, 2)

    percentage_of_global_cap_string = str(round(percentage_of_global_cap * 100, 2)) + "%"
    current_price_string = "$" + str(current_price)
    trillion7price_string = "$" + locale.format_string("%.2f", trillion7price, True)
    trillion36price_string = "$" + locale.format_string("%.2f", trillion36price, True)
    trillion73price_string = "$" + locale.format_string("%.2f", trillion73price, True)
    trillion90price_string = "$" + locale.format_string("%.2f", trillion90price, True)
    trillion217price_string = "$" + locale.format_string("%.2f", trillion217price, True)
    trillion544price_string = "$" + locale.format_string("%.2f", trillion544price, True)

    table.add_row([name,
                   percentage_of_global_cap_string,
                   trillion7price_string,
                   trillion36price_string,
                   trillion73price_string,
                   trillion90price_string,
                   trillion217price_string,
                   trillion544price_string])

print()
print(table)
print()
