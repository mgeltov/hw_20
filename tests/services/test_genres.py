from unittest.mock import MagicMock
import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    drama = Genre(id=1, name='drama')
    comedy = Genre(id=2, name='comedy')
    cartoon = Genre(id=3, name='cartoon')

    genre_dao.get_one = MagicMock(return_value=drama)
    genre_dao.get_all = MagicMock(return_value=[drama, comedy, cartoon])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock(return_value=Genre(id=2))

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert genres is not None
        assert len(genres) == 3

    def test_create(self):
        genre = self.genre_service.create(4)

        assert genre is not None

    def test_update(self):
        genre = self.genre_service.update(3)

        assert genre is not None