import os

import pytest
from fastapi.testclient import TestClient

from app.domain.models import SQLModel
from app.external.db import create_tables, default_engine
from app.external.db.connection import drop_tables
from app.main import app
from app.settings.environments import Environment


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    create_tables()
    SQLModel.metadata.create_all(default_engine)
    yield
    if os.environ.get("ENV") == Environment.e2e.value:
        drop_tables()


@pytest.fixture(scope="session")
def test_client():
    yield TestClient(app)


@pytest.fixture(scope="session")
def category_create_payload():
    return {"name": "test category"}


@pytest.fixture(scope="session")
def created_category(test_client, category_create_payload):
    response = test_client.post("/api/v1/categories", json=category_create_payload)
    return response.json()
