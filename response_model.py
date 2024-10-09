from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: str
    full_name: str


class UserIn(BaseModel):
    username: str
    email: str
    password: str
    full_name: str


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class LoginUser(UserOut):
    password: str


@app.post('/user')
async def create_user(user: UserIn):
    return user


@app.post('/user/user-in')
async def create_user(user: UserIn) -> UserIn:
    return user


@app.post('/user/response-model', response_model=UserIn)
async def create_user(user: UserIn):
    return user


@app.post('/user/response-model-out', response_model=BaseUser)
async def create_user(user: UserIn):
    return user


@app.post('/user/login-user', response_model=UserOut)
async def create_user(user: LoginUser):
    print(user)
    return user
