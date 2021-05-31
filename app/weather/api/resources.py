'''
Endpoints del API
'''

from flask import request, Blueprint
from flask_restful import Api, Resource

import requests
from datetime import datetime

from .schemas import WeatherSchema
from ..models import Weather

from app.common.error_handling import ObjectNotFound

from config import Config

weather_bp = Blueprint('weather', __name__)

weather_schema = WeatherSchema()

api = Api(weather_bp)

class WeatherResource(Resource):

    def get(self, city):
        def load_weather(city):
            args = {'q': city, 'appid': Config.API_KEY, 'units': 'metric', 'lang': 'es'}
            response = requests.get(Config.API_URL, params=args)
            
            if response.status_code == 200:
                weather_json = response.json()

                country = weather_json['sys']['country']
                city = weather_json['name']
                date = datetime.fromtimestamp(weather_json['dt'])
                temp = weather_json['main']['temp']
                temp_min = weather_json['main']['temp_min']
                temp_max = weather_json['main']['temp_max']
                desc = weather_json['weather'][0]['description']

                weather = Weather(country=country, city=city, date=date, temp=int(temp), temp_min=int(temp_min), temp_max=int(temp_max), desc=desc.capitalize())
                weather.save()
            
        load_weather(city)
        weather = Weather.get_by_city(city.capitalize())
        if weather is None:
            raise ObjectNotFound('The city {} does not exist in the database.'.format(city.capitalize()))
        return weather_schema.dump(weather)


api.add_resource(WeatherResource, '/api/v1.0/weather/<string:city>', endpoint='weather_resource')