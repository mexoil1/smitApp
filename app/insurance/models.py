from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel
from typing import Dict, List


class Material(models.Model):
    """Модель материалов."""
    id = fields.IntField(pk=True)
    type = fields.TextField(null=False)
    price = fields.FloatField(null=False)


Material_in_Pydantic = pydantic_model_creator(
    Material, name="Material In", exclude_readonly=True)
Material_Pydantic = pydantic_model_creator(Material, name="Material")


class Rate(BaseModel):
    cargo_type: str
    rate: str


class RateData(BaseModel):
    date: str
    tariffs: List[Rate]


class RequestData(BaseModel):
    data: Dict[str, List[Rate]]
