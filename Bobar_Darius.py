import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/bobardarius/django_training', headers=headers)
responseJson= response.json()
print(responseJson['tefal'])
