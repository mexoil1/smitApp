from fastapi import APIRouter
from typing import List

from .models import (Rates, Material,
                     Rates_Pydantic, Rate_in_Pydantic,
                     Material_in_Pydantic, Material_Pydantic,
                     Order_in_Pydantic)


router = APIRouter(
    prefix="/insurance",
    tags=["Insurance"]
)


@router.get('/ratesList', response_model=List[Rates_Pydantic])
async def get_rates():
    """Вывод всех тарифов."""
    return await Rates_Pydantic.from_queryset(Rates.all())


@router.post("/createRate", response_model=Rates_Pydantic)
async def create_rate(rate: Rate_in_Pydantic):
    """Добавление тарифа."""
    user_obj = await Rates.create(**rate.dict(exclude_unset=True))
    return await Rates_Pydantic.from_tortoise_orm(user_obj)


@router.get('/material', response_model=List[Material_Pydantic])
async def get_material():
    """Вывод списка всех материалов."""
    return await Material_Pydantic.from_queryset(Material.all())


@router.post("/createMaterial", response_model=Material_Pydantic)
async def create_material(material: Material_in_Pydantic):
    """Добавление материала."""
    user_obj = await Material.create(**material.dict(exclude_unset=True))
    return await Material_Pydantic.from_tortoise_orm(user_obj)


@router.post("/createOrder")
async def create_order(order: Order_in_Pydantic):
    """Вычисление стоимости страховки."""
    material = order.dict(exclude_unset=True)["material"]
    rate = order.dict(exclude_unset=True)["rate"]
    count = order.dict(exclude_unset=True)["count"]
    print(count)
    matPrice = await Material.filter(type=material).values('price')
    ratePrice = await Rates.filter(type=rate).values('price')
    resPrice = int(ratePrice[0]['price']) * int(matPrice[0]['price']) * count
    return {"Цена страхования": resPrice}
