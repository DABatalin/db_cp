from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_validator


class SCategory(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str = Field(..., min_length=1, max_length=50, description="Название категории, от 1 до 50 символов")

    

class SCategoryAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Название категории, от 1 до 50 символов")
    