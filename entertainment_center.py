import media
import fresh_tomatoes

# Define several instances of Movie objects including specified data

rules_of_the_game = media.Movie("The Rules of the Game",
        "Rich people employ poor people in France during World War II.",
        "http://images.moviepostershop.com/rules-of-the-game-movie-poster-1939-1020421065.jpg",
        "http://www.youtube.com/watch?v=qxs4P6u1EiI")

rear_window = media.Movie("Rear Window",
        "Jimmy Stewart spies on people.",
        "http://upload.wikimedia.org/wikipedia/commons/3/38/Rear_Window_film_poster.jpg",
        "http://www.youtube.com/watch?v=6kCcZCMYw38")

goodfellas = media.Movie("Goodfellas",
        "Mobsters are friends and also they kill people.",
        "http://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
        "http://www.youtube.com/watch?v=qo5jJpHtI1Y")

rashomon = media.Movie("Rashomon", 
        "People usually lie about crimes.",
        "http://upload.wikimedia.org/wikipedia/commons/a/a7/Rashomon_poster_2.jpg",
        "http://www.youtube.com/watch?v=xCZ9TguVOIA")

annie_hall= media.Movie("Annie Hall",
        "Single guys are neurotic.",
        "http://www.woodyallenpages.com/wp-content/uploads/2012/07/untitled-2.jpeg",
        "http://www.youtube.com/watch?v=TBzHphcc2Jw")

casablanca = media.Movie("Casablanca",
        "An drunk, unhappy expat decides to stay drunk and unhappy.",
        "http://upload.wikimedia.org/wikipedia/commons/b/b3/CasablancaPoster-Gold.jpg",
        "http://www.youtube.com/watch?v=EJvlGh_FgcI")

# Load movies into array and pass to fresh_tomatoes front end
movies = [rules_of_the_game, rear_window, goodfellas, rashomon, annie_hall, casablanca]
fresh_tomatoes.open_movies_page(movies)
