from fastapi import FastAPI

from app.api.v1 import v1_router
from app.api.v1.exception_handlers import (
    entity_not_found_handler,
    generic_exception_handler,
    service_exception_handler,
)
from app.domain.services.exceptions import EntityNotFoundError, ServiceException
from app.external.adapters.logging import setup_logging

app = FastAPI(
    title="API",
    description="REST API",
    version="1.0.0",
)

setup_logging()

app.add_exception_handler(EntityNotFoundError, entity_not_found_handler)
app.add_exception_handler(ServiceException, service_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(v1_router)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}
