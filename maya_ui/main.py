from flask import Flask, render_template,request,session,flash
import pandas as pd
import numpy as np
from flask_table import Table, Col
import csv
import sqlite3 as sql
import os


#building flask table for showing recommendation results
class Results(Table):
    id = Col('Id', show=False)
    title = Col('Recommendation List')

app = Flask(__name__)
app.secret_key = "maya"
#Welcome Page
@app.route('/')
def home():
   return render_template('home.html')

@app.route('/gohome')
def homepage():
    return render_template('index.html')


@app.route('/signup')
def new_user():
   return render_template('signup1.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            phonno = request.form['MobileNumber']
            email = request.form['email']
            unm = request.form['Username']
            passwd = request.form['password']
            with sql.connect("mayadb.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user(name,phono,email,username,password)VALUES(?, ?, ?, ?,?)",(nm,phonno,email,unm,passwd))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("login.html")
            con.close()


@app.route('/login')
def user_login():
   return render_template("login.html")

@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():
    if request.method=='POST':
            usrname=request.form['username']
            passwd = request.form['password']

            with sql.connect("mayadb.db") as con:
                cur = con.cursor()
                cur.execute("SELECT username,password FROM user where username=? ",(usrname,))
                account = cur.fetchall()

                for row in account:
                    database_user = row[0]
                    database_password = row[1]
                    if database_user == usrname and database_password==passwd:
                        #session['logged_in'] = True
                        return render_template('home.html')
                    else:
                        flash("Invalid user credentials")
                return render_template('login.html')


if __name__ == '__main__':
   app.run(debug = True)
