from init import curs, IntegrityError
from app.model.explorer import Explorer
from app.errors import Missing, Duplicate


curs.execute("""create table if not exists explorer( \
                name text primary key, \
                country text, \
                description text)""")


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(
        name=name,
        country=country,
        description=description,
    )


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict()


def get_one(name: str) -> Explorer:
    query = """select * from explorer where name=:name"""
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'Explorer {name} not found')


def get_all() -> list[Explorer]:
    query = """select * from explorer"""
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    if not explorer:
        return None
    query = """insert into explorer (name, country, description) \
        values (:name, :country, :description)"""
    params = model_to_dict(explorer)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(msg=f'Explorer {explorer.name} already exists')
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    if not (name and explorer):
        return None
    query = """update explorer
            set name=:name,
            country=:country,
            description=:description
            where name=:name_orig"""
    params = model_to_dict(explorer)
    params['name_orig'] = name
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(msg=f'Explorer {name} not found')


def delete(name: str):
    if not name:
        return False
    query = """delete from explorer where name = :name"""
    params = {'name': name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f'Explorer {name} not found')
