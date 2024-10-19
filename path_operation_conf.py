from fastapi import FastAPI, status
from pydantic import BaseModel

from enum import Enum

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


class Tags(Enum):
    user = 'user'
    item = 'item'


@app.post('/item', response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item


@app.post('/item/create-item', tags=['items'])
async def create_item(item: Item):
    return item


@app.get('/item/read-item', tags=['items'])
async def read_item(item: Item):
    return item


@app.get('/user/read-user/{user_id}', tags=['users'])
async def read_user(user_id: str):
    return user_id


@app.post('/user/create-user', tags=['users'])
async def create_user(username: str, password: str):
    return {'username': username}


@app.post('/item/create-item/enum', tags=[Tags.item])
async def create_item(item: Item):
    return item


@app.get('/item/read-item/enum', tags=[Tags.item])
async def read_item(item: Item):
    return item


@app.get('/user/read-user/{user_id}/enum', tags=[Tags.user])
async def read_user(user_id: str):
    return user_id


@app.post('/user/create-user/enum', tags=[Tags.user])
async def create_user(username: str, password: str):
    return {'username': username}


@app.post('/item/summary', response_model=Item, summary='Create an item',
          description='Create an item with all information')
async def create_item(item: Item):
    return item


@app.post('/item/summary-desc', response_model=Item, summary='Create an item')
async def create_item(item: Item):
    '''
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if item does not have a tax, you can omit it
    - **tags**: a set of unique tag string for this item
    '''
    return item


@app.post('/item/summary/response-description', response_model=Item, summary='Create an Item',
          response_description='The created item')
async def create_item(item: Item):
    '''
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if item does not have a tax, you can omit it
    - **tags**: a set of unique tag string for this item
    '''
    return item


@app.post('/item/deprecated', response_model=Item, deprecated=True)
async def create_item(item: Item):
    '''
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if item does not have a tax, you can omit it
    - **tags**: a set of unique tag string for this item
    '''
    return item
