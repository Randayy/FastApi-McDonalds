from fastapi import APIRouter, HTTPException
import json
from app.services.product_service import ProductService

product_router = APIRouter()


@product_router.get("/all_products/")
async def get_all_products():
    service = ProductService()
    return await service.get_all_products()


@product_router.get("/product/{product_name}")
async def get_product(product_name: str):
    service = ProductService()
    return await service.get_product(product_name)


@product_router.get("/product/{product_name}/{product_field}")
async def get_product_field(product_name: str, product_field: str):
    service = ProductService()
    return await service.get_product_field(product_name, product_field)
