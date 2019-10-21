from os import environ
from flask import Flask

# Server for Heroku
app = Flask(__name__)
app.run(host= "0.0.0.0", port=environ.get("PORT"))