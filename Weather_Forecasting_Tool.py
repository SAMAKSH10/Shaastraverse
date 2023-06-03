import requests

city = input("ENTER YOUR CITY")
response = requests.get('https://goweather.herokuapp.com/weather/' + city)
#print( response.status_code)
#print(response.json())
temperature = response.json()['temperature']
print(temperature)
wind = response.json()['wind']
print(wind)
description = response.json()['description']
print(description)
for x in range(0, 3):
  print(response.json()['forecast'][x]['day'])
  print(response.json()['forecast'][x]['temperature'])
  print(response.json()['forecast'][x]['wind'])