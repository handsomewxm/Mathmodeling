# encoding: utf-8

from flask import Flask, render_template, request, redirect, url_for, session,g
import config
# from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager   # Manager 用于存放终端命令
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)      # 将数据库的配置文件绑定到app
# manager = Manager(app)
# db = SQLAlchemy(app)
db.init_app(app)   # 将数据库模型初始化

# @app.route('/')
# def home():
#     return render_template('home.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/file_submit/')
def file_submit():
    return render_template('file_submit.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/regist/',methods=['GET', 'POST'])
def regist():
    if request.method == "GET":
        return render_template('regist.html')
    else:
        id = request.form.get('id')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


@app.route('/score_details/')
def score_details():
    return render_template('score_details.html')


if __name__ == '__main__':
    app.run()
