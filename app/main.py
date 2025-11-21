from fastapi import FastAPI

from app.api.v1 import v1_router

app = FastAPI(
    title="API",
    description="REST API",
    version="1.0.0",
)

app.include_router(v1_router)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
