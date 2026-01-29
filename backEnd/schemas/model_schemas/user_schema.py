from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, field_validator, ConfigDict


class UserSchema(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id: int=Field(..., primary_key=True)
    nickname: str=Field(..., uniqe=True, min_length=1, max_length=20, description="Никнейм, от 1 до 20 символов")
    email: EmailStr=Field(..., description="Электронная почта")
    first_name: str=Field(..., min_length=2, max_length=20, description="Имя, от 2 до 20 символов")
    last_name: str=Field(..., min_length=2, max_length=20, description="Фамилия, от 2 до 20 символов")
    city: str=Field(..., min_length=3, max_length=20, description="Название города, от 3 до 20 символов")
    date_of_birth: date=Field(..., description="Дата рождения в формате ГГГГ-ММ-ДД")
    premium: Optional[bool]

    @field_validator("phone_number")
    def validate_phone_number(cls, value):
        if not re.match(r'^\+\d{11}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать 11 цифр')
        return value

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, value):
        if value and value>=datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return value