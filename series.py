import webbrowser
from video_info import *

class TvShow(Video):
    """This class provides a way to store TV Show related information.

    Attributes:
        title: A string indicating a title of a TV show.
        duration: An integer indicating a duration of a TV show in minutes.
        storyline: A string indicating the story of a TV show.
        season: An integer indicating a season of a TV show.
        episode: An integer indicating an episode of a TV show.
        tvshow_poster: A string indicating a url with the TV show poster.
        tv_station: A string indicating a url with TV station listing where the TV show is aired.
    """

    def __init__(self, title, duration, storyline, season, episode, tvshow_poster, tv_station):
        """Inits TvShow with title, duration, season, episode, and tv_station information."""
        Video.__init__(self, title, duration, storyline)
        self.season = season
        self.episode = episode
        self.tvshow_poster = tvshow_poster
        self.tv_station = tv_station

    def get_local_listing(self):
        """Performs operation to open url YouTube trailer in browser."""
        webbrowser.open(self.tv_station)
