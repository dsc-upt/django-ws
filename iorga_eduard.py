import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/EdiOne07/faculty', headers=headers)
responseJson=response.json()
print(responseJson['full_name'])
print(responseJson['private'])
print(responseJson['html_url'])
