from fastapi import FastAPI, Depends

from typing import Annotated

app = FastAPI()


def query(q: str):
    return {'q': q}


def common_params(page: int, size: int, q: Annotated[str, Depends(query)]):
    return {'q': q, 'page': page, 'size': size}


@app.get('/items')
async def get_items(common_params: Annotated[common_params, Depends()]):
    return common_params
