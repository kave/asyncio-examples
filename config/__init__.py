import os
from distutils.util import strtobool
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, verbose=True)

# Server
HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))
ENV = os.environ.get('ENV')
IS_LOCAL = ENV == 'local'
IS_HEROKU = ENV == 'heroku'
DEBUG = strtobool(os.environ.get('DEBUG'))

# Databases
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_DATABASE = os.environ.get('DB_DATABASE')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
