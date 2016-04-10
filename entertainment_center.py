'''
The module sys makes it possible to parse command line arguments.
sys.argv is a list of commandline arguments
len(sys.argv) is the number of arguments
'''
import sys 

'''
The media module contains the class definition for Movie objects
'''
import media

'''
The fresh_tomatoes module contains the open_movies_page() function 
that is used to generate the .html file. The function takes a list
of Movie objects as argument.
'''
import fresh_tomatoes

'''
The xml.dom.minidom module and the parse function is used in
in this case to parse the .xml file that is passed as a command
line argument.
'''
import xml.dom.minidom
from xml.dom.minidom import parse

# Function definitions for createObjects() and parsexml()

def createObjects():

	# Checking if at least one argument has been passed
	if len(sys.argv) == 1:
		print "error: no xml file passed as argument."
		print "proper usage: python start.py file.xml"

   	elif len(sys.argv) == 2:
   		#proper usage -> create objects
   		fileName = sys.argv[1]
   		fresh_tomatoes.open_movies_page(parsexml(fileName))
   	
   	else:
   		print "error: you must pass only one xml file as argument."
		print "proper usage: python start.py file.xml"

def parsexml(xmlfile):

	listOfMovieObjects = []
	#parse the xml file passed as a command line argument
	domtree = xml.dom.minidom.parse(sys.argv[1])

	collection = domtree.documentElement
	
	movieList = collection.getElementsByTagName("movie")
	movieProperties = ["title","storyLine","image_url","trailer_youtube"]

	for movie in movieList:
	      # print movie.getElementsByTagName("title")[0]
	      movieData = []
	      for string in movieProperties:
	         attr = movie.getElementsByTagName(string)[0]
	         #print attr.childNodes[0].data
	         movieData.append(attr.childNodes[0].data)
	      newObject = media.Movie(movieData[0], movieData[1], movieData[2], movieData[3])
	      listOfMovieObjects.append(newObject)

	return listOfMovieObjects;