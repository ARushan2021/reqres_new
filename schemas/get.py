"""Модуль для валидации json-схем в response get-запроса, какие должны быть поля и какие типы"""

from pydantic import BaseModel, validator

from schemas.validation_of_fields import ValidationOfFields


class Data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @validator('email')
    def check_that_dog_presented_in_email_adress(cls, email):
        ValidationOfFields.check_that_dog_presented_in_email_adress(email)

    @validator('avatar')
    def check_that_https_in_avatar(cls, web_link):
        ValidationOfFields.check_that_https_in_link(web_link)


class Support(BaseModel):
    url: str
    text: str

    @validator('url')
    def check_that_https_in_avatar(cls, web_link):
        ValidationOfFields.check_that_https_in_link(web_link)


class Get(BaseModel):
    data: Data
    support: Support
