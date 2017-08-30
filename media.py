class Movie():
    """This class provides a way to store movie related information"""
    def __init__(self, title, poster_image, trailer_youtube):
    	"""This init function takes in a title, poster image, and youtube trailer. It then creates a Movie instance from the data passed to it."""
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
