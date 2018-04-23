# encoding: utf-8
# 用mysql-python配置数据库相关的内容
# mysql + mysqldb://username:password@hostname/database
import os


DIALECT = 'mysql'
DRIVER = 'mysqldb'
HOSTNAME = '127.0.0.1'
DATABASE = 'math'
USERNAME = 'root'
PASSWORD = 'qazwsx'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}/{}'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOSTNAME, DATABASE)
SQLALCHEMY_COMMIT_ON_TEARDOWN = True


DEBUG = True    # 调试器始终打开
SECRET_KEY = os.urandom(24)    # 使用session时需要用到的密钥
SQLALCHEMY_TRACK_MODIFICATIONS = False    # 不需要实时监控数据库的变化

