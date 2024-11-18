from app.model.explorer import Explorer
from app.errors import Missing, Duplicate

fakes = [
    Explorer(name='Claude Hande',
             country='FR',
             description='Scarce during full moons'),
    Explorer(name='Noah Weiser',
             country='DE',
             description='Myopic machete man'),
]


def find(name: str) -> Explorer | None:
    for fake in fakes:
        if fake.name == name:
            return fake
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f'Missing explorer {name}')


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f'Duplicate explorer {name}')


def get_all() -> list[Explorer]:
    """Return all explorers."""
    return fakes


def get_one(name: str) -> Explorer:
    """Return one explorer."""
    check_missing(name)
    return find(name)


# Currently all stubs
def create(explorer: Explorer) -> Explorer:
    """Add a new explorer."""
    check_duplicate(explorer.name)
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    """Update some info about the explorer."""
    check_missing(name)
    return explorer


def delete(name: str) -> None:
    """Delete the explorer; return None if the explorer existed."""
    check_missing(name)
    return None
