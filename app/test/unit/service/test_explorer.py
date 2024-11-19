import os
import pytest
from fastapi import HTTPException
from app.model.explorer import Explorer
from app.web import explorer

os.environ['CRYPTID_UNIT_TEST'] = 'true'


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name='Ann Jane',
        description='Explorer Extraordinary',
        country='UK',
    )


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


def assert_duplicate(exception):
    assert exception.value.status_code == 409
    assert 'Duplicate' in exception.value.msg


def assert_missing(exception):
    assert exception.value.status_code == 404
    assert 'Missing' in exception.value.msg


def test_explorer(sample):
    assert explorer.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as e:
        explorer.create(fakes[0])
        assert_duplicate(e)


def test_get_one(fakes):
    assert explorer.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as e:
        explorer.get_one('Sue Joe')
        assert_missing(e)


def test_modify(fakes):
    assert explorer.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as e:
        explorer.modify(sample.name, sample)
        assert_missing(e)


def test_delete(fakes):
    assert explorer.delete(fakes[0].name) is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as e:
        explorer.delete('Sue Joe')
        assert_missing(e)
