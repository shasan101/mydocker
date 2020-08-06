FROM python:3

#RUN mkdir /usr/src/FlaskApp
#RUN mkdir /usr/src/FlaskApp/code

WORKDIR /usr/src/FlaskApp/code


COPY ./code ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY FlaskApp.wsgi /usr/src/FlaskApp/

EXPOSE 5000

VOLUME /usr/src

RUN ls

RUN ls ..

CMD [ "python", "__init__.py" ]
#CMD ["touch", "__init__.py"]
