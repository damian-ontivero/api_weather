# A P I   W E A T H E R

Made with Python (Flask) and SQLAlchemy as ORM.

Source weather 'https://openweathermap.org'

## To run the application you will need:
#### Have Docker installed:
    https://docs.docker.com/engine/install/

#### Make Docker image:
    docker build -t api-weather:1.0 .
Note: You must be in the Dockerfile dir

#### Run container with docker run:
    docker run --name api-weather --publish 5000:5000 api-weather:1.0

#### Run container with docker-compose:
    docker-compose up -d

    docker-compose -f docker-compose.yml up -d
Note: You must have docker-compose installed and be in the docker-compose.yml dir

### Example:
#### Request:
    curl localhost:5000/api/v1.0/weather/barcelona
Note: To check the weather of another city, change the city at the end of the url.

#### Response:
    {"temp_min": "20", "id": 45, "desc": "Algo de nubes", "temp": "23", "date": "2021-05-31T09:57:02", "country": "ES", "city": "Barcelona", "temp_max": "26"}

#### TODO
* Add unit test.