import datetime
import json
import requests
import os


def get_currency(years):
    today = datetime.date.today()
    for i in range(years):
        symbols = "USD, UAH"
        url = f"http://api.exchangeratesapi.io/v1/{today.strftime('%Y-%m-%d')}?access_key=de5f8413f528aa0fbbca47c0fa9f81e6&symbols={symbols}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        with open(f'json_data/resp_cur{today.year}.json', 'w') as f:
            json.dump(data, f, indent=4)
        today = today.replace(year=today.year - 1)


def get_max_rate():
    # TODO: FIX 10
    list_of_dates = []
    list_of_rates = []
    listoffiles = list((os.listdir(f'{os.getcwd()}/json_data')))
    for i in listoffiles:
        with open(f'json_data/{i}') as f:
            data = json.load(f)
            list_of_rates.append(data['rates']['UAH'])
            list_of_dates.append(data['date'])
            print(data['date'], data['rates']['UAH'])
    maxrate =list_of_rates.index(max(list_of_rates))
    print(f'the max rate was in {list_of_dates[maxrate]} year, is {max(list_of_rates)}')

if __name__ == '__main__':
    # get_currency(15)
    get_max_rate()
