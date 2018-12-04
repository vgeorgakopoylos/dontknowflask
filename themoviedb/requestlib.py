import requests
import json
from flask import current_app

	
def apiCallGeneral(searchItem, searchMethod, additionalParams={}):
	params = paramBuilder(additionalParams);
	url = current_app.config['MAIN_URL'] + '/' + current_app.config['API_VERSION'] + '/' + searchItem + '/' + searchMethod;
	response = requests.get(url, params,verify=False);
	
	if (response.status_code!=200):
		raise Exception("API Call was not completed correctly. Status Code returned:"+str(response.status_code));

	return json.loads(response.text);	

def paramBuilder(additionalParams):
	standarParams = {'api_key':current_app.config['API_KEY_V3'],'language':current_app.config['API_LANGUAGE']};
	urlParams = {**standarParams, **additionalParams};
	
	return urlParams;
	
