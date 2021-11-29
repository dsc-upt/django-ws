import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/dsc-upt/django-template-project/contributors', headers=headers)
response_json = response.json()

print(response_json)
for element in response_json[0]:
    print(str(response_json[0][element]))