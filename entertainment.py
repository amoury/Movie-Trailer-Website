# imports the file that serves the website & for creating objects from class Movie
import movie_zone
import media

toy_story = media.Movie("Toy story",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who"
                        " belongs to a young boy named Andy (John Morris),"
                        " sees his position as Andy's favorite toy jeopardized"
                        " when his parents buy him a Buzz Lightyear"
                        " (Tim Allen) action figure.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.poster_image_url)


avatar = media.Movie("Avatar",
                     "Humans. Sam Worthington as Jake Sully, a Marine veteran,"
                     " paralyzed from the waist down that volunteers to go to"
                     " Pandora as an avatar driver."
                     " There he falls in love with the Na'vi princess, Neytiri."
                     " He is the main protagonist of the film.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


a_beautiful_mind = media.Movie("A Beautiful Mind",
                               "A Beautiful Mind is a 2001 American"
                               " biographical drama film based on the life of"
                               " John Nash, a Nobel Laureate in Economics."
                               " The film was directed by Ron Howard,"
                               " from a screenplay written by Akiva Goldsman.",
                               "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                               "https://www.youtube.com/watch?v=aS_d0Ayjw4o")



midnight_in_paris = media.Movie("Midnight in Paris",
                                "Midnight in Paris is a 2011 American-French "
                                "romantic comedy film written and directed by",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                  "Plot. In 1947 Portland, Maine, banker Andy"
                                  " Dufresne is convicted of murdering his wife"
                                  " and her lover, and is sentenced to two"
                                  " consecutive life sentences at the Shawshank"
                                  " State Penitentiary. "
                                  "Andy is befriended by contraband smuggler, "
                                  "Ellis Redding, an inmate serving a life"
                                  " sentence.",
                                  "https://www.movieposter.com/posters/archive/main/42/MPW-21321",
                                  "https://www.youtube.com/watch?v=6hB3S9bIaco")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Jules Winnfield and Vincent Vega are two hitmen "
                           "who are out to retrieve a suitcase stolen from "
                           "their employer, mob boss Marsellus Wallace."
                           "Wallace has also asked Vincent to take his wife "
                           "Mia out a few days later when Wallace himself will"
                           " be out of town.",
                           "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=wZBfmBvvotE")
    
movies = [toy_story, avatar, a_beautiful_mind, midnight_in_paris,
shawshank_redemption, pulp_fiction]
movie_zone.open_movies_page(movies)
