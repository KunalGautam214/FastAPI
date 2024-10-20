from fastapi import FastAPI, Depends, Header, HTTPException

from typing import Annotated


def verify_token(x_token: Annotated[str, Header()]):
    if x_token != 'super-fake-token':
        raise HTTPException(status_code=400, detail='x-token header invalid')


def verify_key(x_key: Annotated[str, Header()]):
    if x_key != 'super-fake-key':
        raise HTTPException(status_code=400, detail='x-key header invalid')
    return x_key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get('/items')
async def get_items():
    return {'name': 'Apple', 'description': 'Doctor recommended fruits'}


@app.get('/users')
async def get_users():
    return {'name': 'Code with KG', 'description': 'YouTube tutorial channel'}
