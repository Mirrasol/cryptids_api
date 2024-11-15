from app.model.explorer import Explorer

# Mock database, to be replaced by real data and SQL
_explorers = [
    Explorer(name='Claude Hande',
             country='FR',
             description='Scarce during full moons'),
    Explorer(name='Noah Weiser',
             country='DE',
             description='Myopic machete man'),
]


def get_all() -> list[Explorer]:
    """Return all explorers."""
    return _explorers


def get_one(name: str) -> Explorer | None:
    """Return one explorer."""
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

# Currently all stubs
def create(explorer: Explorer) -> Explorer:
    """Add a new explorer."""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Update some info about the explorer."""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Full update about the explorer."""
    return explorer


def delete(name: str) -> bool:
    """Delete the explorer; return None if the explorer existed."""
    return None
