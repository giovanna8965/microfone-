import requests

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=da9eb21ffc614118c8abe326f71b7171"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        return f"O tempo em {city} está {weather_desc} com temperatura de {temp_celsius:.1f} graus Celsius."
    else:
        return "Não foi possível obter a previsão do tempo para esta cidade."
