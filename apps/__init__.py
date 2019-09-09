# coding=utf-8
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from .settings.dev import DevConfig
from .settings.prod import ProdConfig
from .utils.log import setup_log
from .utils.helper import get_redis_connection
from flask_script import Manager,Command
from flask_migrate import Migrate, MigrateCommand


config = {
	"dev": DevConfig,
	"prod": ProdConfig
}


# 创建数据库连接对象
db = SQLAlchemy()

def init_app(config_name):
	"""项目的初始化功能"""
	app = Flask(__name__)

	# 终端脚本工具
	app.manager = Manager(app)

	# 启用数据迁移工具
	Migrate(app, db)
	# 添加数据迁移的命令到终端脚本工具中
	app.manager.add_command('db', MigrateCommand)

	# 设置配置类
	Config = config.get(config_name)

	# 加载配置类
	Config = config.get(config_name)

	# redis的链接初始化
	app.redis = get_redis_connection(Config.REDIS.get("default"))

	# 开启session功能
	Session(app)

	# 配置数据库连接
	db.init_app(app)

	# 启动日志
	setup_log(Config)

	return app


