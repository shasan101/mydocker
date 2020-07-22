FROM python:3

WORKDIR /usr/src/FlaskApp

COPY ./code ./
RUN pip install --no-cache-dir -r requirements.txt

COPY FlaskApp.wsgi /usr/src

EXPOSE 5000

CMD [ "python", "./__init__.py" ]
