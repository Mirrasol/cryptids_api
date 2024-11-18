import os
from fastapi import APIROUTER, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.model.user import User
if os.getenv('CRUPTID_UNIT_TEST'):
    from app.fake import user as service
else:
    from app.service import user as service

ACCESS_TOKEN_EXPIRES = 30

router = APIROUTER(prefix = '/user')

oauth2_dep = OAuth2PasswordBearer(tokenUrl='token')


def unauthed():
    raise HTTPException(
        status_code=401,
        detail='Incorrect name or password',
        headers={'WWW-Authenticate': 'Bearer'},
    )
