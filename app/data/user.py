from app.data.init import curs, IntegrityError
from app.model.user import User
from app.errors import Missing, Duplicate


curs.execute("""create table if not exists user( \
                name text primary key, \
                hash text)""")

curs.execute("""create table if not exists xuser( \
                name text primary key, \
                hash text)""")


def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(
        name=name,
        hash=hash,
    )


def model_to_dict(user: User) -> dict:
    return user.dict()


def get_one(name: str) -> User:
    query = """select * from user where name = :name"""
    params = {'name': name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'User {name} not found')


def get_all() -> list[User]:
    query = """select * from user"""
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(user: User, table: str = 'user') -> User:
    if table not in ('user', 'xuser'):
        raise Exception('Invalid table name')
    query = f"""insert into {table} (name, hash) \
        values (:name, :hash)"""
    params = model_to_dict(user)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(msg=f'User {user.name} already exists')
    return user


def modify(name: str, user: User) -> User:
    query = """update user
            set name=:name,
            hash=:hash,
            where name = :name_orig"""
    params = model_to_dict(user)
    params['name_orig'] = name
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(user.name)
    else:
        raise Missing(msg=f'User {name} not found')


def delete(name: str):
    user = get_one(name)
    query = """delete from user where name = :name"""
    params = {'name': name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f'User {name} not found')
    create(user, table='xuser')
