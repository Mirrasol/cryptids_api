import os
from fastapi import APIRouter, HTTPException
from app.model.explorer import Explorer
from app.errors import Duplicate, Missing
if os.getenv('CRYPTID_UNIT_TEST'):
    from app.fake import explorer as service
else:
    from app.service import explorer as service

router = APIRouter(prefix='/explorer')


@router.get('')
@router.get('/')
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


# All the rest - currently stubs
@router.post('', status_code=201)
@router.post('/', status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.msg)


@router.patch('/')
def modify(name: str, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete('/{name}', status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
