from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class HabitCreateSchema(BaseModel):
    id: int
    name: str=Field(..., description="Имя привычки")
    description: str=Field(..., max_length=300, description="Описание привычки")
    goal: int=Field(..., description="Цель для привычки")
    step: int=Field(..., description="Шаг выполнения привычки")