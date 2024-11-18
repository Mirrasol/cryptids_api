from init import curs
from app.model.creature import Creature


curs.execute("""create table if not exists creature(
                name text primary key,
                description text,
                country text,
                area text,
                aka text""")


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)


def model_to_dict(creature: Creature) -> dict:
    return creature.dict()


def get_one(name: str) -> Creature:
    query = 'select * from creature where name=%(name)s'
    params = {'name': name}
    curs.execute(query, params)
    return row_to_model(curs.fetchone())


def get_all(name: str) -> list[Creature]:
    query = 'select * from creature'
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature):
    query = 'insert into creature (name, description, country, area, aka) \
        values (%(name)s, %(description)s, %(country)s, %(area)s, %(aka)s)'
    params = model_to_dict(creature)
    curs.execute(query, params)
    return get_one(creature.name)


def modify(creature: Creature) -> Creature:
    query = """update creature
                set country=%(country)s,
                    name=%(name)s,
                    description=%(description)s,
                    area=%(area)s,
                    aka=%(aka)s
                where name=%(name_orig)s"""
    params = model_to_dict(creature)
    params['name_orig'] = creature.name
    _ = curs.execute(query, params)
    return get_one(creature.name)


def delete(creature: Creature) -> bool:
    query = 'delete from creature where name = %(name)s'
    params = {'name': creature.name}
    result = curs.execute(query, params)
    return bool(result)
