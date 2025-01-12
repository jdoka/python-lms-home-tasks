import requests

api_key = "f7b49d1dfc478c73ad0939ac54719ec6"
city = input("Введите город: ")

city_data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}").json()[0]
lat = city_data["lat"]
lon = city_data["lon"]

weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}").json()

temperature_diff = 273
temperature = weather["main"]["temp"] - temperature_diff
print(f"{temperature.__round__()} °C")
print(weather["weather"][0]["main"])
