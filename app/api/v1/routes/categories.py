from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.v1.dependencies import get_category_repository
from app.domain.models.data import CategoryCreate, CategoryPublic, CategoryUpdate
from app.domain.ports.repositories import CategoryRepository
from app.external.adapters.repositories.exceptions import RepositoryError

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("", response_model=CategoryPublic, status_code=status.HTTP_201_CREATED)
def create_category(
    category: CategoryCreate,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Create a new category.
    """
    try:
        return repository.create(category)
    except RepositoryError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e


@router.get("/{category_id}", response_model=CategoryPublic)
def get_category(
    category_id: str,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Get a category by ID.
    """
    try:
        category = repository.find_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with ID {category_id} not found",
            )
        return category
    except RepositoryError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e


@router.put("/{category_id}", response_model=CategoryPublic)
def update_category(
    category_id: str,
    category_update: CategoryUpdate,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Update a category.
    """
    try:
        return repository.update(category_id, category_update)
    except RepositoryError as e:
        if "not found" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e),
            ) from e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: str,
    repository: Annotated[CategoryRepository, Depends(get_category_repository)],
):
    """
    Delete a category.
    """
    try:
        repository.delete(category_id)
    except RepositoryError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e
