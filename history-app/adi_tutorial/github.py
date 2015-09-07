import requests

url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript"
response = requests.get(url)
response_dict = response.json()

print response_dict


##############################################
### Programmatic method for generating token:
# gh_username = raw_input('GitHub username: ')
# gh_password = raw_input('GitHub password: ')
# payload = json.dumps({'scopes': []})
#
# gh_response = requests.post('https://api.github.com/authorizations', auth=(gh_username, gh_password), data=payload)
# print gh_response.json()['token']
##############################################