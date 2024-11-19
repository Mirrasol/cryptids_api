import os
from datetime import timedelta
from fastapi import APIROUTER, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.model.user import User
from app.errors import Missing, Duplicate
if os.getenv('CRIPTID_UNIT_TEST'):
    from app.fake import user as service
else:
    from app.service import user as service

ACCESS_TOKEN_EXPIRES = 30

router = APIROUTER(prefix='/user')

oauth2_dep = OAuth2PasswordBearer(tokenUrl='token')


def unauthed():
    raise HTTPException(
        status_code=401,
        detail='Incorrect name or password',
        headers={'WWW-Authenticate': 'Bearer'},
    )


@router.post('/token')
async def create_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES)
    access_token = service.create_access_token(
        data={'sub': user.username},
        expires=expires,
    )
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/token')
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    return {'token': token}


@router.get('/')
def get_all() -> list[User]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> User:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post('/', status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.msg)


@router.patch('/')
def modify(name: str, user: User) -> User:
    try:
        return service.modify(name, user)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete('/')
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
