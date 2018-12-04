from themoviedb import themoviedb
from flask import render_template,send_from_directory,request
from themoviedb import requestlib,transformations

import os


@themoviedb.route('/')
@themoviedb.route('/home')
@themoviedb.route('/moviesupcoming')
def moviesupcoming():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiCallGeneral(searchItem='movie', searchMethod='upcoming',additionalParams={"page" : curPage});
	upcomingMovies = dataResp['results'];
	upcomingMovies=transformations.appendPosterPath(upcomingMovies)
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemList = upcomingMovies, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviesupcoming',
										   pageLimit = 10,
										   pageColLimit = 3,
										   totalPages = totalPages);
										   
@themoviedb.route('/moviestoprated')
def moviestoprated():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiCallGeneral(searchItem='movie', searchMethod='top_rated',additionalParams={"page" : curPage});
	topRatedMovies = dataResp['results'];
	topRatedMovies=transformations.appendPosterPath(topRatedMovies)
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemList = topRatedMovies, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviestoprated',
										   pageLimit = 10,
										   pageColLimit = 3,
										   totalPages = totalPages);		

@themoviedb.route('/moviespopular')
def moviespopular():
	curPage = 1 if request.args.get('curPage') is None else request.args.get('curPage');

	dataResp = requestlib.apiCallGeneral(searchItem='movie', searchMethod='popular',additionalParams={"page" : curPage});
	topRatedMovies = dataResp['results'];
	topRatedMovies=transformations.appendPosterPath(topRatedMovies)
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemList = topRatedMovies, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviespopular',
										   pageLimit = 10,
										   pageColLimit = 3,
										   totalPages = totalPages);	
	
@themoviedb.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(themoviedb.root_path, 'static'),'images/favicon.ico')
	
@themoviedb.route('/moviedesc')
def moviedesc():
	return "";