"""
Script to retrieve movie information for the database
Run using 'python manage.py shell' and 'from game.utils import *'
"""

import json
import requests
from bs4 import BeautifulSoup

from src.secrets import *
from .models import Movie


def get_details():
    """ Open Movie Database API to return specific information for filtering """

    mn_orig = str(input("Please enter a movie name\n>>> "))  # Take in movie name return as string
    rt_name = mn_orig.lower().replace(" ", "_")
    omdb_name = mn_orig.replace(" ", "+").lower()

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

    return director_last_name, year_filmed, actor_fn, actor_ln, mn_orig, rt_name, omdb_name


def get_reviews():
    """Grabs text for top reviews, filters them, and returns them in a list"""

    # call above function to get movie information
    d = get_details()

    # use requests to scrape html information on movie page
    raw = requests.get("http://www.rottentomatoes.com/m/{}/reviews/?type=top_critics".format(d[5]))
    soup = BeautifulSoup(raw.content, 'html.parser')
    rev = soup.find_all("div", {"class": "the_review"})        # TODO: Error/exception if review is NULL
    crit = soup.find_all("a", {"class": "unstyled bold articleLink"})

    # extract text from beautiful soup object if it has something in it
    reviews = [x.text for x in rev[:10] if len(x.text) >= 5][:5]
    critics = [x.text for x in crit[:5]]

    # filter out words that will give movie away easily
    reviews_f = [word.replace(d[4], "[Movie]")              # TODO: consider list comprehension or regex
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
    mov = Movie.objects.get(title=d[4])

    # loop to return 5 reviews and save into database
    if confirm == 'y':
        for i in range(0, 5):
            rev = mov.review_set.create(review=reviews_f[i], reviewer=critics[i])
    else:
        print("Process terminated")
        return

    return mov, d[4], d[6]


def get_similar():
    """ Use 'Taste Kid' API to return similar movies - usage limit 150 per hour """

    get = get_reviews()

    r = requests.get("https://www.tastekid.com/api/similar?q={}&k={}&type=movies&info=1&limit=5".format(get[2], tastekid_api))
    data = json.loads(r.text)

    # parsing through nested dictionary object
    dict_parse = data['Similar']['Results']
    similar = [li['Name'] for li in dict_parse]
    url = [li['yUrl'] for li in dict_parse]

    youtube = data['Similar']['Info']
    real_name = youtube[0]['Name']
    real_url = youtube[0]['yUrl']

    print("\nSimilar: {}".format(similar))
    confirm = input(str("\nIs this okay? (Y/N)"))

    # point to primary key object to properly construct similar object
    mov = Movie.objects.get(title=get[1])

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
    get_similar()

get_similar()
