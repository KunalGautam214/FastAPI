from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        'json_schema_extra': {
            'examples': [
                {
                    'name': 'Carrot',
                    'description': 'A red and sweet',
                    'price': 10.50,
                    'tax': 1.50,
                }
            ]
        }
    }


class Item_3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class Item_2(BaseModel):
    name: str = Field(examples=['Banana'])
    description: str | None = Field(None, examples=['A healthy fruit'])
    price: float = Field(examples=[20.10])
    tax: float | None = Field(None, examples=[2.50])


@app.get('/item')
async def get_items(item: Item):
    return item


@app.put('/items/model-schema-2')
async def update_item(item: Item_2):
    return item


@app.put('/items/model-schema-3')
async def update_item(item: Annotated[Item_3, Body(
    examples=[
        {
            'name': 'Apple',
            'description': 'Doctor recommended fruit',
            'price': 50.50,
            'tax': 3.10
        }
    ]
)]):
    return item


@app.put('/items/model-schema-4')
async def update_item(item: Annotated[Item_3, Body(
    openapi_examples={
        'normal': {
            'summary': 'A normal example',
            'description': 'A normal example works correctly',
            'value': {
                'name': 'Carrot',
                'description': 'A red and sweet',
                'price': 10.50,
                'tax': 1.50,
            }
        },
        'converted': {
            'summary': 'A converted example',
            'description': 'FastAPI can convert price string to actual value',
            'value': {
                'name': 'Carrot',
                'price': '10.50'
            }
        },
        'invalid': {
            'summary': 'Invalid example',
            'description': 'Invalid data is rejected with an error',
            'value': {
                'name': 'Carrot',
                'price': 'ten point five zero'
            }
        }
    }
)]):
    return item
