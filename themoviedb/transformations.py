import json
from flask import current_app
from flask import url_for

def upcomingMoviesTransf(relatedMovies):
	for relatedMovie in relatedMovies:
		if relatedMovie['poster_path'] is None:
			relatedMovie['poster_dom'] = '<div class="nopostercont"><img src="'+url_for('static', filename='images/noposter.jpg')+'"><div class="nopostercentered">'+relatedMovie['title']+'</div></div>';
		else:
			relatedMovie['poster_dom'] = '<img src="'+current_app.config['IMAGE_URL'] + current_app.config['IMAGE_WIDTH_GENERAL']+relatedMovie['poster_path']+'">';
			
	return relatedMovies
	
	