import datetime
import json
import requests


def get_currency(years):
    today = datetime.date.today()
    for i in range(years):
        symbols = "USD, UAH"
        url = f"http://api.exchangeratesapi.io/v1/{today.strftime('%Y-%m-%d')}?access_key=de5f8413f528aa0fbbca47c0fa9f81e6&symbols={symbols}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        today = today.replace(year=today.year - 1)
        with open(f'json_data/resp_cur{today.year}.json', 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == '__main__':
    get_currency(5)