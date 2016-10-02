class Video():
    """This class provides a way to store video related information.

    Attributes:
        title: A title of a video.
        duration: The duration of a video in minutes.
        storyline: The story of a video.
    """
    
    def __init__(self, title, duration, storyline):
        """Inits Video with title and duration information."""
        self.title = title
        self.duration = duration
        self.storyline = storyline
