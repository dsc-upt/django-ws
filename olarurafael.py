import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/orgs/dsc-upt/repos', headers=headers)
responseJson = response.json()

print(responseJson[0]['name'])
