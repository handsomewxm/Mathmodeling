# encoding: utf-8
# 用于存放数据库模型
from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=True)

    def __init__(self, *args, **kwargs):
        id = kwargs.get("id")
        username = kwargs.get('username')
        password = kwargs.get('password')
        self.id = id
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result
