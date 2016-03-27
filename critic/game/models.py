from django.db import models


class Movie(models.Model):
    """ Database of movies with relevant details """
    title = models.CharField(max_length=80)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=5)
    description = models.TextField()
    poster_url = models.CharField(max_length=200)
    genre = models.CharField(max_length=80)

    def __str__(self):
        return self.title + ' ({})'.format(self.year)


class Review(models.Model):
    """ Reviews that are associated with a particular movie """
    review = models.TextField()
    reviewer = models.CharField(max_length=50)
    movie_name = models.ForeignKey(Movie)

    def __str__(self):
        return self.reviewer


class Similar(models.Model):
    """ Similar movies associated to a particular movie """
    movie = models.ForeignKey(Movie)
    real = models.CharField(max_length=80)
    real_u = models.CharField(max_length=150)
    sim1 = models.CharField(max_length=80)
    url1 = models.CharField(max_length=150)
    sim2 = models.CharField(max_length=80)
    url2 = models.CharField(max_length=150)
    sim3 = models.CharField(max_length=80)
    url3 = models.CharField(max_length=150)
    sim4 = models.CharField(max_length=80)
    url4 = models.CharField(max_length=150)
    sim5 = models.CharField(max_length=80)
    url5 = models.CharField(max_length=150)
