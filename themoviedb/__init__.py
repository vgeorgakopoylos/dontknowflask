from flask import Flask
import os
from os import environ

themoviedb = Flask(__name__)

from themoviedb import routes

# Setting this up here does not do anything
themoviedb.config.update({'TEMPLATES_AUTO_RELOAD': True})

# Neither does this:
themoviedb.templates_auto_reload = True
themoviedb.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'static','configuration','devconfig.cfg'));


if __name__ == 'themoviedb':
	themoviedb.secret_key = themoviedb.config['SESSION_SECRET_KEY'] 
	themoviedb.run(host='0.0.0.0',port= environ.get("PORT", 5000))
