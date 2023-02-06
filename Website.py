from flask import Flask, render_template, request
import sys
import sqlite3 as sql
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("hello.html")

@application.route('/user_form')
def new_user():
    return render_template('user.html')

@application.route('/user_info',methods = ['POST', 'GET'])
def user_info():
    if (request.method == 'POST'):
        user_email = request.form['user_email']
        user_name = request.form['user_name']

    with sql.connect("database.db") as con:
        cur = con.cursor()

    cur.execute("INSERT INTO users (email, name) VALUES (?,?)",(user_email,user_name) )

    msg = "Success"
    return render_template("result.html",msg = msg)

@application.route('/list')
def list():
    con = sql.connect("database.db") #database.db파일에 접근.
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from users")

    rows = cur.fetchall()
    return render_template("list.html",rows = rows)

if __name__ == "__main__":
    application.run(host='0.0.0.0')