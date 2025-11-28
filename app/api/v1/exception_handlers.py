from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.domain.services.exceptions import EntityNotFoundError, ServiceException
from app.external.adapters.logging.python_logger import get_logger

logger = get_logger(__name__)


async def entity_not_found_handler(request: Request, exc: EntityNotFoundError) -> JSONResponse:  # noqa: ARG001
    """
    Handle EntityNotFoundError exceptions by returning a 404 response.
    """
    logger.info("Entity not found: %s", exc)
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": str(exc)},
    )


async def service_exception_handler(request: Request, exc: ServiceException) -> JSONResponse:  # noqa: ARG001
    """
    Handle ServiceException exceptions by returning a 500 response.
    """
    logger.error("Service exception: %s", exc, exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": str(exc)},
    )


async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:  # noqa: ARG001
    """
    Handle unexpected exceptions by returning a 500 response.
    This is a catch-all for any exceptions not handled by more specific handlers.
    """
    logger.exception("Unexpected error: %s", exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )
