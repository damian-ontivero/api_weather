FROM python:3.9-alpine3.13

# Arguments for the image
ARG user=api-weather
ARG group=api-weather
ARG home=/home/${user}
ARG APP_DIR=/opt/api-weather

# User and group creation
RUN mkdir -p ${home} \
    && addgroup -S ${group} \
    && adduser -S ${user} -G ${group} -h ${home}

# Copy app
COPY . ${APP_DIR}

# Set workdir
WORKDIR /opt/api-weather

# Installing dependencies
RUN apk --no-cache --update add build-base \
    && pip3 install -r requirements.txt

# Grant user permissions
RUN chown -R ${user}:${group} ${APP_DIR}

# Set user
USER ${user}

# Set the Flask app environment variable
ENV FLASK_APP=entrypoint:app

# Run entrypoint script
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]