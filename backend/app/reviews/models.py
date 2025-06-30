from django.db import models
from app.movies.models import Movie

class Review(models.Model):
    grade = models.IntegerField()
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
