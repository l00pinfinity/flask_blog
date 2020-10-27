#flask_blog/config.py

SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_blog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = 'secret key'  #for greater security,use longer random values in production
USERNAME = 'loop'
PASSWORD = 'loop123'
