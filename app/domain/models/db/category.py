from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel


class CategoryBase(SQLModel):
    name: str


class Category(CategoryBase, table=True):
    __tablename__ = "categories"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    parent_id: UUID | None = Field(default=None, foreign_key="categories.id")

    # Relationships
    parent: Optional["Category"] = Relationship(
        sa_relationship_kwargs={"remote_side": "Category.id"}
    )
    sub_categories: list["Category"] = Relationship(back_populates="parent")
