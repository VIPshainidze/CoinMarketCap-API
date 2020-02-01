import json
import requests


while True:
    ticker_url = "https://api.coinmarketcap.com/v2/ticker/?structure=array"

    request = requests.get(ticker_url)
    results = request.json()

    limit = 100
    start = 1
    sort = "rank"
    convert = "USD"

    choice = input("Do you want to enter any custom parameters? (y/n): ")

    if choice == "y":
        limit = input("What is the custom limit?: ")
        start = input("What is the custom start number?: ")
        sort = input("What do oyu want to sort by?: ")
        convert = input("What is your local currency?: ")

    ticker_url += f"&limit={str(limit)}&sort={sort}&start={start}&convert={convert}"

    # print(json.dumps(results, sort_keys=True, indent=4))

    data = results["data"]

    print()
    for currency in data:
        rank = currency["rank"]
        name = currency["name"]
        symbol = currency["symbol"]

        circulating_supply = int(currency["circulating_supply"])
        total_supply = int(currency["total_supply"])

        quotes = currency["quotes"][convert]
        market_cap = quotes["market_cap"]
        hour_change = quotes["percent_change_1h"]
        day_change = quotes["percent_change_24h"]
        week_change = quotes["percent_change_7d"]
        price = quotes["price"]
        volume = quotes["volume_24h"]

        volume_string = "{:,}".format(volume)
        market_cap_string = "{:,}".format(market_cap)
        circulating_supply_string = "{:,}".format(circulating_supply)
        total_supply_string = "{:,}".format(total_supply)

        print(f"{str(rank)}: {name} ({symbol})")
        print(f"Market cap: \t\t${market_cap_string}")
        print(f"Price: \t\t\t\t${str(price)}")
        print(f"24h volume: \t\t${volume_string}")
        print(f"Hour change: \t\t{str(hour_change)}%")
        print(f"Day change: \t\t{str(day_change)}%")
        print(f"Week change: \t\t{str(week_change)}%")
        print(f"Total supply: \t\t{total_supply_string}")
        print(f"Circulating supply: {circulating_supply_string}")
        print(f"Percentage of coins in circulation: {str(int(circulating_supply / total_supply))}")
        print()

    choice = input("Again?: (y/n):")
    if choice == "n":
        break
# done!
