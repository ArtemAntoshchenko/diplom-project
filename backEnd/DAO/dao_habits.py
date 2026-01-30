from .dao_base import BaseDAO
from ..db.models import Habit
from ..db.database import get_db
from sqlalchemy import select
 
class HabitDAO(BaseDAO):
    model=Habit

    @classmethod
    async def find_all_active(cls):
        async with get_db() as session:
            query=select(cls.model).where(cls.model.active==True)
            result=await session.scalars(query)
            result_list=result.all()
            return result_list 