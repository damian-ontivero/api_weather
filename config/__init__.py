'''
Configuración de la app
'''

class Config:
    API_KEY = 'a4c3297ec7d40ebb82b51c6f3ac08b55'

    PROPAGATE_EXCEPTIONS = True

    # Database configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
    SHOW_SQLALCHEMY_LOG_MESSAGES = False

    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
    ERROR_404_HELP = False
    