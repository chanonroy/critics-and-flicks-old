import re
import requests
from bs4 import BeautifulSoup

# take movie name as input and return the relevant URL titles
mn_orig = str(input("Please enter a movie name\n>>> "))             # Take in
rt_name = mn_orig.replace(" ", "_").lower()                         # Rotten Tomatoes has '_' in between words
omdb_name = mn_orig.replace(" ", "+").lower()                       # OMDB has '+' in between words


def get_details():
    """ Open Movie Database API to return specific information for filtering """
    raw = requests.get("http://www.omdbapi.com/?t={}&r=json".format(omdb_name))
    # Keys: "Title", "Year", "Released", "Genre", "Director", "Actors", "Plot", "Poster" (300px image)

    movie = raw.json()
    director = movie['Director'].split(",")[0]                      # Director's Full Name
    director_last_name = director.split(" ")[1]                     # Director's Last Name
    actor = movie['Actors'].split(",")[0]                           # Main Actor's Full Name
    actor_fn = actor.split(" ")[0]                                  # Actor First name
    actor_ln = actor.split(" ")[1]                                  # Actor Last Name
    year_filmed = movie['Year']                                     # Year of film release
    poster_url = movie['Poster']                                    # URL for image of poster
    genres = movie['Genre'].split(",")                              # Genres separated in a list
    imdb = movie['imdbID']                                          # IMDb ID

    return director_last_name, year_filmed, actor_fn, actor_ln, poster_url, genres, imdb


def get_reviews():
    """Grabs text for top reviews, filters them, and returns them in a list"""
    # use requests to scrape html information on movie page
    raw = requests.get("http://www.rottentomatoes.com/m/{}/reviews/?type=top_critics".format(rt_name))
    soup = BeautifulSoup(raw.content, 'html.parser')
    rev = soup.find_all("div", {"class": "the_review"})        # TODO: Error/exception if review is NULL
    crit = soup.find_all("a", {"class": "unstyled bold articleLink"})

    # extract text from beautiful soup object
    reviews = [x.text for x in rev[0:5]]                       # TODO: consider dictionary format for key:value pair
    critics = [x.text for x in crit[0:5]]

    # call above function to get movie information
    d = get_details()

    # filter out words that will give movie away easily
    reviews_f = [word.replace(mn_orig, "[Movie]")              # TODO: consider list comprehension or regex
                     .replace(d[0], "[Director]")
                     .replace(d[1], "[Date]")
                     .replace(d[2], "[Actor First Name]")
                     .replace(d[3], "[Actor Name]") for word in reviews]

    return reviews_f, critics


def get_similar(imdb):
    # raw = requests.get("http://www.imdb.com/title/{}/".format(imdb))
    # soup = BeautifulSoup(raw.content, 'html.parser')
    # sim = soup.find_all("div", {"class": "rec-title"})
    # similar = [x.text for x in sim[0:5]]                # '\nRiddick\n(2013)\n', '\nElysium\nI\n(2013)\n', '\nRoboCop\n(2014)\n'

    similar = ['\nRiddick\n(2013)\n', '\nElysium\nI\n(2013)\n', '\nRoboCop\n(2014)\n']
    simnew = re.match(r"\[([A-Za-z0-9_]+)\]", similar)

    # print(similar)

get_similar('tt1731141')

# get_reviews()
