import os
import pytest
from fastapi import HTTPException
from app.model.creature import Creature
from app.web import creature

os.environ['CRYPTID_UNIT_TEST'] = 'true'


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name='Yeti',
        aka='Abominable Snowman',
        country='CN',
        description='Hirsute Himalayan',
        area='Himalayas',
    )


@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()


def assert_duplicate(exception):
    assert exception.value.status_code == 409
    assert 'Duplicate' in exception.value.msg


def assert_missing(exception):
    assert exception.value.status_code == 404
    assert 'Missing' in exception.value.msg


def test_creature(sample):
    assert creature.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as e:
        creature.create(fakes[0])
        assert_duplicate(e)


def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as e:
        creature.get_one('cat')
        assert_missing(e)


def test_modify(fakes):
    assert creature.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as e:
        creature.modify(sample.name, sample)
        assert_missing(e)


def test_delete(fakes):
    assert creature.delete(fakes[0].name) is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as e:
        creature.delete('cat')
        assert_missing(e)
