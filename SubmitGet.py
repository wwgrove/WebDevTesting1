'''
Created on May 2, 2022

@author: gordie.campbell
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql




app = Flask(__name__)    # Construct an instance of Flask class for our webapp
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


#@app.route('/index')
@app.route('/submit')
def submit():
    return render_template('sample_form_input.html', title='Submit Code')

@app.route('/submit_get')   
def submit_get():
   
    if request.method == "GET":
       # getting input with name = fname in HTML form
       first_name = request.args['fname']
       # getting input with name = lname in HTML form 
       last_name = request.args['lname']
       
       
    
       
       return "Your name is "+ first_name + ' ' + last_name
   
   
   

if __name__ == '__main__':  # Script executed directly?
    
    app.debug = True
    app.run()  # Launch built-in web server and run this Flask webapp