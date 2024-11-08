from fastapi import APIRouter

router = APIRouter()


@router.get('/users')
async def get_users():
    return {'name': 'Code with KG'}


@router.get('/users/{user_id}')
async def get_users_by_id(user_id: int):
    return {'user_id': user_id}
