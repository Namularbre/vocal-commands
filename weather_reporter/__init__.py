import json
from datetime import datetime

from http_client.http_get import http_get


def get_weather() -> str:
    json_response = http_get("https://api.open-meteo.com/v1/forecast?latitude=45.8336&longitude=1.2476&current"
                             "=temperature_2m,apparent_temperature,weather_code&timezone=Europe%2FBerlin")
    if json_response:
        response = json.loads(json_response)
        return __stringify_weather_data(response["current"])
    return "Il y a eu une erreur durant la récupération de la météo."


def __stringify_weather_data(current_weather: dict) -> str:
    current_temperature = current_weather["temperature_2m"]
    current_time = datetime.fromisoformat(current_weather["time"]).strftime("%Hh%M, le %d/%m/%Y")
    apparent_temperature = current_weather["apparent_temperature"]
    weather_code = current_weather["weather_code"]
    weather_str = __weather_code_to_str(weather_code)
    return f"Aujourd'hui à {current_time} il fait {current_temperature} degrés, ressentit {apparent_temperature}."\
           f"{str(weather_str)}"


def __weather_code_to_str(weather_code: int) -> str:
    try:
        __weather_code_to_str_dict = {
            0: "le ciel est dégagé",
            1: "le ciel est clair",
            2: "le ciel est nuageux",
            3: "c'est couvert",
            45: "il y a du brouillard",
            48: "il y a du  brouillard verglaçant",
            51: "il y a une bruine légère",
            52: "il bruine",
            53: "il y a une forte bruine",
            56: "il y a une bruine légère verglaçante",
            57: "il y a une forte bruine verglaçante",
            61: "il pleut légèrement",
            63: "il pleut",
            65: "il pleut fortement",
            66: "il y a une légère pluie verglaçante",
            67: "il y a une forte pluie verglaçante",
            71: "il neige légèrement",
            73: "il neige",
            75: "il neige fortement",
            77: "il neige (snow grains)",
            80: "il y a des petites averses",
            81: "il y a des averses",
            82: "il y a de grosses averses",
            85: "il y a de légères averses de neige",
            86: "il y a de grosses averses de neige",
            95: "il y a un orage",
            96: "il y a un orage de grêle"
        }
        return __weather_code_to_str_dict[weather_code]
    except KeyError as e:
        print(f"Received an unknown weather_code : {e}")
        return "inconnu"
