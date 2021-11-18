import requests
import json
import pandas as pd
url = "https://v3.football.api-sports.io/teams/statistics?season=2021&team=550&league=333"

payload={}
headers = {
  'x-rapidapi-key': '254205446bea705afd5d227e7dd696c5',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
with open('tmp/res.json', 'w') as f:
     json.dump(data, f, indent=4)
