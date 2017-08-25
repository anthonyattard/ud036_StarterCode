import fresh_tomatoes
import media

# Creates movie instances
fight_club = media.Movie("Fight Club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

waking_life = media.Movie("Waking Life",
                          "https://upload.wikimedia.org/wikipedia/en/9/98/Waking-Life-Poster.jpg",
                          "https://www.youtube.com/watch?v=xX10vQEa56E")

before_sunrise = media.Movie("Before Sunrise",
                          "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
                          "https://www.youtube.com/watch?v=9v6X-Dytlko")

the_big_short = media.Movie("The Big Short",
                          "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
                          "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

the_conjuring = media.Movie("The Conjuring",
                          "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
                          "https://www.youtube.com/watch?v=DtC1hTw7Rto")


# Puts all of the movie instances into 1 list
movies = [fight_club, shawshank_redemption, waking_life, before_sunrise, the_big_short, the_conjuring]
# Passes the list of movies to fresh_tomatoes to be processed
fresh_tomatoes.open_movies_page(movies)
