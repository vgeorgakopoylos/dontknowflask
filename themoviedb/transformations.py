import json
from flask import current_app
from flask import url_for

#old function replaced by appendImagePath
def appendPosterPathGeneral(items):
	for item in items:
		if item['poster_path'] is not None:
			item['image_path'] = current_app.config['IMAGE_URL'] + current_app.config['IMAGE_WIDTH_GENERAL']+item['poster_path'];
		
	return items;
	
#old function replaced by appendImagePath and 	appendVideoPath
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

def appendImagePath (items, loopPaths, appendedKey, imageWidth, targetKeyValue):
	loopPathsSplitted = loopPaths.split(';');
	appendedKeySplitted = appendedKey.split(';');
	imageWidthSplitted = imageWidth.split(';');
	targetKeyValueSplitted = targetKeyValue.split(';');
	idx = 0;
	for loopPath in loopPathsSplitted:
		tempLoopPath = '';
		
		if loopPath != '':
			for loopKey in loopPath.split('.'):
				tempLoopPath =  tempLoopPath + '[\''+loopKey+'\']';	
				
		codeBlock = '''for item in items'''+tempLoopPath+''': 
						if item[\''''+targetKeyValueSplitted[idx]+'''\'] is not None: 
							item[\''''+appendedKeySplitted[idx]+'''\'] = current_app.config[\'IMAGE_URL\'] + current_app.config[\''''+imageWidthSplitted[idx]+'''\'] + item[\''''+targetKeyValueSplitted[idx]+'''\'];'''
		execCodeObject = compile(codeBlock ,'<string>', 'exec');				
		exec(execCodeObject);
		idx += 1;
	return items;
	
def appendVideoPath (items, loopPaths, appendedKey, siteKey, targetKeyValue):	
	loopPathsSplitted = loopPaths.split(';');
	appendedKeySplitted = appendedKey.split(';');
	siteKeySplitted = siteKey.split(';');
	targetKeyValueSplitted = targetKeyValue.split(';');
	idx = 0;
	for loopPath in loopPathsSplitted:
		tempLoopPath = '';
		
		if loopPath != '':
			for loopKey in loopPath.split('.'):
				tempLoopPath =  tempLoopPath + '[\''+loopKey+'\']';	

		codeBlock = '''for item in items'''+tempLoopPath+''': 
						if item[\''''+siteKeySplitted[idx]+'''\'].lower() == \'youtube\': 
							item[\''''+appendedKeySplitted[idx]+'''\'] = current_app.config[\'VIDEO_PREFIX\'][\'YOUTUBE\']+item[\''''+targetKeyValueSplitted[idx]+'''\'];''';
		execCodeObject = compile(codeBlock ,'<string>', 'exec')				
		exec(execCodeObject);
		idx += 1;
	return items;	
	
	
	
	
	