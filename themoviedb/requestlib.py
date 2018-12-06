import requests
import json
from flask import current_app

def apiCallGeneral(searchItem, searchMethod, additionalParams={}):
	params = paramBuilder(additionalParams = additionalParams, includeLang = True);
	url = current_app.config['MAIN_URL'] + '/' + current_app.config['API_VERSION'] + '/' + searchItem + '/' + searchMethod;
	response = requests.get(url, params,verify=False);
	
	if (response.status_code!=200):
		raise Exception("API Call was not completed correctly. Status Code returned:"+str(response.status_code));

	return json.loads(response.text);

def apiCallById(searchItem, itemId, itemSuffix, additionalParams={}):
	params = paramBuilder(additionalParams = additionalParams, includeLang = False);
	url = current_app.config['MAIN_URL'] + '/' + current_app.config['API_VERSION'] + '/' + searchItem + '/' + str(itemId);
	if (itemSuffix != ""):
		url = url + "/" + itemSuffix;
		
	response = requests.get(url, params,verify=False);
	
	if (response.status_code!=200):
		raise Exception("API Call was not completed correctly. Status Code returned:"+str(response.status_code));

	return json.loads(response.text);		

def paramBuilder(additionalParams, includeLang):
	if (includeLang):
		standarParams = {'api_key':current_app.config['API_KEY_V3'],'language':current_app.config['API_LANGUAGE']};
	else:
		standarParams = {'api_key':current_app.config['API_KEY_V3']};
		
	urlParams = {**standarParams, **additionalParams};
	
	return urlParams;
	
