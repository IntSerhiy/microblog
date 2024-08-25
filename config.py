import os
basedir = os.path.abspath(os.path.abspath(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-guess'
    SQLACLHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')