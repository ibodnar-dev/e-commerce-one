from fastapi import APIRouter

from app.api.v1.routes.categories import router as categories_router

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(categories_router)
