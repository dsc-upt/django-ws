import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/dariusbobar/faculty', headers=headers)
responseJson= response.json()
print(response)
print(responseJson)
