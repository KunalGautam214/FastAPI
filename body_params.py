from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post('/items')
async def create_item(item: Item):
    return item


fake_db_list = []


@app.post('/items/{item_id}')
async def create_item(item: Item, item_id: int):
    item_dict = item.dict()
    if item.price:
        tax_price = item.price * item.tax
        item_dict.update({'price_with_tax': tax_price})
    fake_db_list.append(item_dict)
    return {'item_id': item_id, 'items': item_dict}


@app.get('/items/{item_name}')
async def get_item(item_name: str):
    item_dict = {}
    for item in fake_db_list:
        if item.get('name') == item_name:
            item_dict.update({'message': 'Item found in db',
                              'item': item_name})
            return {'item': item_dict}
    return {'message': 'Item not found in db'}
