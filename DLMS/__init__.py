from flask import  Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SECRET_KEY']=b'^$z\xf7\xcd\x96\xb8\xeb)\x02\x8d\x7f\xe4[*Fp\x0c5\x9aU\x96W('
db=SQLAlchemy(app)

from DLMS import  routes
