#/usr/bin/python
import webbrowser

class Movie():

	"""This class provides a way to store movie related information"""

	#class variable
	# capitalized for constant variable accordings to Google code standard
	VALID_RATINGS = ["G","PG","PG-13","R"]

#init reserved in python so add __, create space in memory 
#to remember instance we are going to create
# __init__ == constructor, construct a memory space for instance created

	def __init__(self, movie_title, movie_storyline,poster_image, 
		trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

		# if "self" removed, the storyline becomes from instance variable 
		#into local variable (only can be accessed inside Movie class)
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)