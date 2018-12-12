import requests
import json
from flask import current_app

def apiTMDBCallGeneral(searchItem, searchMethod, additionalParams={}):
	params = paramBuilder(additionalParams = additionalParams, includeLang = True);
	url = current_app.config['MAIN_URL'] + '/' + current_app.config['API_VERSION'] + '/' + searchItem + '/' + searchMethod;
	response = requests.get(url, params,verify=False);
	
	if (response.status_code!=200):
		raise Exception("API Call was not completed correctly. Status Code returned:"+str(response.status_code));

	return json.loads(response.text);

def apiTMDBCallById(searchItem, itemId, itemSuffix, additionalParams={}):
	params = paramBuilder(additionalParams = additionalParams, includeLang = False);
	url = current_app.config['MAIN_URL'] + '/' + current_app.config['API_VERSION'] + '/' + searchItem + '/' + str(itemId);
	if (itemSuffix != ""):
		url = url + "/" + itemSuffix;
		
	response = requests.get(url, params,verify=False);
	
	if (response.status_code!=200):
		raise Exception("API Call was not completed correctly. Status Code returned:"+str(response.status_code));

	return json.loads(response.text);		
	
def apiIPCall(request_ip):
	url = current_app.config['API_IP_MAIN_URL'] + '/' + request_ip
	response = requests.get(url, {'access_key':current_app.config['API_KEY_IP_LOC']});
	
	if (response.status_code!=200):
		raise Exception("API Call was not completed correctly. Status Code returned:"+str(response.status_code));	
		
	return response.json();

def paramBuilder(additionalParams, includeLang):
	if (includeLang):
		standarParams = {'api_key':current_app.config['API_KEY_V3'],'language':current_app.config['API_LANGUAGE']};
	else:
		standarParams = {'api_key':current_app.config['API_KEY_V3']};
		
	urlParams = {**standarParams, **additionalParams};
	
	return urlParams;
	
