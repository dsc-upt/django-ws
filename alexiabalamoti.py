import requests

headers = { 'Accept': 'application/vnd.github.v3+json',}

response = requests.get('https://api.github.com/repos/dsc-upt/gdsc-backend', headers=headers)
responseJson = response.json()

print(responseJson['name'])
