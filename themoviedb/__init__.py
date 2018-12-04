from flask import Flask
import os

themoviedb = Flask(__name__)

from themoviedb import routes

# Setting this up here does not do anything
themoviedb.config.update({'TEMPLATES_AUTO_RELOAD': True})

# Neither does this:
themoviedb.templates_auto_reload = True
themoviedb.config.from_pyfile(os.path.join(os.path.dirname(__file__), 'static','configuration','devconfig.cfg'));


