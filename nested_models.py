from fastapi import FastAPI, Body
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()


class Image(BaseModel):
    name: str
    url: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # image: Image | None = None
    image: list[Image] | None = None


@app.put('/item')
async def update_item(item: Annotated[Item, Body(embed=True)]):
    return item
