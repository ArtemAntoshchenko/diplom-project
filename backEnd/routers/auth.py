from fastapi import APIRouter, HTTPException, status
from core.auth import get_password_hash
from DAO.dao_registation import UserDAO
from schemas.service_schemas.reg_schema import UserRegisterSchema

router=APIRouter(prefix='/auth', tags=['Авторизация'])

@router.post('/login')
async def login():
    pass

@router.post('/registration')
async def register_user(user_data: UserRegisterSchema) -> dict:
    user = await UserDAO.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.model_dump()
    user_dict['password'] = get_password_hash(user_data.password)
    await UserDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}