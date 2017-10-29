"""This module stores classes for media objects, like Movie, Video, Show"""

class Movie(object):
    '''A class for a basic high-level abstraction on a movie and key web links'''

    def __init__(self, title, description, poster_image_url, trailer_youtube_url):
        self.title = title
        self.description = description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def getmoviesummaries(self, movie):
        '''Returns the a title and Description of the movie'''
        return str.format("Title: {0} - Description: {1}", movie.title, movie.description)
