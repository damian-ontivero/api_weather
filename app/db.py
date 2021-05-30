'''
Database configuration
Basic methods
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel:
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_by_city(cls, city):
        return cls.query.filter_by(city=city).order_by(cls.id.desc()).first()