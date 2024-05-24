from fastapi import HTTPException
import json
from app.schemas.product_schemas import ProductSchema, ProductFieldSchema

class ProductService:
    def __init__(self):
        pass

    async def open_file(self):
        try:
            with open('items.json', 'r', encoding='utf8') as f:
                items = json.load(f)
            return items
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="items.json not found")

    async def get_all_products(self) -> dict:
        items = await self.open_file()
        return items
        
    async def get_product(self, product_name: str) -> ProductSchema:
        items = await self.open_file()
        for item in items:
            if item["name"] == product_name:
                return ProductSchema(**item)
        raise HTTPException(status_code=404, detail="Product not found")
        
    async def get_product_field(self, product_name: str, product_field: str) -> ProductFieldSchema:
        items = await self.open_file()
        for item in items:
            if item["name"] == product_name:
                if item.get(product_field):
                    return ProductFieldSchema(field=product_field, value=item[product_field])
                else:
                    raise HTTPException(status_code=404, detail="Field not found")

        raise HTTPException(status_code=404, detail="Product not found")