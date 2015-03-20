import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def print_title(self):
        print self.title
    
class Movie(Video):
    """ This class provides a way to store movie related information, including data that is used to support the fresh_tomatoes front end."""
    
    valid_ratings = ["G", "PG", "PG-13", "R"]

    # Initialize Each Instance using the Passed Data; unless 
    # otherwise specified, the initialized values will default 
    # to an empty string
    def __init__(self, title="", storyline="", poster_image="", trailer_youtube="", rating="", duration=0):
        
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        # Set the Rating to the passed rating; set to NR if not specified
        if rating in self.valid_ratings:
            self.rating = rating
        else:
            rating = "NR"

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)

