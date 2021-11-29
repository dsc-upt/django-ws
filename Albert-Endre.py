import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/albert020119/faculty', headers=headers)

responseJson = response.json()
print(responseJson['owner']['avatar_url'])