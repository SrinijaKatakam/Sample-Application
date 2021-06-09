from flask import Flask, render_template
import pyodbc

server = 'tcp:databasetest3.database.windows.net'
database = 'test'
username = 'srinija'
password = 'Texas@123'   
driver= '{ODBC Driver 17 for SQL Server}'


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')


with pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:databasetest3.database.windows.net,1433;Database=test;Uid=srinija;Pwd=Texas@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30') as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM people")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()