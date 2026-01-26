from .dao_base import BaseDAO
from db.models import Habit

 
class HabitDAO(BaseDAO[Habit]):
    def __init__(self):
        super().__init__(Habit)