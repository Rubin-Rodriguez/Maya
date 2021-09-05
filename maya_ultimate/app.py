from flask import Flask, render_template, request, session, flash
import sqlite3 as sql
import os
import pandas as pd
import csv
from collections import defaultdict
import numpy as np
from scipy.signal import *
from numpy.fft import *
from scipy import *
import mne
import random
import pandas as pd
import random
from pylab import *

app = Flask(__name__)

@app.route('/')
def home():
    session['logged_in'] = False
    return render_template('index.html')

@app.route('/gohome')
def homepage():
    return render_template('index.html')

@app.route('/homepage')
def resulthome():
    if session['logged_in']:
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/enternew')
def new_user():
   return render_template('signup.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        name = request.form['Name']
        phonno = request.form['MobileNumber']
        email = request.form['email']
        user = request.form['Username']
        passwd = request.form['password']
        import maya_ultimate.Signup as signup
        msg = signup.signup_maya(name, phonno, email, user, passwd)
        return render_template("result.html", msg=msg)

@app.route('/userlogin')
def user_login():
   return render_template("login.html")

@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():
    if request.method == 'POST':
        import maya_ultimate.Login as login
        usrname = request.form['username']
        passwd = request.form['password']
        login_flag = login.login_maya(usrname, passwd)
        if login_flag == 1:
            session['logged_in'] = True
            return render_template('home.html')
        else:
            flash("Invalid user credentials")
            return render_template('login.html')

@app.route('/about')
def about():
    if session['logged_in']:
        return render_template('aboutus.html')
    else:
        return render_template('login.html')

@app.route('/help')
def help():
    if session['logged_in']:
        return render_template('help.html')
    else:
        return render_template('login.html')


@app.route('/predictinfo')
def predictin():
    if session['logged_in']:
        return render_template('info.html')
    else:
        return render_template('login.html')

@app.route('/predict',methods = ['POST', 'GET'])
def predcrop():
    if request.method == 'POST':

        import maya_ultimate.Mayamantra as mantra

        response, accuracy = mantra.maya_mantra()
        if response == "":

            return render_template('info.html')
        else:
            return render_template('resultpred.html', prediction=response, prediction1=accuracy)

@app.route('/predictchord')
def predictchord():
    if session['logged_in']:
        return render_template('info2.html')
    else:
        return render_template('login.html')

@app.route('/chords_predict',methods = ['POST', 'GET'])
def predchord():
    if request.method == 'POST':

        import maya_ultimate.Stringsmelody as strmel

        response, accuracy = strmel.strings_melody()
        if response == "":
            return render_template('info.html')
        else:
            return render_template('resultpred.html', prediction=response, prediction1=accuracy)


@app.route("/assist")
def assist():

    if session['logged_in']:
        import maya_ultimate.Maya as maya
        message = maya.maya_assist()
        flash("Maya Assistant Terminated")
        return render_template('home.html', response=message)
    else:
        return render_template('login.html')

@app.route("/music")
def music():

    if session['logged_in']:
        import maya_ultimate.Kukushka as kuku
        kuku.play()
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)


