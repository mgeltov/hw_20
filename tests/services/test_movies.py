from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    john = Movie(id=1, title='John', description='description',
                 trailer='http//q', year=2020, rating=5.1, genre_id=1, director_id=1)
    bob = Movie(id=2, title='Bob', description='description',
                trailer='http//q', year=2020, rating=5.1, genre_id=1, director_id=1)
    bill = Movie(id=3, title='Bill', description='description',
                 trailer='http//q', year=2020, rating=5.1, genre_id=1, director_id=1)

    movie_dao.get_one = MagicMock(return_value=john)
    movie_dao.get_all = MagicMock(return_value=[john, bob, bill])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock(return_value=Movie(id=2))

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) == 3

    def test_create(self):
        movie = self.movie_service.create(4)

        assert movie is not None

    def test_update(self):
        movie = self.movie_service.update(3)

        assert movie is not None
