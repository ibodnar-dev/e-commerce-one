from uuid import UUID

from sqlmodel import SQLModel

from app.domain.models.db import CategoryBase


class CategoryCreate(CategoryBase): ...


class CategoryPublic(CategoryBase):
    id: UUID


class CategoryUpdate(SQLModel):
    name: str | None = None
    parent_id: UUID | None = None
