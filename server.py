from os import environ
from flask import Flask

# Server for Heroku
#app = Flask(__carti__)
app.run(environ.get('PORT'))