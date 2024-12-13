from sqlalchemy import insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import text

from app.dao.base import BaseDAO
from app.filmcategorys.models import FilmCategory
from app.database import async_session_maker
from sqlalchemy import update, delete, event


class FilmCategoryDAO(BaseDAO):
    model = FilmCategory
    table_name = "filmcategorys"

    @classmethod
    async def find_one_or_none_by_two_ids(cls, film_id: int, category_id: int):
        query = text(f"SELECT * FROM {cls.table_name} WHERE film_id = :film_id AND category_id = :category_id")
        params = {"film_id": film_id, "category_id": category_id}
        async with async_session_maker() as session:
            result = await session.execute(query, params)
            return result.fetchone()