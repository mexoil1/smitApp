from fastapi import APIRouter
from typing import List

from .models import Material, Material_in_Pydantic, Material_Pydantic, RequestData


router = APIRouter(
    prefix="/insurance",
    tags=["Insurance"]
)


@router.get('/material', response_model=List[Material_Pydantic])
async def get_material():
    """Вывод списка всех материалов."""
    return await Material_Pydantic.from_queryset(Material.all())


@router.post("/createMaterial", response_model=Material_Pydantic)
async def create_material(material: Material_in_Pydantic):
    """Добавление материала."""
    user_obj = await Material.create(**material.dict(exclude_unset=True))
    return await Material_Pydantic.from_tortoise_orm(user_obj)


@router.post("/calculate_insurance_cost")
async def calculate_insurance_cost(request_data: RequestData):
    """Вычисление стоимости заказа"""
    result = {}
    for date, rates in request_data.data.items():
        result[date] = []
        for rate in rates:
            cargo_type = rate.cargo_type
            rate = rate.rate
            cargoPrice = await Material.filter(type=cargo_type).values("price")
            print(cargoPrice)
            result[date].append({"cargo_price": float(
                cargoPrice[0]['price']) * float(rate)})
            print(result)
    return result
