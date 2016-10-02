import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 50px;
            padding: 20px;
        }
        .movie-tile:hover {
            background-color: #CCC;
            cursor: pointer;
            border-radius: 25px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;          
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .movie-container {
            background-color: #EEE;
            border-radius: 25px;
            margin: 40px;
            padding: 20px;        
        }
        h1 {
          text-align: center;
          padding-bottom: 10px;
        }
        .tvshow-container {
            background-color: #EEE;
            border-radius: 25px;
            margin: 40px;
            padding: 20px;        
        }
        .hover_info {
            visibility: hidden;
        }
        span:hover + div {
            visibility: visible;
        }
        .tvshow-tile {
            margin-bottom: 50px;
            padding: 20px;
        }
        .tvshow-tile:hover {
            background-color: #CCC;
            cursor: pointer;
            border-radius: 25px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Go to tv listings whenever the tv station modal is opened
        $(document).on('click', '.tvshow-tile', function (event) {
            var sourceUrl = $(this).attr('tvshow-stations');
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
          $('.tvshow-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie and TV Show</a>
          </div>
        </div>
      </div>
    </div>
    <div class="movie-container">
        <h1>Movies</h1>
        <div class="container">
          {movie_tiles}
        </div>
    </div>
    <div class="tvshow-container">
        <h1>TV Shows</h1>
        <div class="container">
          {series_tiles}
        </div>
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <span><img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2></span>
    <div class="hover_info">{movie_storyline} <br> Duration: {movie_duration} min</div>
</div>
'''

# A single TV show entry html template
tvshow_tile_content = '''
<div class="col-md-6 col-lg-4 tvshow-tile text-center" tvshow-stations="{tvshow_listings}" data-toggle="modal" data-target="#trailer">
    <span><img src="{poster_image}" width="220" height="342">
    <h2>{tvshow_title}</h2></span>
    <div class="hover_info">{tvshow_storyline} <br> Season {tvshow_season} Episode {tvshow_episode} <br> Duration: {tvshow_duration} min</div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.youtube_trailer)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.youtube_trailer)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image,
            trailer_youtube_id=trailer_youtube_id,
            movie_duration=movie.duration,
            movie_storyline=movie.storyline
        )
    return content

def create_tvshow_tiles_content(series):
    # The HTML content for this section of the page
    content = ''
    tvshow_listings = ''
    for tvshow in series:
        # Append the tile for the tvshow with its content filled in
        content += tvshow_tile_content.format(
            tvshow_title=tvshow.title,
            tvshow_storyline=tvshow.storyline,
            tvshow_duration=tvshow.duration,
            poster_image=tvshow.tvshow_poster,
            tvshow_season=tvshow.season,
            tvshow_episode=tvshow.episode,
            tvshow_listings=tvshow.tv_station
        )
    return content

def open_movies_page(movies, series):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        series_tiles=create_tvshow_tiles_content(series)
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
