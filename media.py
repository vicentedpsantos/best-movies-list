class Movie():
    """class returns an object Movie

    Arguments are:
    -> Title of the movie
    -> Brief Storyline of the movie
    -> Link to poster image
    -> Link to official trailer on Youtube"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
