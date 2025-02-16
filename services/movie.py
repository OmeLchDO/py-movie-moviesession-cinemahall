from django.db.models.query import QuerySet
from db.models import Movie
from typing import List


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids:
        queryset = queryset.filter(genres__id__in=genres_ids)
    if actors_ids:
        queryset = queryset.filter(actors__id__in=actors_ids)

    return queryset


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: List[int] = None,
                 actors_ids: List[int] = None
                 ) -> None:
    film = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genres_ids:
        film.genres.set(genres_ids)
    if actors_ids:
        film.actors.set(actors_ids)
