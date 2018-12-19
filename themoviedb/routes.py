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
		request_ip = request.remote_addr;
		resp = requestlib.apiIPCall(request_ip);
		for languages in resp['location']['languages']:
			session['languages'] = session['languages'] + languages['code']+ ',';
		
		if session['languages'] == '':
			session['languages'] = 'en'
		session['languages'] = session['languages'] + 'null';

################################Movies Start################################		
@themoviedb.route('/')
@themoviedb.route('/home')
@themoviedb.route('/moviesupcoming')
def moviesupcoming():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');
	dataResp = requestlib.apiTMDBCallGeneral(searchItem='movie', searchMethod='upcoming',additionalParams={"page" : curPage});
	upcomingMovies = dataResp['results'];
	upcomingMovies = transformations.appendImagePath (upcomingMovies, '', 'image_path', 'IMAGE_WIDTH_GENERAL', 'poster_path');
	totalPages = dataResp['total_pages'];
	return render_template('itemlist.html',itemdesc = 'movie',
										   itemList = upcomingMovies, 
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

	return render_template('itemlist.html',itemdesc = 'movie',
										   itemList = topRatedMovies, 
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

	return render_template('itemlist.html',itemdesc = 'movie',
										   itemList = topPopular, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviespopular',
										   pageLimit = 9,
										   pageColLimit = 3,
										   totalPages = totalPages);	
										   
@themoviedb.route('/moviedesc')
def moviedesc():
	curPage = 1 if request.args.get('simMoviescurPage') is None else request.args.get('simMoviescurPage');
	
	movieInfo = requestlib.apiTMDBCallById(searchItem='movie', itemId = request.args.get('itemid'), itemSuffix='',additionalParams={'append_to_response':'images,videos','include_image_language':session['languages']});
	movieInfo = transformations.appendImagePath (movieInfo, 'images.posters;images.backdrops', 'image_path;image_path', 'IMAGE_WIDTH_DETAIL;IMAGE_WIDTH_DETAIL', 'file_path;file_path');
	movieInfo = transformations.appendVideoPath (movieInfo, 'videos.results', 'video_path', 'site', 'key');
	
	credits = requestlib.apiTMDBCallById(searchItem='movie', itemId = request.args.get('itemid'), itemSuffix='credits');
	credits = transformations.appendImagePath (credits, 'cast;crew', 'image_path;image_path', 'IMAGE_WIDTH_LOGO;IMAGE_WIDTH_LOGO', 'profile_path;profile_path');
	
	similarResp = requestlib.apiTMDBCallById(searchItem='movie', itemId = request.args.get('itemid'), itemSuffix='similar');
	totalPages = similarResp['total_pages'];
	similar = similarResp['results'];
	similar = transformations.appendImagePath (similar, '', 'image_path', 'IMAGE_WIDTH_SIMILAR', 'poster_path');

	return render_template('itemoverallinfo.html',	itemdesc = 'movie',
													itemInfo = movieInfo,
													credits = credits, 
													similarItems = similar,
													similarMethod = 'moviedesc',
													pagingMethod = 'similarMoviePage',
													pageParameterName = 'simMoviescurPage',
													pagingGenParameters = {'itemid':request.args.get('itemid')},
													curPage = curPage,
													pageLimit = 10,
													totalPages = totalPages);	

@themoviedb.route('/similarMoviePage')		
def similarMoviePage():
	curPage = 1 if request.args.get('simMoviescurPage') is None else request.args.get('simMoviescurPage');

	similarResp = requestlib.apiTMDBCallById(searchItem='movie', itemId = request.args.get('itemid'), itemSuffix='similar', additionalParams = {'page':curPage});
	totalPages = similarResp['total_pages'];
	similar = similarResp['results'];
	similar = transformations.appendImagePath (similar, '', 'image_path', 'IMAGE_WIDTH_SIMILAR', 'poster_path');	
	
	return render_template('similaritemshorizontal.html',	itemdesc = 'movie',
															similarItems = similar,
															similarMethod = 'moviedesc',
															pagingMethod = 'similarMoviePage',
															pageParameterName = 'simMoviescurPage',
															pagingGenParameters = {'itemid':request.args.get('itemid')},
															curPage = curPage,
															pageLimit = 10,
															totalPages = totalPages);
							

################################Movies End################################

################################TV Start################################
@themoviedb.route('/tvonair')	
def tvonair():			
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiTMDBCallGeneral(searchItem='tv', searchMethod='on_the_air',additionalParams={"page" : curPage});
	tvonair = dataResp['results'];
	tvonair = transformations.appendImagePath (tvonair, '', 'image_path', 'IMAGE_WIDTH_GENERAL', 'poster_path');
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemdesc = 'tv',
										   itemList = tvonair, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'tvdesc',
										   pagingMethod = 'tvonair',
										   pageLimit = 9,
										   pageColLimit = 3,
										   totalPages = totalPages);		

@themoviedb.route('/tvtoprated')
def tvtoprated():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiTMDBCallGeneral(searchItem='tv', searchMethod='top_rated',additionalParams={"page" : curPage});
	tvtoprated = dataResp['results'];
	tvtoprated = transformations.appendImagePath (tvtoprated, '', 'image_path', 'IMAGE_WIDTH_GENERAL', 'poster_path');
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemdesc = 'tv',
										   itemList = tvtoprated, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'tvdesc',
										   pagingMethod = 'tvtoprated',
										   pageLimit = 9,
										   pageColLimit = 3,
										   totalPages = totalPages);										   
	
