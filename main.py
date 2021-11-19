import requests
import json
import pandas as pd

url = "https://v3.football.api-sports.io/teams/statistics?season=2020&team=550&league=333"

payload = {}
headers = {
    'x-rapidapi-key': '254205446bea705afd5d227e7dd696c5',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}
seasons = ['2018', '2019', '2020', '2021']


def get_info():
    for i in seasons:
        url = f'https://v3.football.api-sports.io/teams/statistics?season={i}&team=550&league=333'
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        with open(f'tmp/res{i}.json', 'w') as f:
            json.dump(data, f, indent=4)


def get_win(year):
    with open(f'tmp/res{str(year)}.json', 'r') as f:
        data = json.load(f)
        fc_name = data['response']['team']['name']
        fc_wins = data['response']['fixtures']['wins']['total']
        fc_loses = data['response']['fixtures']['loses']['total']
        fc_draws = data['response']['fixtures']['draws']['total']
        print(fc_name)
    pass


def get_loses():
    pass


if __name__ == '__main__':
    # get_info()
    get_win(2020)
