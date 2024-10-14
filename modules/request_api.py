import requests
#Импортирует read_json через фром
from .read_json import read_json
#импорт json
import json
#Дата апи читает конфиг read_json
data_api = read_json(name_file= 'config_api.json')
#Апи ключ
API_KEY = data_api['api_key']
#Указываем название города в котором мы находимся или тот в котором мы хотим видеть погоду
CITY_NAME = data_api['city_name']
#Вставляем юрлк ссылку на карту Open weather и указываем наш апи ключ
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#Задаем вопрос на полученние юрлки
response = requests.get(URL)
#Если ответ-статус код равен 200
if response.status_code == 200:
    #Отвекчаем на контент
    data_dict = json.loads(response.content)
    #Переводим словарь в тип данных строки
    print(json.dumps(data_dict, indent= 4))