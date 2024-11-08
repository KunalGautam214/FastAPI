from fastapi import Header, HTTPException
from typing import Annotated


async def get_header_token(x_token: Annotated[str, Header()]):
    if x_token != 'super-fake-token':
        raise HTTPException(status_code=400, detail='X-token is invalid')
