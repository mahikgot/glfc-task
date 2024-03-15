import os

class Config:
    TESTING = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:"+os.environ.get("MYSQL_PASSWORD", "password")+"@"+os.environ.get("INSTANCE_HOST", "localhost")+":3306/task"

class ProductionConfig(Config):
    SQLALCHEMY_ECHO = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

config = {
        'production': ProductionConfig,
        'testing': TestingConfig,
        'development': DevelopmentConfig
        }

