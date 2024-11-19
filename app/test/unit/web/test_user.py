import os
import pytest
from fastapi import HTTPException
from app.model.user import User
from app.web import user

os.environ['CRYPTID_UNIT_TEST'] = 'true'


@pytest.fixture
def sample() -> User:
    return User(
        name='Wyll Ravengard',
        hash='123987',
    )


@pytest.fixture
def fakes() -> list[User]:
    return user.get_all()


def assert_duplicate(exception):
    assert exception.value.status_code == 409
    assert 'Duplicate' in exception.value.msg


def assert_missing(exception):
    assert exception.value.status_code == 404
    assert 'Missing' in exception.value.msg


def test_user(sample):
    assert user.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as e:
        user.create(fakes[0])
        assert_duplicate(e)


def test_get_one(fakes):
    assert user.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as e:
        user.get_one('Shadowheart')
        assert_missing(e)


def test_modify(fakes):
    assert user.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as e:
        user.modify(sample.name, sample)
        assert_missing(e)


def test_delete(fakes):
    assert user.delete(fakes[0].name) is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as e:
        user.delete('Shadowheart')
        assert_missing(e)
