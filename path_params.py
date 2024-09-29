from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get('/items/{item_id}')
async def get_items(item_id: int):
    return {'item_id': item_id}


class Fruits(str, Enum):
    apple = 'Apple'
    banana = 'Banana'
    pineapple = 'PineApple'


@app.get('/fruits/{fruit_name}')
async def get_fruit(fruit_name: Fruits):
    if fruit_name is Fruits.apple:
        return {'fruit_name': fruit_name, 'message': 'I am an apple'}
    elif fruit_name.value == 'Banana':
        return {'fruit_name': fruit_name, 'message': 'I am yellow in color'}
    return {'fruit_name': fruit_name, 'message': 'I am very sharp from outside'}
