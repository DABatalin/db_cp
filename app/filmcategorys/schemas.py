from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator


class SFilmCategory(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    film_id: int
    category_id: int

    

class SFilmCategoryAdd(BaseModel):
    film_id: int
    category_id: int
    