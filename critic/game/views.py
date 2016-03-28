import random
from django.shortcuts import render
from .models import Movie


def index(request):

    # random movie from database (TODO: refactor)
    m_count = 60    # hardcoded to avoid costly counting operation
    movies_int = random.randint(0, m_count)
    m = Movie.objects.all()[movies_int - 1]                     # alt = Movie.objects.get(title=movie) - with text file

    # random reviews from database
    r = random.sample(range(0, 5), 3)
    rev = m.review_set.all()
    reviews = [rev[r[0]], rev[r[1]], rev[r[2]]]

    # Similar movies dictionary object (key=title, value=youtube url)
    # (TODO: return 2 out of 5 similar with main included)
    t = m.similar_set.values()
    t = t[0]
    sim = {t['real']: t['real_u'], t['sim1']: t['url1'], t['sim2']: t['url2'], t['sim3']: t['url3'],
           t['sim4']: t['url4'], t['sim5']: t['url5']}
    # TODO: add html class in the value for key (main movie)

    context = {
        "movie": m,
        "reviews": reviews,
        "similar": sim
    }
    return render(request, "game/game.html", context)

# http://stackoverflow.com/questions/1602557/display-django-values-on-foreign-key-in-template-as-object-instead-of-its-id
# http://stackoverflow.com/questions/27180190/django-using-objects-values-and-get-foreignkey-data-in-template

