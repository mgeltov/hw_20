from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    john = Director(id=1, name='John')
    bob = Director(id=2, name='Bob')
    bill = Director(id=3, name='Bill')

    director_dao.get_one = MagicMock(return_value=john)
    director_dao.get_all = MagicMock(return_value=[john, bob, bill])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock(return_value=Director(id=2))

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None

    def test_create(self):
        director = self.director_service.create(4)

        assert director is not None

    def test_update(self):
        director = self.director_service.update(3)

        assert director is not None