import requests

headers = {
    'Accept': 'application/vnd.github.v3+json',
}

user = 'DragosChileban'

response = requests.get('https://api.github.com/users/' + user +'/repos', headers=headers)
responseJson = response.json()


for i in responseJson:
    print(i['language'])

#print all the languages of a user's repos