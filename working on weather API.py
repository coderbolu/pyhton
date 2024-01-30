import requests

requests_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

# get data from web API
response = requests.get (requests_url)

# convert the JSON data object into a python friendly format
data = response.json()

for weather in data:
  print(data["latitude"])
  print(data["longitude"])
  print(data["timezone"])
  print(data["generationtime_ms"])
  print(data["elevation"])
  print(data["hourly"])
  print(data["hourly_units"])
  print(data["utc_offset_seconds"])
