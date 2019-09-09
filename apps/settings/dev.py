from . import Config


class DevConfig(Config):
    """开发环境下的配置"""
    DEBUG = True
    SQLALCHEMY_ECHO = True

