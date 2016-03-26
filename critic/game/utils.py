import requests
from bs4 import BeautifulSoup


mn_orig = str(input("Please enter a movie name\n>>> "))             # Movie Name
rt_name = mn_orig.replace(" ", "_").lower()                         # Rotten Tomatoes has '_' in between
omdb_name = mn_orig.replace(" ", "+").lower()                       # OMDB wants '+' in between


def get_details():
    """ Open Movie Database API to return specific information for filtering """
    raw = requests.get("http://www.omdbapi.com/?t=" + omdb_name + "&r=json")
    # Keys: "Title", "Year", "Released", "Genre", "Director", "Actors", "Plot", "Poster" (300px image)
    movie = raw.json()
    director = movie['Director'].split(",")[0]                      # Director's Full Name
    director_last_name = director.split(" ")[1]                     # Director's Last Name
    actor = movie['Actors'].split(",")[0]                           # Main Actor's Full Name
    actor_fn = actor.split(" ")[0]                                  # Actor First name
    actor_ln = actor.split(" ")[1]                                  # Actor Last Name
    year_filmed = movie['Year']                                     # Year of film release
    poster_url = movie['Poster']                                    # URL for image of poster
    genres = movie['Genre'].split(",")

    return director_last_name, year_filmed, actor_fn, actor_ln, poster_url, genres


def get_reviews():
    """Grabs text for top reviews, filters them, and returns them in a list"""
    review_url = "http://www.rottentomatoes.com/m/" + rt_name + "/reviews/?type=top_critics"
    r = requests.get(review_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rev = soup.find_all("div", {"class": "the_review"})
    crit = soup.find_all("a", {"class": "unstyled bold articleLink"})

    # consider dictionary format for key:value pair
    reviews = [x.text for x in rev[0:5]]
    critics = [x.text for x in crit[0:5]]

    d = get_details()

    reviews_f = [word.replace(mn_orig, "[Movie]")              # consider list comprehension or regex
                     .replace(d[0], "[Director]")
                     .replace(d[1], "[Date]")
                     .replace(d[2], "[Actor First Name]")
                     .replace(d[3], "[Actor Name]") for word in reviews]

    return reviews_f, critics


def get_similar():
    """  """
    pass
    # grab IMDb id from OMDB
    #

# get_reviews()
