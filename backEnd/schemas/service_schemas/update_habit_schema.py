from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class HabitUpdateSchema(BaseModel):
    id: int
    name: str=Field(..., description="Имя привычки")
    description: str=Field(..., max_length=300, description="Описание привычки")
    goal: Optional[int]=Field(None, description="Цель для привычки")

class HabitUpdateResponse(BaseModel):
    id: int
    name: str=Field(..., description="Имя привычки")
    description: str=Field(..., max_length=300, description="Описание привычки")
    goal: Optional[int]=Field(None, description="Цель для привычки")