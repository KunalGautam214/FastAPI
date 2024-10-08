from fastapi import FastAPI, Response, Cookie
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class CustomCookie(BaseModel):
    my_cookie: str | None = Field('my_cookie')
    ads_id: str | None = Field('ads_id')
    custom_cookie: str | None = Field('custom_cookie')


@app.get('/set-cookie')
async def set_cookie(response: Response):
    response.set_cookie(key='my_cookie', value='my value')
    response.set_cookie(key='ads_id', value='my ads id')
    response.set_cookie(key='custom_cookie', value='some random cookie')
    return {'message': 'Cookie set successfully'}


@app.get('/get-cookie')
async def get_cookie(my_cookie: Annotated[str, Cookie()] = None):
    return {'cookie': my_cookie}


@app.get('/get-cookie/multiple')
async def multiple_cookie(cookies: Annotated[CustomCookie, Cookie()]):
    return {'cookies': cookies}
