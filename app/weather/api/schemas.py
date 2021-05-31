'''
Schemas for serializing the models in JSON
'''

from marshmallow import fields

from app.ext import ma

class WeatherSchema(ma.Schema):
    id = fields.Integer(dump_only=True) # It only matter in serialization
    country = fields.String()
    city = fields.String()
    date = fields.DateTime()
    temp = fields.String()
    temp_min = fields.String()
    temp_max = fields.String()
    desc = fields.String()