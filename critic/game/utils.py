"""
Script to retrieve movie information for the database
Run using 'python manage.py shell' and 'from game.utils import *'
"""

import json
import requests
from bs4 import BeautifulSoup

from critic.secrets import *
from .models import Movie

# take movie name as input and return the relevant URL titles
mn_orig = str(input("Please enter a movie name\n>>> "))             # Take in movie name return as string
rt_name = mn_orig.replace(" ", "_").lower()                         # Rotten Tomatoes has '_' in between words
omdb_name = mn_orig.replace(" ", "+").lower()                       # OMDB has '+' in between words

# TODO: Filter out 'the', 'a', 'an' from search


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
    genres = movie['Genre']                                         # Genres separated in a list
    plot = movie['Plot']                                            # Movie plot

    print("\nTitle: {}\nDirector: {}\nYear: {}\nPlot: {}".format(mn_orig, director, year_filmed, plot))
    confirm = input(str("\nShall I save to the database, sir? (Y/N)")).lower()

    if confirm == 'y':
        new = Movie(title=mn_orig, director=director, year=year_filmed, description=plot, poster_url=poster_url, genre=genres)
        new.save()
    else:
        print("\nProcess terminated")
        return

    return director_last_name, year_filmed, actor_fn, actor_ln


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

    for line in reviews_f:
        print("Review: {}".format(line))
    print("Critics: {}".format(critics))

    # print("Reviews: {}\nCritics: {}".format(reviews_f, critics))
    confirm = input(str("\nIs this okay? (Y/N)"))

    # point to primary key object to properly construct review object
    mov = Movie.objects.get(title=mn_orig)

    # loop to return 5 reviews and save into database
    if confirm == 'y':
        for i in range(0, 5):
            rev = mov.review_set.create(review=reviews_f[i], reviewer=critics[i])
    else:
        print("Process terminated")
        return

    return mov


def get_similar():
    """ Use 'Taste Kid' API to return similar movies - usage limit 150 per hour """

    d = get_reviews()

    r = requests.get("https://www.tastekid.com/api/similar?q={}&k={}&type=movies&info=1&limit=5".format(omdb_name, tastekid_api))
    data = json.loads(r.text)

    # parsing through nested dictionary object
    dict_parse = data['Similar']['Results']
    similar = [li['Name'] for li in dict_parse]
    url = [li['yUrl'] for li in dict_parse]

    youtube = data['Similar']['Info']
    real_name = youtube[0]['Name']
    real_url = youtube[0]['yUrl']

    print("Similar: {}".format(similar))
    confirm = input(str("\nIs this okay? (Y/N)"))

    # point to primary key object to properly construct similar object
    mov = Movie.objects.get(title=mn_orig)

    # loop to set movie trailer urls and similar movie names to the database
    if confirm == 'y':
        sim = mov.similar_set.create(real=real_name,
                                     real_u=real_url,
                                     sim1=similar[0],
                                     url1=url[0],
                                     sim2=similar[1],
                                     url2=url[1],
                                     sim3=similar[2],           # this seems like a really dumb way to do this ...
                                     url3=url[2],
                                     sim4=similar[3],
                                     url4=url[3],
                                     sim5=similar[4],
                                     url5=url[4])
    else:
        print("Process terminated")
        return

get_similar()               # TODO: recursive, run function again
