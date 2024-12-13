from sqlalchemy import insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.categorys.models import Category

from app.database import async_session_maker
from sqlalchemy import update, delete, event


class CategoryDAO(BaseDAO):
    model = Category
    table_name = "categorys"

    # @classmethod
    # async def find_full_data(cls, category_id: int):
    #     async with async_session_maker() as session:

    #         query = select(cls.model).filter_by(id=category_id)
    #         result = await session.execute(query)
    #         category_info = result.scalar_one_or_none()


    #         if not category_info:
    #             return None

    #         category_data = category_info.to_dict()
    #         return category_data
        

    # @classmethod
    # async def add_category(cls, **category_data: dict):
    #     async with async_session_maker() as session:
    #         async with session.begin():
    #             new_category = Category(**category_data)
    #             session.add(new_category)
    #             await session.flush()
    #             new_category_id = new_category.id
    #             await session.commit()
    #             return new_category_id
            
            
    # @classmethod
    # async def delete_category_by_id(cls, category_id: int):
    #     async with async_session_maker() as session:
    #         async with session.begin():
    #             query = select(cls.model).filter_by(id=category_id)
    #             result = await session.execute(query)
    #             category_to_delete = result.scalar_one_or_none()

    #             if not category_to_delete:
    #                 return None

    #             await session.execute(
    #                 delete(cls.model).filter_by(id=category_id)
    #             )

    #             await session.commit()
    #             return category_id