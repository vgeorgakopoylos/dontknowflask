import json
from flask import current_app
from flask import url_for

def appendPosterPath(items):
	for item in items:
		if item['poster_path'] is None:
			item['poster_dom'] = '<div class="nopostercont"><img src="'+url_for('static', filename='images/noposter.jpg')+'"><div class="nopostercentered">'+item['title']+'</div></div>';
		else:
			item['poster_dom'] = '<img src="'+current_app.config['IMAGE_URL'] + current_app.config['IMAGE_WIDTH_GENERAL']+item['poster_path']+'">';
			
	return items;
	
	