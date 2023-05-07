"""Модуль для валидации json-схем в response post-запроса, какие должны быть поля и какие типы"""

from datetime import datetime

from pydantic import BaseModel, validator
from pydantic.class_validators import Optional
from schemas.validation_of_fields import ValidationOfFields


class Post(BaseModel):
    first_name: Optional[str]
    email: Optional[str]
    name: Optional[str]
    job: Optional[str]
    id: int
    createdAt: datetime

    @validator('email')
    def check_that_dog_presented_in_email_adress(cls, email):
        ValidationOfFields.check_that_dog_presented_in_email_adress(email)


class PostUnseccessful(BaseModel):
    error: str
