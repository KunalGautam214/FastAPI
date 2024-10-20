from fastapi import FastAPI, Depends

from typing import Annotated

app = FastAPI()


async def common_params(q: str, page: int, size: int):
    return {'q': q, 'page': page, 'size': size}


common_param = Annotated[dict, Depends(common_params)]


@app.get('/item')
async def get_items(common_params: common_param):
    return common_params


@app.get('/user')
async def get_users(q: str, page: int, size: int):
    return {'q': q, 'page': page, 'size': size}


class CommonParams:
    def __init__(self, q: str, page: int, size: int):
        self.q = q
        self.page = page
        self.size = size


@app.get('/user/class-depends')
async def get_users(common_params: Annotated[CommonParams, Depends()]):
    return common_params
