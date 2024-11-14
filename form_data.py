from fastapi import FastAPI, Form
from pydantic import BaseModel

from typing import Annotated

app = FastAPI()


class UserDataForm(BaseModel):
    username: str
    password: str


@app.post('/user')
async def create_user(username: Annotated[str, Form()]):
    return {'username': username}


@app.post('/user/form-data')
async def create_user(user_data: Annotated[UserDataForm, Form()]):
    return {'username': user_data}
