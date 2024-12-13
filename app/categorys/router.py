from fastapi import APIRouter, Depends, HTTPException, status

from app.categorys.dao import CategoryDAO
from app.categorys.rb import RBCategory
from app.categorys.schemas import SCategory, SCategoryAdd


router = APIRouter(prefix='/categorys', tags=['Работа с категориями'])


@router.get("/", summary="Получить все категории")
async def get_all_categorys(request_body: RBCategory = Depends()) -> list[SCategory]:
    return await CategoryDAO.find_all(**request_body.to_dict())


@router.get("/{category_id}", summary="Получить одну категорию по айди")
async def get_category(request_body: RBCategory = Depends()) -> SCategory:
    response = await CategoryDAO.find_one_or_none_by_id(request_body.id)
    if response: 
        return response 
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Категории с таким id не существует!')


@router.post("/add/")
async def add_category(category: SCategoryAdd) -> dict:
    check = await CategoryDAO.add(**category.dict())
    if check:
        return {"message": "Категория успешно добавлена!", "category": category}
    else:
        return {"message": "Ошибка при добавлении категории!"}
    

@router.delete("/del/{category_id}")
async def dell_category_by_id(category_id: int) -> dict:
    check = await CategoryDAO.delete(id=category_id)
    if check:
        return {"message": f"Категория с ID {category_id} удалена!"}
    else:
        return {"message": "Ошибка при удалении категории!"}
    
    
@router.put("/update/")
async def update_category(
    category: SCategory
) -> dict:
    try:
        print(category.dict())
        id = category.dict().pop('id')
        check = await CategoryDAO.update(filter_by={'id': id}, **category.dict())
        if check:
            return {"message": f"Категория с ID {category.id} успешно обновлена!"}
        else:
            return {"message": "Ошибка обновления катгории или категория не найден."}
    except Exception as e:
        return {"message": f"Ошибка: {str(e)}"}
