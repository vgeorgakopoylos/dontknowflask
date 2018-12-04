class Movie(object):
	movie_id = None;
	title = None;
	poster_path = None;
	backdrop_path = None;
	video = None;
	overview = None;
	
	def __init__(self, movie_id, title, poster_path, backdrop_path, video, overview):
		self.movie_id = movie_id;
		self.title = title;
		self.poster_path = poster_path;
		self.backdrop_path = backdrop_path;
		self.video = video;
		self.overview = overview;

class UpcomingMovie(object):	
	movies = [];