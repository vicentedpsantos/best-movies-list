class Movie():
    """Responsible for creating Movie objects

    Parameters
    ----------
    movie_title : string
        Title of the movie
    movie_storyline : string
        Brief description of the story of the movie
    poster_image_url : string
        Link to image of official movie poster    
    trailer_youtube_url : string
        URL link to official movie trailer on YouTube

    Returns
    -------
    When instatiated, returns object of Class Movie
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
