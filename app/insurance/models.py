from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Rates(models.Model):
    """Модель тарифов."""
    id = fields.IntField(pk=True)
    type = fields.TextField(null=False)
    price = fields.FloatField(null=False)
    days = fields.IntField(null=False)
    period = fields.IntField(null=False)
    discount_amount = fields.FloatField(null=True)


Rate_in_Pydantic = pydantic_model_creator(
    Rates, name="Rate In", exclude_readonly=True)
Rates_Pydantic = pydantic_model_creator(Rates, name="Rate")


class Material(models.Model):
    """Модель материалов."""
    id = fields.IntField(pk=True)
    type = fields.TextField(null=False)
    price = fields.FloatField(null=False)


Material_in_Pydantic = pydantic_model_creator(
    Material, name="Material In", exclude_readonly=True)
Material_Pydantic = pydantic_model_creator(Material, name="Material")


class Order(models.Model):
    """Модель вычисления стоимости страховки."""
    id = fields.IntField(pk=True)
    material = fields.TextField()
    rate = fields.TextField()
    count = fields.IntField()


Order_in_Pydantic = pydantic_model_creator(
    Order, name="Order In", exclude_readonly=True)
