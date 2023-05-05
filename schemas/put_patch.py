"""Модуль для валидации json-схем в response put и patch запросах, какие должны быть поля и какие типы"""

from datetime import datetime

from pydantic import BaseModel
from pydantic.class_validators import Optional


class PutPatch(BaseModel):
    first_name: Optional[str]
    second_name: Optional[str]
    name: Optional[str]
    job: Optional[str]
    updatedAt: datetime
