from fastapi import FastAPI, Header
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class CustomHeaders(BaseModel):
    host: str | None = Field('host')
    user_agent: str | None = Field('user-agent')
    x_token: str | None = Field('x-token')


@app.get('/header')
async def get_header(host: Annotated[str, Header()] = None):
    return {'host': host}


@app.get('/header/custom')
async def get_header(header_custom: Annotated[CustomHeaders, Header()] = None):
    return {'header_custom': header_custom}
