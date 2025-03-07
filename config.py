import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://user:password@localhost/scenario_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
