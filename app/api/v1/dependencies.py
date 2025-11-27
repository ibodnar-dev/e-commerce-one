from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.domain.ports.repositories import CategoryRepository
from app.external.adapters.repositories import SQLCategoryRepository
from app.external.db import get_managed_db_session


def get_category_repository(
    session: Annotated[Session, Depends(get_managed_db_session)],
) -> CategoryRepository:
    """
    Provides a CategoryRepository instance for dependency injection.
    """
    return SQLCategoryRepository(session)
