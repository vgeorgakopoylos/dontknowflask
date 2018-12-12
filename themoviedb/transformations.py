import json
from flask import current_app
from flask import url_for

def appendPosterPathGeneral(items):
	for item in items:
		if item['poster_path'] is not None:
			item['image_path'] = current_app.config['IMAGE_URL'] + current_app.config['IMAGE_WIDTH_GENERAL']+item['poster_path'];
			
	return items;
	
def appendPosterPathDetails(itemInfo):
	for poster in itemInfo['images']['posters']:
		if poster['file_path'] is not None:
			poster['image_path'] = current_app.config['IMAGE_URL'] + current_app.config['IMAGE_WIDTH_DETAIL']+poster['file_path'];
	
	for backdrops in itemInfo['images']['backdrops']:
		if backdrops['file_path'] is not None:
			backdrops['image_path'] = current_app.config['IMAGE_URL'] + current_app.config['IMAGE_WIDTH_DETAIL']+backdrops['file_path'];
			
	for video in itemInfo['videos']['results']:
		if video['site'].lower() == "youtube":
			video['video_path'] = current_app.config['VIDEO_PREFIX']['YOUTUBE']+video['key'];			
	
	return itemInfo;
