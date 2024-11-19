import os
from app.model.creature import Creature
if os.getenv('CRYPTID_UNIT_TEST'):
    from app.fake import creature as data
else:
    from app.data import creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Creature:
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def modify(name: str, creature: Creature) -> Creature:
    return data.modify(name, creature)


def delete(name: str) -> None:
    return data.delete(name)
