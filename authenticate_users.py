from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
import secrets
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError

app = FastAPI()

SECRET_KEY = 'cbb9624c95e66536333a0e14d4645f0db928f0df4f191498796f619899613e43'  # length = 32
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_SECONDS = 30

FAKE_DB_USERS = {
    'codewithkg': {
        'username': 'codewithkg',
        'email': 'codewithkg@example.com',
        'full_name': 'Code with Kg',
        'hashed_password': '$2b$12$7QAx46kMf8N8QrmHZK5g5u.yR3GJtpnDCceZMqdfp7SDgBznLIck2',  # supersecret
        'disabled': False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)


def get_hashed_password(password):
    return pwd_context.hash(password)


def get_secret_key(length=32):
    return secrets.token_hex(length)


def get_user(db, username: str):
    if username in db:
        user = db[username]
        return UserInDB(**user)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if user is None:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(seconds=30)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Could not validate credential',
                                headers={'WWW-Authenticate': 'Bearer'})
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Invalid token',
                            headers={'WWW-Authenticate': 'Bearer'})
    user = get_user(FAKE_DB_USERS, username=token_data.username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Could not validate credential',
                            headers={'WWW-Authenticate': 'Bearer'})
    return user


def get_current_active_user(current_user: Annotated[User,
Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Inactive user')
    return current_user


@app.post('/token')
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm,
Depends()]):
    user = authenticate_user(FAKE_DB_USERS,
                             form_data.username,
                             form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or password',
                            headers={'WWW-Authenticate': 'Bearer'})

    access_token_expire = timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    access_token = create_access_token(data={'sub': user.username},
                                       expires_delta=access_token_expire)
    return Token(access_token=access_token, token_type='bearer')


@app.get('/user/me', response_model=User)
async def get_users(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


@app.get('/items')
async def get_items(current_user: Annotated[User, Depends(get_current_active_user)]):
    return {'name': 'Carrot', 'description': 'sweet and red in color'}
