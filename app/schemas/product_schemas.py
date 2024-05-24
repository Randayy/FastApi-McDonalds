from pydantic import BaseModel

class ProductSchema(BaseModel):
    name: str
    description: str
    weight: float
    calories: float
    proteins: float
    fats: float
    carbs: float
    НЖК: float
    Цукор: float
    Ingridients: str
    Alergens: str

class ProductFieldSchema(BaseModel):
    field: str
    value: str