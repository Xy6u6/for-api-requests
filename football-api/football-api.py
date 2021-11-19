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


def get_statistic(year):
    with open(f'tmp/res{str(year)}.json', 'r') as f:
        data = json.load(f)
        fc_name = data['response']['team']['name']
        fc_wins = data['response']['fixtures']['wins']['total']
        fc_loses = data['response']['fixtures']['loses']['total']
        fc_draws = data['response']['fixtures']['draws']['total']
        print(f'A football club: \b {fc_name} has next stats in {year}y season:'
              f'\n total wins: {fc_wins},'
              f'\n total draws: {fc_draws},'
              f'\n total loses: {fc_loses},'
              f'\n wins percentage: {(fc_wins / (fc_draws + fc_wins + fc_loses)) * 100}%')


if __name__ == '__main__':
    #get_info()
    get_statistic(2021)
