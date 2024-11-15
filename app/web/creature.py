from fastapi import APIRouter
from app.model.creature import Creature
import app.fake.creature as service

router = APIRouter(prefix='/creature')


@router.get('/')
def get_all() -> list[Creature]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Creature | None:
    return service.get_one(name)


# All the rest - currently stubs
@router.post('/')
def create(creature: Creature) -> Creature:
    return service.create(creature)


@router.patch('/')
def modify(creature: Creature) -> Creature:
    return service.modify(creature)


@router.put('/')
def replace(creature: Creature) -> Creature:
    return service.replace(creature)


@router.delete('/{name}')
def delete(name: str):
    return service.delete(name)
