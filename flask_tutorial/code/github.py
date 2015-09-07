import requests

url = "https://api.github.com/search/repositories?q=Space%20Invaders%20HTML5+language:JavaScript"
response = requests.get(url)
response_dict = response.json()


print "The complete response:\n"
print response_dict



print "\n\nChoosing one element, we see the following."
print  response_dict["items"][0]["language"]