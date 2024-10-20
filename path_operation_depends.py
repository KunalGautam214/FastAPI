from fastapi import FastAPI, Depends, Header, HTTPException

from typing import Annotated

app = FastAPI()


def verify_token(x_token: Annotated[str, Header()]):
    if x_token != 'super-fake-token':
        raise HTTPException(status_code=400, detail='x-token invalid')


def verify_key(x_key: Annotated[str, Header()]):
    if x_key != 'super-fake-key':
        raise HTTPException(status_code=400, detail='x-key invalid')
    return x_key


@app.get('/items', dependencies=[Depends(verify_token), Depends(verify_key)])
async def get_items():
    return {'name': 'Carrot', 'description': 'Red and sweet in color'}
