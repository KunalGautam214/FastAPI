from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_db_list = [x for x in range(21)]

@app.get('/items/{item_id}')
async def items(item_id, page: int, size: int):
    items = fake_db_list[page:size]
    items_dict = {'items': items}
    if page:
        items_dict.update({'page': page})
    if size:
        items_dict.update({'size': size})
    return items_dict


@app.get('/items-optional/{item_id}')
async def items_optional(item_id, page: Optional[int] = 0,
                         size: Optional[int] = 10):
    items = fake_db_list[page:size]
    items_dict = {'items': items}
    if page:
        items_dict.update({'page': page})
    if size:
        items_dict.update({'size': size})
    return items_dict

@app.get('/items-optional_2/{item_id}')
async def items_optional(item_id, page: int | None = 0,
                         size: int | None = 10):
    items = fake_db_list[page:page+size]
    items_dict = {'items': items}
    if page:
        items_dict.update({'page': page})
    if size:
        items_dict.update({'size': size})
    return items_dict


@app.get('/items-bool/{item_id}')
async def items_optional(item_id, page: int | None = 0,
                         size: int | None = 10,
                         short: bool | None = False):
    items = fake_db_list[page:page+size]
    items_dict = {'items': items}
    if item_id:
        items_dict.update({'item_id': item_id})
    if page:
        items_dict.update({'page': page})
    if size:
        items_dict.update({'size': size})
    if short:
        items_dict.update({'short': short})
    return items_dict
