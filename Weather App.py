import requests
print(".................Welcome To Basic Weather App....................")
api_key='b81182a9e2312fc17c6dfa406fed364d'
city=input("Enter city: ")
print(f"City: {city}")
weather_data=requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
print(weather_data.status_code)
if (weather_data.status_code==200):
 weather=weather_data.json()['weather'][0]['main']
 temp_kelvin=round(weather_data.json()['main']['temp'])
 temp_celcius=round(weather_data.json()['main']['temp']-273.15,2) # convert from kelvin to celcius
 temp_fahrenheit=round((temp_kelvin - 273.15) * 9/5 + 32, 2)
 humidity=weather_data.json()['main']['humidity']
 print(f"The weather of {city} is {weather}")
 print(f"The temperature of {city} in Kelvins is {temp_kelvin} K")
 print(f"The temperature of {city} in Celcius {temp_celcius}'C")
 print(f"The temperature of {city} in Celcius {temp_fahrenheit}'F")
 print(f"The humidity in {city} is {humidity}%")
else:
 print(f"Error fetching data of city: {city}.Please check your API or city name") 