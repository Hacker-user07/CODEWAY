from pip._vendor import requests

apikey="792c017f8919398cb631c27a12c443eb"
userInput=input('enter city name:-')
data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&appid={apikey}")
weather=data.json()['weather'][0]['main']
temp=data.json()['main']['temp']
print(f"The weather in {userInput} is {weather} and temperature is {temp}F")
