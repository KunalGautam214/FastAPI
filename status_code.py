from fastapi import FastAPI, status

app = FastAPI()


@app.post('/user', status_code=201)
async def create_user(username: str, password: str):
    return {'username': username}


@app.post('/user/created', status_code=status.HTTP_201_CREATED)
async def create_user(username: str, password: str):
    return {'username': username}
