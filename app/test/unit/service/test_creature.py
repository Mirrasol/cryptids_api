from app.model.creature import Creature
from app.service import creature

test_subject = Creature(
    name='Yeti',
    aka='Abominable Snowman',
    country='CN',
    description='Hirsute Himalayan',
    area='Himalayas',
)


def test_create():
    result = creature.create(test_subject)
    assert result == test_subject


def test_get_exists():
    result = creature.get_one('Yeti')
    assert result == test_subject


def test_get_missing():
    result = creature.get_one('Boxturtle')
    assert result is None
