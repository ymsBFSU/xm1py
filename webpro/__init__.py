# -*- encoding=UTF-8 -*-

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')#支持break扩展
app.config.from_pyfile('app.conf')
app.secret_key = 'xxxxxxxx'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = '/regloginpage/' #用户没有登录，自动跳到此页面

from webpro import views, models
