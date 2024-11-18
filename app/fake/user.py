from app.model.user import User
from app.errors import Missing, Duplicate

fakes = [
    User(name='kwij', hash='abc'),
    User(name='erm', hash='defg'),
]


def find(name: str) -> User | None:
    for fake in fakes:
        if fake.name == name:
            return fake
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f'Missing user {name}')


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f'Duplicate user {name}')


def get_all() -> list[User]:
    return fakes


def get_one(name: str) -> User:
    check_missing(name)
    return find(name)


def create(user: User) -> User:
    check_duplicate(user.name)
    return user


def modify(name: str, user: User) -> User:
    check_missing(name)
    return user


def delete(name: str) -> None:
    check_missing(name)
    return None
