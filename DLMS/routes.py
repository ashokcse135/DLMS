from flask import render_template, url_for, flash, redirect
from DLMS import app
from DLMS.models import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin=Admin(app)
admin.add_view(ModelView(Librarian_t1,db.session))
admin.add_views(ModelView(Librarian_t2,db.session))
