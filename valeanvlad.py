import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/Vlad-Valean/square-to-circle', headers=headers)
print(response)
print(response.content)
responseJson = response.json()
print(responseJson['visibility'])
