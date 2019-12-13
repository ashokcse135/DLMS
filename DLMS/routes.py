from flask import render_template, url_for, flash, redirect
from DLMS import app
from DLMS.models import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin=Admin(app)
admin.add_view(ModelView(Librarian_t1,db.session))
admin.add_views(ModelView(Librarian_t2,db.session))


@app.route('/')
@app.route('/home')
def home():
    return  render_template('home.html')

@app.route('/404.html')
def error():
    return  render_template('404.html')

@app.route('/blank.html')
def blank():
    return  render_template('blank.html')

@app.route('/buttons.html')
def buttons():
    return  render_template('buttons.html')

@app.route('/cards.html')
def cards():
    return  render_template('cards.html')

@app.route('/charts.html')
def charts():
    return  render_template('charts.html')

@app.route('/forgot-password.html')
def forgot():
    return  render_template('forgot-password.html')

@app.route('/index.html')
def index():
    return  render_template('index.html')

@app.route('/login.html')
def login():
    return  render_template('login.html')

@app.route('/register.html')
def register():

    return  render_template('register.html')

@app.route('/tables.html')
def tables():
    return  render_template('tables.html')

@app.route('/utilities-animation.html')
def animation():
    return  render_template('utilities-animation.html')

@app.route('/utilities-border.html')
def border():
    return  render_template('utilities-border.html')

@app.route('/utilities-color.html')
def color():
    return  render_template('utilities-color.html')

@app.route('/utilities-other.html')
def other():
    return  render_template('utilities-other.html')












