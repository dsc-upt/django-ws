import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/albert020119/faculty', headers=headers)
responseJson = response.json()
owner_name=responseJson['owner']['login']
print(owner_name)