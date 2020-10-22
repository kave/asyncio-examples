import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, verbose=True)

# Server
HOST = os.environ.get('HOST', "127.0.0.1")
PORT = int(os.environ.get('PORT', 9000))
