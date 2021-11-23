import requests
import os

API_key = "734be6d868bc3f5eba0e5cbb1bb2bbc2"
tabriz_lat = 38.096237
tabriz_lon = 46.273800
OW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": tabriz_lat,
    "lon": tabriz_lon,
    "appid": API_key,
}


request = requests.get(url=OW_Endpoint, params=parameters)
all_data = request.json()
print(all_data["daily"])




