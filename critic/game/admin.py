from django.contrib import admin
from .models import Movie, Review, Similar

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Similar)
