from fastapi import APIRouter, Depends

from .dependencies import get_header_token

router = APIRouter(
    prefix='/items',
    tags=['items'],
    dependencies=[Depends(get_header_token)]
)


@router.get('/')
async def get_items():
    return {'name': 'Apple'}


@router.get('/{item_id}', status_code=200)
async def get_item_by_id(item_id: int):
    return {'item_id': item_id}
