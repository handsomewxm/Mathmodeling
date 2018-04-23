# encoding: utf-8   # 用来写命令的

from flask_script import Manager   # Manager 用于存放终端命令
from flask_migrate import MigrateCommand, Migrate  # 模型到表的迁移
from math import app
from exts import db
from models import User
# 导入数据库模型


manager = Manager(app)
migrate = Migrate(db)    # 使用Migrate绑定app和db
manager.add_command('db', MigrateCommand)   # 添加迁移脚本的命令到manager中


if __name__ == '__main__':
    manager.run()       # 执行终端存放的命令