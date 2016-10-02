import media
import series
import fresh_tomatoes

#Call Movie constructor to create Captain America: Civil War movie object.
civil_war = media.Movie("Captain America: Civil War",
                        147,
                        "Avengers split into two groups",
                        "http://www.joblo.com/timthumb.php?src=/posters/images/full/Captain-America-Civil-War-main-poster.jpg&h=600&q=100",
                        "https://www.youtube.com/watch?v=dKrVegVI0Us")

#Call Movie constructor to create Avatar movie object.
avatar = media.Movie("Avatar",
                     162,
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

#Call Movie constructor to create Harry Potter and the Order of the Phoenix movie object.
harry_potter = media.Movie("Harry Potter and the Order of the Phoenix",
                           138,
                           "A wizard is targeted by evil forces",
                           "http://www.tribute.ca/harrypotter/images/HP5/harry_potter_and_the_order_of_the_phoenix_poster2.jpg",
                           "https://www.youtube.com/watch?v=y6ZW7KXaXYk")

#Call Movie constructor to create Star Trek Beyond movie object.
star_trek = media.Movie("Star Trek Beyond",
                        122,
                        "Crew explores space",
                        "http://www.impawards.com/2016/posters/star_trek_beyond_ver2.jpg",
                        "https://www.youtube.com/watch?v=Tvq3y8BhZ2s")

#Call Movie constructor to create Star Wars The Force Awakens movie object.
star_wars = media.Movie("Star Wars The Force Awakens",
                        138,
                        "Resistance vs First Order",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/6/2015/10/star-wars-force-awakens-official-poster-691x1024.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

#Call Movie constructor to create Warcraft movie object.
warcraft = media.Movie("Warcraft",
                       123,
                       "Orcs invade the human lands",
                       "http://static.srcdn.com/slir/w800-h1186-q90-c800:1186/wp-content/uploads/warcraft-movie-2016-poster.jpg",
                       "https://www.youtube.com/watch?v=RhFMIRuHAL4")

#Call TvShow constructor to create Game of Thrones tv show object.
game_of_thrones = series.TvShow("Game of Thrones",
                                56,
                                "Civil war between noble families",
                                6,
                                10,
                                "http://www.eonline.com/eol_images/Entire_Site/2015127/rs_634x939-150227131719-634-game-of-thrones.ls.22715.jpg",
                                "http://www.tvguide.com/tvshows/game-of-thrones/episodes/305628/")

#Call TvShow constructor to create Supernatural tv show object.
supernatural = series.TvShow("Supernatural",
                             44,
                             "Two brothers fight evil supernatural beings",
                             11,
                             23,
                             "https://nerdophiles.files.wordpress.com/2014/09/season-9-promo-poster.jpg",
                             "http://www.tvguide.com/tvshows/supernatural/episodes-season-11/192272/")

#Call TvShow constructor to create Marvel's Daredevil tv show object.
daredevil = series.TvShow("Marvel's Daredevil",
                          54,
                          "Hero delivers justice to Hell's Kitchen",
                          2,
                          13,
                          "http://i.annihil.us/u/prod/marvel/i/mg/3/e0/5519b41765e9b.jpg",
                          "http://www.tvguide.com/tvshows/marvels-daredevil/episodes/665130/")

#Movie list data structure.
movies = [warcraft, civil_war, harry_potter, star_trek, star_wars, avatar]

#TV Show list data structure.
series = [game_of_thrones, supernatural, daredevil]

#Build the HTML file and display website.
fresh_tomatoes.open_movies_page(movies, series)
