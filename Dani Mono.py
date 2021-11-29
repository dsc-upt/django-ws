import requests

"""
# creeaza un fisier extern ce te duce la site:
resp = requests.get("https://facebook.com")
with open("index.html", "w") as f:
    f.write(str(resp.content))
# print(resp.content)

#
# accesare git:
headers = {
    'Accept': 'application/vnd.github.v3+json',
}
response = requests.get('https://api.github.com/orgs/dsc-upt/repos', headers=headers)

responseJson = response.json()  # e o lista de dictionare, fiecare repo are mai multe date:id,name,language,owner,description etc...
#print(responseJson[3]['name'])

for el in responseJson:
    print(el['language'])



"""

headers = {
    'Accept': 'application/vnd.github.v3+json',
}
response = requests.get('https://api.github.com/repos/mateasmario/django-training', headers=headers)
responseJson = response.json()
print(responseJson['id'])
