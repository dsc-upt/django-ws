import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/octocat/hello-world/languages', headers=headers)
response.json = response.json(headers)
print(response)
print(response.json)
