import requests

requests_url = "https://official-joke-api.appspot.com/random_joke"

# get data from web API
response = requests.get (requests_url)

# convert the JSON data object into a python friendly format
data = response.json()

# go through each joke in the list of data and print it.
print(data["type"])
print(data["setup"])
print(data["punchline"])  

# to work with API, you go to the documentaions and find out what the addresses are, of the API that will give you certain information taht you then use in your program