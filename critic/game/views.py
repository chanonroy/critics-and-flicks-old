import random
from django.shortcuts import render
from .models import Movie, Review, Similar

# film = "Gods of Egypt" (hard coded way to test)


def index(request):
    # determine count of all movies
    m_count = Movie.objects.count()
    # hard_code_length = 500
    # find random integer for indexing
    movies_int = random.randint(1, m_count)     # could hard code length to prevent db strain
    # index movie by random primary key
    m = Movie.objects.get(id=movies_int)

    # 8 reviews in a pack, return 3
    # r = random.sample(range(1,9), 3)
    rev = m.review_set.all()[:3]
    s = m.similar_set.all()

    # http://jsfiddle.net/gpJN4/3/ -- fiddle for youtube embed (similar movies)

    context = {
        "movie": m,
        "reviews": rev,
        "similar": s
    }
    return render(request, "index.html", context)
