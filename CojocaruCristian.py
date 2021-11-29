import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get('https://api.github.com/repos/octocat/hello-world/languages', headers=headers)
responseJson = response.json(headers)
print(response)
print(responseJson ['name'])
