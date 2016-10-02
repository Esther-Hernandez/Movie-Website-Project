import webbrowser
from video_info import *

class Movie(Video):
    """This class provides a way to store movie related information.

    Attributes:
        title: A string indicating a title of a movie.
        duration: An float indicating a duration of a movie in minutes.
        storyline: A string indicating a storyline of a movie.
        poster_image: A string indicating a url path for the poster image of a movie.
        youtube_trailer: A string indicating a url path for the YouTube trailer of a movie.
    """
    
    def __init__(self, title, duration, storyline, poster_image, youtube_trailer):
        """Inits Movie with title, duration, story, poster image url, and YouTube trailer url information."""
        Video.__init__(self, title, duration, storyline)
        self.poster_image = poster_image
        self.youtube_trailer = youtube_trailer

    def show_trailer(self):
        """Performs operation to open url YouTube trailer in browser."""
        webbrowser.open(self.youtube_trailer)

        
