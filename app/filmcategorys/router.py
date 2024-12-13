from fastapi import APIRouter, Depends, HTTPException, status

from app.filmcategorys.dao import FilmCategoryDAO
from app.filmcategorys.rb import RBFilmCategory
from app.filmcategorys.schemas import SFilmCategory, SFilmCategoryAdd


router = APIRouter(prefix='/filmcategorys', tags=['Работа с связью категорий и фильмом'])


@router.get("/", summary="Получить все связи")
async def get_all_film_categorys(request_body: RBFilmCategory = Depends()) -> list[SFilmCategory]:
    return await FilmCategoryDAO.find_all(**request_body.to_dict())


@router.get("/{film_id}/{category_id}", summary="Получить связь фильма и категории")
async def get_film_and_category(request_body: RBFilmCategory = Depends()) -> SFilmCategory:
    response = await FilmCategoryDAO.find_one_or_none_by_two_ids(request_body.film_id, request_body.category_id)
    if response: 
        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Фильма с таким id не существует!')


@router.post("/add/")
async def add_film_category(film_category: SFilmCategoryAdd) -> dict:
    check = await FilmCategoryDAO.add(**film_category.dict())
    if check:
        return {"message": "Связь категории с фильмом успешно добавлена!", "film_category": film_category}
    else:
        return {"message": "Ошибка при добавлении связи!"}
    

@router.delete("/del/{film_id}/{category_id}")
async def dell_film_category_by_id(film_id: int, category_id: int) -> dict:
    check = await FilmCategoryDAO.delete(film_id = film_id, category_id = category_id)
    if check:
        return {"message": f"Связь фильма {film_id} c категорией {category_id} удалена!"}
    else:
        return {"message": "Ошибка при удалении связи!"}
    

@router.put("/update/")
async def update_film(
    filmCategory: SFilmCategory
) -> dict:
    try:
        film_id = filmCategory.dict().pop('id1')
        category_id = filmCategory.dict().pop('id2')
        check = await FilmCategoryDAO.update(filter_by={'film_id': film_id, 'category_id': category_id}, **filmCategory.dict())
        if check:
            return {"message": f"Связь ID {filmCategory.id} успешно обновлен!"}
        else:
            return {"message": "Ошибка обновления связи."}
    except Exception as e:
        return {"message": f"Ошибка: {str(e)}"}
