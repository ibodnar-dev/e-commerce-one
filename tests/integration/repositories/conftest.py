import pytest

from app.external.adapters.repositories.category import SQLCategoryRepository
from app.external.db import DefaultSession


@pytest.fixture(scope="class")
def db_session():
    session = DefaultSession()
    try:
        yield session
        session.commit()
    finally:
        session.rollback()
        session.close()


@pytest.fixture()
def category_repo(db_session):
    yield SQLCategoryRepository(session=db_session)
