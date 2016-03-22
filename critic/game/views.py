# from django.shortcuts import render_to_response
# from django.template import RequestContext
from django.shortcuts import render
from .models import Movie, Review, Similar


def index(request):
    film = "Gods of Egypt"
    m = Movie.objects.get(title=film)
    r = m.review_set.all()
    context = {
        "movie": m,
        "reviews": r
    }
    return render(request, "index.html", context)
