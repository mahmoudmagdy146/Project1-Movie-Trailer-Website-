import webbrowser


class Movie ():
    """This Class Provides a Way To Store Movie related Informatin """
    def __init__(self, movie_title, movie_story_line, poster_img,
                 trailer_youtube):
        """ This Docstring Should Explain The Constructor Method """
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster = poster_img
        self.trailer = trailer_youtube

    def show_trailer(self):
        """ This Docstring Should Explain what the show_trailer() function
            does """
        webbrowser.open(self.trailer)
