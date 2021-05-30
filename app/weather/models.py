'''
Modelo de la tabla de la base de datos
'''

from app.db import db, BaseModel

class Weather(db.Model, BaseModel):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    country = db.Column(db.String(128), nullable=False)
    city = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    temp = db.Column(db.Integer, nullable=False)
    temp_min = db.Column(db.Integer, nullable=False)
    temp_max = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(128), nullable=False)

    def __init__(self, country, city, date, temp, temp_min, temp_max, desc):
        self.country = country
        self.city = city
        self.date = date
        self.temp = temp
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.desc = desc

    def __repr__(self):
        return 'City: {} - Weather: {}'.format(self.city, self.temp)
    
    def __str__(self):
        return '{} - {}'.format(self.city, self.temp)