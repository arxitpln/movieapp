import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from app.movies.models import Movie
from app.reviews.models import Review
from app.actors.models import Actor

Movie.objects.all().delete()
Actor.objects.all().delete()
Review.objects.all().delete()

actors = []
for i in range(15):
    actor = Actor.objects.create(first_name=f"Prénom{i}", last_name=f"Nom{i}")
    actors.append(actor)

for i in range(10):
    movie = Movie.objects.create(
        title=f"Film {i+1}",
        description=f"Description du film {i+1}"
    )
    movie.actors.add(*random.sample(actors, k=random.randint(1, 3)))

    for _ in range(5):
        Review.objects.create(
            grade=random.randint(1, 5),
            movie=movie
        )

print("Dummy datas added")
