from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/items/{item_id}')
async def items(item_id: Annotated[int | None, None] = None):
    return {'item_id': item_id}


@app.get('/items/validation/{item_id}')
async def items(item_id: Annotated[int | None, Path(gt=5, lt=15)]):
    return {'item_id': item_id}


@app.get('/items/docs/{item_id}')
async def items(item_id: Annotated[int | None, Path(
    title='Path parameter',
    description='Path parameter to fetch record from database',
    gt=5,
    lt=15
)]):
    return {'item_id': item_id}
