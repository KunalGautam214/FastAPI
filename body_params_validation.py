from fastapi import FastAPI, Body, Query
from pydantic import BaseModel, Field

from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str = Field(min_length=3, max_length=10)
    description: str | None = Field(None)
    price: float = Field(100)
    tax: float | None = Field(None)


@app.post('/items')
async def create_item(item: Annotated[Item, Body()]):
    return item


@app.get('/items/query-params')
async def read_item(filter_items: Annotated[Item, Query()]):
    return filter_items


@app.get('/items/{path_items}')
async def read_item(path_items: str):
    return path_items


@app.post('/items/{path_items}/mix')
async def read_item(path_items: str, item: Item, q: str):
    return {'path_items': path_items, 'body': item, 'q': q}
