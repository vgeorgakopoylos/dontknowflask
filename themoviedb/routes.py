from themoviedb import themoviedb
from flask import render_template,send_from_directory,request, session
from themoviedb import requestlib,transformations
import os
from flask import jsonify
import datetime


@themoviedb.before_request
def set_parameters():
	if 'languages' not in session:
		session['languages'] = '';
		request_ip = '213.249.40.200';#request.remote_addr;
		resp = requestlib.apiIPCall(request_ip);
		for languages in resp['location']['languages']:
			session['languages'] = session['languages'] + languages['code']+ ',';
		
		if session['languages'] == '':
			session['languages'] = 'en'
		session['languages'] = session['languages'] + 'null';

@themoviedb.route('/')
@themoviedb.route('/home')
@themoviedb.route('/moviesupcoming')
def moviesupcoming():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');
	dataResp = requestlib.apiTMDBCallGeneral(searchItem='movie', searchMethod='upcoming',additionalParams={"page" : curPage});
	upcomingMovies = dataResp['results'];
	upcomingMovies = transformations.appendImagePath (upcomingMovies, '', 'image_path', 'IMAGE_WIDTH_GENERAL', 'poster_path');
	totalPages = dataResp['total_pages'];
	return render_template('itemlist.html',itemList = upcomingMovies, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviesupcoming',
										   pageLimit = 9,
										   pageColLimit = 3,
										   totalPages = totalPages);
										   
@themoviedb.route('/moviestoprated')
def moviestoprated():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiTMDBCallGeneral(searchItem='movie', searchMethod='top_rated',additionalParams={"page" : curPage});
	topRatedMovies = dataResp['results'];
	topRatedMovies = transformations.appendImagePath (topRatedMovies, '', 'image_path', 'IMAGE_WIDTH_GENERAL', 'poster_path');
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemList = topRatedMovies, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviestoprated',
										   pageLimit = 9,
										   pageColLimit = 3,
										   totalPages = totalPages);		

@themoviedb.route('/moviespopular')
def moviespopular():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiTMDBCallGeneral(searchItem='movie', searchMethod='popular',additionalParams={"page" : curPage});
	topPopular = dataResp['results'];
	topPopular = transformations.appendImagePath (topPopular, '', 'image_path', 'IMAGE_WIDTH_GENERAL', 'poster_path');
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemList = topPopular, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviespopular',
										   pageLimit = 10,
										   pageColLimit = 3,
										   totalPages = totalPages);	
										   
@themoviedb.route('/moviedesc')
def moviedesc():
	movieInfo = requestlib.apiTMDBCallById(searchItem='movie', itemId = request.args.get('itemid'), itemSuffix='',additionalParams={'append_to_response':'images,videos','include_image_language':session['languages']});
	movieInfo = transformations.appendImagePath (movieInfo, 'images.posters;images.backdrops', 'image_path;image_path', 'IMAGE_WIDTH_DETAIL;IMAGE_WIDTH_DETAIL', 'file_path;file_path');
	movieInfo = transformations.appendVideoPath (movieInfo, 'videos.results', 'video_path', 'site', 'key');
	
	credits = requestlib.apiTMDBCallById(searchItem='movie', itemId = request.args.get('itemid'), itemSuffix='credits');
	credits = transformations.appendImagePath (credits, 'cast;crew', 'image_path;image_path', 'IMAGE_WIDTH_LOGO;IMAGE_WIDTH_LOGO', 'profile_path;profile_path');
	
	return render_template('itemoverallinfo.html',itemInfo = movieInfo, credits = credits);	
	

@themoviedb.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(themoviedb.root_path, 'static'),'images/favicon.ico')
	