@themoviedb.route('/tvpopular')
def tvpopular():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiTMDBCallGeneral(searchItem='tv', searchMethod='top_rated',additionalParams={"page" : curPage});
	tvpopular = dataResp['results'];
	tvpopular = transformations.appendImagePath (tvpopular, '', 'image_path', 'IMAGE_WIDTH_GENERAL', 'poster_path');
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemdesc = 'tv',
										   itemList = tvpopular, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'tvdesc',
										   pagingMethod = 'tvpopular',
										   pageLimit = 9,
										   pageColLimit = 3,
										   totalPages = totalPages);			
	
@themoviedb.route('/tvdesc')		
def tvdesc():
	curPage = 1 if request.args.get('simTVscurPage') is None else request.args.get('simTVscurPage');
	
	tvInfo = requestlib.apiTMDBCallById(searchItem='tv', itemId = request.args.get('itemid'), itemSuffix='',additionalParams={'append_to_response':'images,videos','include_image_language':session['languages']});
	tvInfo = transformations.appendImagePath (tvInfo, 'images.posters;images.backdrops', 'image_path;image_path', 'IMAGE_WIDTH_DETAIL;IMAGE_WIDTH_DETAIL', 'file_path;file_path');
	tvInfo = transformations.appendVideoPath (tvInfo, 'videos.results', 'video_path', 'site', 'key');
	
	credits = requestlib.apiTMDBCallById(searchItem='tv', itemId = request.args.get('itemid'), itemSuffix='credits');
	credits = transformations.appendImagePath (credits, 'cast;crew', 'image_path;image_path', 'IMAGE_WIDTH_LOGO;IMAGE_WIDTH_LOGO', 'profile_path;profile_path');
	
	similarResp = requestlib.apiTMDBCallById(searchItem='tv', itemId = request.args.get('itemid'), itemSuffix='similar');
	totalPages = similarResp['total_pages'];
	similar = similarResp['results'];
	similar = transformations.appendImagePath (similar, '', 'image_path', 'IMAGE_WIDTH_SIMILAR', 'poster_path');

	return render_template('itemoverallinfo.html',	itemdesc = 'tv',
													itemInfo = tvInfo,
													credits = credits, 
													similarItems = similar,
													similarMethod = 'tvdesc',
													pagingMethod = 'similarTVPage',
													pageParameterName = 'simTVscurPage',
													pagingGenParameters = {'itemid':request.args.get('itemid')},
													curPage = curPage,
													pageLimit = 10,
													totalPages = totalPages);
													
@themoviedb.route('/similarTVPage')		
def similarTVPage():
	curPage = 1 if request.args.get('simTVcurPage') is None else request.args.get('simTVcurPage');

	similarResp = requestlib.apiTMDBCallById(searchItem='tv', itemId = request.args.get('itemid'), itemSuffix='similar', additionalParams = {'page':curPage});
	totalPages = similarResp['total_pages'];
	similar = similarResp['results'];
	similar = transformations.appendImagePath (similar, '', 'image_path', 'IMAGE_WIDTH_SIMILAR', 'poster_path');	
	
	return render_template('similaritemshorizontal.html',	itemdesc = 'tv',
															similarItems = similar,
															similarMethod = 'moviedesc',
															pagingMethod = 'similarTVPage',
															pageParameterName = 'simTVcurPage',
															pagingGenParameters = {'itemid':request.args.get('itemid')},
															curPage = curPage,
															pageLimit = 10,
															totalPages = totalPages);													
		
################################TV End################################		
@themoviedb.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(themoviedb.root_path, 'static'),'images/favicon.ico')
	