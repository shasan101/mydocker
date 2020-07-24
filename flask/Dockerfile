FROM python:3

WORKDIR /usr/src/FlaskApp

COPY ./code ./
RUN pip install --proxy "http://muhammadhasan2:Volley<3ball@172.16.0.28:8080" --no-cache-dir -r requirements.txt

COPY FlaskApp.wsgi /usr/src

EXPOSE 5000

CMD [ "python", "./__init__.py" ]
