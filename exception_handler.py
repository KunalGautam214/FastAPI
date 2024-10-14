from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name


items = {
    'carrot': 'Red and healthy for life'
}


@app.get('/item')
async def get_items(item: str):
    if item not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    return items[item]


@app.exception_handler(CustomException)
async def exception_handler(request: Request, exec: CustomException):
    return JSONResponse(status_code=404,
                        content={'message': exec.name})


@app.get('/item/custom-exception')
async def get_items(item: str):
    if item not in items:
        raise CustomException('Item not found in list')
    return items[item]
