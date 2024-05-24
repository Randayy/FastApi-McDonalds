from fastapi import FastAPI
from app.routers.product_routes import product_router

app = FastAPI(debug=True)

app.include_router(product_router,tags=["Products"])
