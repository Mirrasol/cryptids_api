from app.model.creature import Creature

# Mock database, to be replaced by real data and SQL
_creatures = [
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


def get_all() -> list[Creature]:
    """Return all explorers."""
    return _creatures


def get_one(name: str) -> Creature | None:
    """Return one creature."""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


# Currently all stubs
def create(creature: Creature) -> Creature:
    """Add a new creature."""
    return creature


def modify(creature: Creature) -> Creature:
    """Update some info about the creature."""
    return creature


def replace(creature: Creature) -> Creature:
    """Full update about the creature."""
    return creature


def delete(name: str) -> bool:
    """Delete the creature; return None if the creature existed."""
    return None
