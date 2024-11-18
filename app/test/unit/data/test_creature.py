from app.model.creature import Creature
from app.errors import Missing, Duplicate
from app.data import creature
import os
import pytest

os.environ['CRYPTID_SQLITE_DB'] = ':memory:'


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name='yeti',
        country='CN',
        area='Himalayas',
        description='Hirsute Himalayan',
        aka='Abominable Snowman',
    )


def test_create(sample):
    response = creature.create(sample)
    assert response == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)


def test_get_one(sample):
    response = creature.get_one(sample.name)
    assert response == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = creature.get_one('boxturtle')


def test_modify(sample):
    creature.area = 'Sesame Street'
    response = creature.modify(sample.name, sample)
    assert response == sample


def test_modify_missing():
    thing: Creature = Creature(
        name='snurfle',
        country='RU',
        area='',
        description='some thing',
        aka='',
    )
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)


def test_delete(sample):
    response = creature.delete(sample.name)
    assert response is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)
