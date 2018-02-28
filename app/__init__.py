from flask import Flask
from config import Config

app2 = Flask(__name__)
app2.config.from_object(Config)

from app import routes
