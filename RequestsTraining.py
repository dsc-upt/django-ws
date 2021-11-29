import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/mateasmario/django-training', headers=headers)

responseJson = response.json()

print(f"name of the repo is {responseJson['name']}")