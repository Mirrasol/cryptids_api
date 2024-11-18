from app.data.init import curs, IntegrityError
from app.model.creature import Creature
from app.errors import Missing, Duplicate


curs.execute("""create table if not exists creature( \
                name text primary key, \
                country text, \
                area text, \
                description text, \
                aka text)""")


def row_to_model(row: tuple) -> Creature:
    name, country, area, description, aka = row
    return Creature(
        name=name,
        description=description,
        country=country,
        area=area,
        aka=aka,
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.dict()


def get_one(name: str) -> Creature:
    query = """select * from creature where name=:name"""
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'Creature {name} not found')


def get_all() -> list[Creature]:
    query = """select * from creature"""
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature) -> Creature:
    query = """insert into creature (name, country, area, description, aka) \
        values (:name, :country, :area, :description, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(query, params)
        return get_one(creature.name)
    except IntegrityError:
        raise Duplicate(msg=f'Creature {creature.name} already exists')


def modify(name: str, creature: Creature) -> Creature:
    query = """update creature set \
            name=:name,
            country=:country,
            area=:area,
            description=:description,
            aka=:aka
            where name=:name_orig"""
    params = model_to_dict(creature)
    params['name_orig'] = name
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(msg=f'Creature {name} not found')


def delete(name: str):
    query = """delete from creature where name = :name"""
    params = {'name': name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f'Creature {name} not found')
