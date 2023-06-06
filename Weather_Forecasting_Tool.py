import requests
from datetime import datetime,date


city = input("ENTER YOUR CITY: ")
response = requests.get('https://goweather.herokuapp.com/weather/' + city)

current_date = datetime.now().date()
date=int(current_date.day)

mon=int(current_date.month)
print ("Date : %.2d/%.2d/%s" % (date, mon, current_date.year),"\n")  

s=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
t=datetime.today()

for x in range(0, 3):
    print("Day :",response.json()['forecast'][x]['day'],end=" , ")
    print (s[(t.weekday()+x)%7])
    print("Temperature:", response.json()['forecast'][x]['temperature'])
    print("Wind:", response.json()['forecast'][x]['wind'],"\n")