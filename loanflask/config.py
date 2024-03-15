import os


#hahahahahahahhahahaahhaa access denied, f.read() leaves a \n causing wrong password
def get_password_compose():
    try:
        f = open("/run/secrets/db_pass")
        password = f.read().splitlines()[0]
        f.close()
        return password
    except:
        return "password"

class Config:
    TESTING = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:"+get_password_compose()+"@"+os.environ.get("INSTANCE_HOST", "localhost")+":3306/task"

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

