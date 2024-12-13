from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator


class SActor(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str = Field(..., min_length=1, max_length=50, description="Название категории, от 1 до 50 символов")
    surname: str = Field(..., min_length=1, max_length=50, description="Название категории, от 1 до 50 символов")
    age: int = Field(..., ge=1, le=100, description="Возраст должен быть в диапазоне от 1 до 100")
    photo_link: str

    

class SActorAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Название категории, от 1 до 50 символов")
    surname: str = Field(..., min_length=1, max_length=50, description="Название категории, от 1 до 50 символов")
    age: int = Field(..., ge=1, le=100, description="Возраст должен быть в диапазоне от 1 до 100")
    photo_link: str