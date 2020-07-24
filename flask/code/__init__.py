from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_ROOT_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DATABASE')

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS MyUsers ( firstname VARCHAR(30) NOT NULL,  lastname VARCHAR(30) NOT NULL);')
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    bg_color = "red"
    if os.environ.get('APP_BACKGROUNDD_COLOR') != "" or os.environ.get('APP_BACKGROUNDD_COLOR') != None:
        bg_color = os.environ.get('APP_BACKGROUNDD_COLOR')
    return render_template('index.html', color=bg_color)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
