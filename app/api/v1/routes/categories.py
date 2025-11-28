from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.v1.dependencies import get_category_repository
from app.domain.models.data import CategoryCreate, CategoryPublic, CategoryUpdate
from app.domain.ports.repositories import CategoryRepository
from app.domain.services import category as category_service

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("", response_model=CategoryPublic, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Create a new category.
    """
    return category_service.create(category=category, repo=repository)


@router.get("/{category_id}", response_model=CategoryPublic)
def get_category(
    category_id: str,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Get a category by ID.
    """
    return category_service.find_by_id(category_id, repo=repository)


@router.put("/{category_id}", response_model=CategoryPublic)
def update_category(
    category_id: str,
    category_update: CategoryUpdate,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Update a category.
    """
    return category_service.update(category_id, category_update, repo=repository)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: str,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Delete a category.
    """
    category_service.delete(category_id, repo=repository)
