from app.model.creature import Creature
from app.errors import Missing, Duplicate

fakes = [
    Creature(name='Yeti',
             aka='Abominable Snowman',
             country='CN',
             description='Hirsute Himalayan',
             area='Himalayas'),
    Creature(name='Bigfoot',
             aka='Sasquatch',
             country='US',
             description="Yeti's Cousin Eddie",
             area='*'),
]


def find(name: str) -> Creature | None:
    for fake in fakes:
        if fake.name == name:
            return fake
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f'Missing creature {name}')


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f'Duplicate creature {name}')


def get_all() -> list[Creature]:
    """Return all explorers."""
    return fakes


def get_one(name: str) -> Creature:
    """Return one creature."""
    check_missing(name)
    return find(name)


# Currently all stubs
def create(creature: Creature) -> Creature:
    """Add a new creature."""
    check_duplicate(creature.name)
    return creature


def modify(name: str, creature: Creature) -> Creature:
    """Update some info about the creature."""
    check_missing(name)
    return creature


def delete(name: str) -> None:
    """Delete the creature; return None if the creature existed."""
    check_missing(name)
    return None
