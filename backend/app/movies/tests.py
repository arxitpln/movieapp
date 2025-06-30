from django.test import TestCase
from movies.models import Movie
from .models import Review

class ReviewTestCase(TestCase):
    def test_review_creation(self):
        movie = Movie.objects.create(title="Test", description="Test desc")
        review = Review.objects.create(grade=4, movie=movie)
        self.assertEqual(review.grade, 4)
        self.assertEqual(review.movie, movie)
