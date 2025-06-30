from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg
from .models import Movie
from .serializers import MovieSerializer

class MoviePagination(PageNumberPagination):
    page_size_query_param = 'count'
    # max_page_size = 100

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    queryset = Movie.objects.all()

    def get_queryset(self):
        return Movie.objects.all().prefetch_related('actors', 'reviews') \
            .annotate(average_grade=Avg('reviews__grade'))
