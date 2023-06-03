import requests
from datetime import date

city = input("ENTER YOUR CITY : ")
response = requests.get('https://goweather.herokuapp.com/weather/' + city)
# print( response.status_code)
# print(response.json())gwa
# temperature = response.json()['temperature']
# print(temperature)
# wind = response.json()['wind']
# print(wind)
# description = response.json()['description']
# print(description)
s=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
t=date.today()
for x in range(0, 3):
    print("Day :",response.json()['forecast'][x]['day'],end=" , ")
    print (s[(t.weekday()+x)%7])
    print("Temprature :",response.json()['forecast'][x]['temperature'])
    print("Wind Speed :",response.json()['forecast'][x]['wind'],"\n")
