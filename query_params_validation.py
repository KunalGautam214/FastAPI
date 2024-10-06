from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get('/item')
async def item(q: Annotated[int | None, Query()] = None):
    return {'q': q}


@app.get('/item/validation')
async def item_validation(q: Annotated[str | None, Query(min_length=3, max_length=10)] = None):
    return {'q': q}


@app.get('/item/validation/integer')
async def item_validation_integer(q: Annotated[int | None, Query(ge=3, le=10)] = None):
    return {'q': q}


@app.get('/item/validation/default')
async def item_validation_default(q: Annotated[str | None, Query(min_length=3, max_length=10)] = 'Apple'):
    return {'q': q}


@app.get('/item/validation/list')
async def item_validation_list(q: Annotated[list[str] | None, Query()] = ['Apple', 'Banana']):
    return {'q': q}


@app.get('/item/validation/query-params')
async def item_validation_query_param(q: Annotated[str | None, Query(alias='query-param')] = None):
    return {'q': q}


@app.get('/item/validation/docs')
async def item_validation_docs(q: Annotated[str | None, Query(
    title='Query parameter',
    description='Query parameter for search query in database',
    alias='query-param',
    min_length=3,
    max_length=10
)] = None):
    return {'q': q}
