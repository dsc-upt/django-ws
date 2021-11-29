import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/VladS159/faculty', headers=headers)

respJson = response.json()

print("id:",respJson['id'],";","name:",respJson['name'])