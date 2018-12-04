from themoviedb import themoviedb
from flask import render_template,send_from_directory,request
from themoviedb import requestlib,transformations

import os


@themoviedb.route('/')
@themoviedb.route('/home')
@themoviedb.route('/moviesupcoming',methods=['GET', 'POST'])
def moviesupcoming():
	curPage = "";
	if request.args.get('curPage') is not None:
		curPage = request.args.get('curPage');
	elif request.form.get('curPage', None) is not None :
		curPage = request.form['curPage']
	else:
		curPage = 1;
		
	dataResp = requestlib.apiCallGeneral(searchItem='movie', searchMethod='upcoming',additionalParams={"page" : curPage});
	upcomingMovies = dataResp['results'];
	upcomingMovies=transformations.upcomingMoviesTransf(upcomingMovies)
	totalPages = dataResp['total_pages'];

	return render_template('itemlist.html',itemList = upcomingMovies, 
										   maxNumOfCol = 4, 
										   curPage = curPage,
										   drilldownMethod = 'moviedesc',
										   pagingMethod = 'moviesupcoming',
										   pageLimit = 10,
										   pageColLimit = 3,
										   totalPages = totalPages);
	
@themoviedb.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(themoviedb.root_path, 'static'),'images/favicon.ico')
	
@themoviedb.route('/moviedesc')
def moviedesc():
	return "";