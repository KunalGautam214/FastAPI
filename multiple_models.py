from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class UserOut(BaseUser):
    pass


class UserIn(BaseUser):
    password: str


class UserInDB(BaseUser):
    hashed_password: str


def fake_hashed_password(password):
    return 'supersecretpassword' + password


def fake_user_create(user: UserIn):
    hashed_password = fake_hashed_password(user.password)
    user_created = UserInDB(**user.model_dump(),
                            hashed_password=hashed_password)
    print(user_created)
    return user_created


@app.post('/user', response_model=UserOut)
async def create_user(user: UserIn):
    user = fake_user_create(user)
    return user
