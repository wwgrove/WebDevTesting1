'''
Created on May 2, 2022

@author: gordie.campbell
'''
"test"

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql
from flask import request

from addflask import students

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(32))
   city = db.Column(db.String(32))
   addr = db.Column(db.String(32))
   pk = db.Column(db.String(32)) 
   
   def __init__(self, name, city, addr,pk):
       self.name = name
       self.city = city
       self.addr = addr
       self.pk = pk


app = Flask(__name__)    # Construct an instance of Flask class for our webapp
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

print('DEBUG: 23:')

@app.route('/list')
def listStuff():
    print("DEBUG INSIDE LIST: 25:")
    con = sql.connect("D:\CompSci Stuff\WebDevTesting1\database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor() 
    cur.execute("select * from students")
   
    rows = cur.fetchall(); 

    
       
    return render_template("testing1.html", rows=rows)
    
@app.route("/delete?pk=1")   
def delete():
    
    con = sql.connect("D:\CompSci Stuff\WebDevTesting1\database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor() 
    cur.execute("select * from students")
    rows = cur.fetchall(); 
    pk = request.args['pk']
    name = request.args['name']
    city = request.args['city']
    addr = request.args['addr']
       

    student = students(pk,name,city,addr)

    db.session.delete(student)
    return ("delete")


'''
@app.route('/')   # URL '/' to be handled by main() route handler
def index():
    name = 'Wonder'
    return render_template('index.html', title='Welcome',username=name)
'''
if __name__ == '__main__':  # Script executed directly?
    
    app.debug = True
    app.run()  # Launch built-in web server and run this Flask webapp
