from fastapi import FastAPI
from .web import explorer

app = FastAPI()

app.include_router(explorer.router)


@app.get('/')
def top():
    return 'top here'


@app.get('/echo/{thing}')
def echo(thing):
    return f'echoing {thing}'
