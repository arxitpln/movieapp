from django.db import models
from app.actors.models import Actor

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")

    def average_grade(self):
        return self.reviews.aggregate(models.Avg("grade"))["grade__avg"] or 0
