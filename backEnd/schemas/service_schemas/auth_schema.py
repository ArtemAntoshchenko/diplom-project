from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class UserRegister_schema(BaseModel):
    email: EmailStr=Field(..., description="Электронная почта")
    password: str=Field(..., min_length=6, max_length=30, description="Пароль, от 6 до 20 знаков")
    phone_number: str=Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str=Field(..., min_length=2, max_length=30, description="Имя, от 2 до 20 символов")
    last_name: str=Field(..., min_length=2, max_length=30, description="Фамилия, от 2 до 20 символов")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, value: str) -> str:
        if not re.match(r'^\+\d{5,15}$', value):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 5 до 15 цифр')
        return value