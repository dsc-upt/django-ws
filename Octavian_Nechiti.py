import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/N-octavian/tic_tac_toe', headers=headers)
responseJson = response.json()
owner_name = responseJson['owner']['login']
project = responseJson['name']
visibility = responseJson['visibility']
watchers = responseJson["watchers"]
print(f"Minunatul proiect {project} de pe JetBrainsAcademy, facut de {owner_name}, vizibil {visibility}, cu {watchers} watchers")
