from fastapi import FastAPI

app = FastAPI()


@app.get('/welcome')
async def welcome():
    return 'Welcome to FastAPI world'
