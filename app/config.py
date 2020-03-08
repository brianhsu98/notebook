import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pandapandapanda'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://localhost/notebook'

