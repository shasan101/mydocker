FROM python:3

ENV APP_BACKGROUNDD_COLOR=blue
ENV MYSQL_ROOT_PASSWORD=mydbpassword
ENV MYSQL_DATABASE=flask_db
ENV DB_HOST=mysqldb
ENV MYSQL_USER=root

WORKDIR /usr/src/FlaskApp

COPY ./code ./
RUN pip install --no-cache-dir -r requirements.txt

COPY FlaskApp.wsgi /usr/src

EXPOSE 5000

CMD [ "python", "./__init__.py" ]
