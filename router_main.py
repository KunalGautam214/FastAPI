from fastapi import FastAPI

from api_router import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)


@app.get('/root')
async def root():
    return 'I am root'
