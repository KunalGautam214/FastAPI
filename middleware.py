from fastapi import FastAPI, Request
import time

app = FastAPI()


@app.middleware('http')
async def middleware(request: Request, call_next):
    start = time.time()
    print('Before route call')
    response = await call_next(request)
    print('After route call')
    end = time.time() - start
    response.headers['X-process-time'] = str(end)
    return response


@app.get('/items')
async def get_items():
    print('Route called')
    return {'name': 'Apple', 'description': 'Doctor recommended fruit'}
