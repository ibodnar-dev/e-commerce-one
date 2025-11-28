from app.domain.models import Category
from app.domain.models.data import CategoryCreate, CategoryUpdate
from app.domain.ports.repositories import CategoryRepository
from app.domain.services.exceptions import EntityNotFoundError, ServiceException
from app.external.adapters.logging.python_logger import get_logger
from app.external.adapters.repositories.exceptions import RepositoryError

logger = get_logger(__name__)


def create(category: CategoryCreate, repo: CategoryRepository) -> Category:
    logger.info("Creating category: %s", category.name)
    try:
        result = repo.create(category)
        logger.info("Category created successfully with ID: %s", result.id)
        return result
    except RepositoryError as e:
        logger.error("Failed to create category: %s", e)
        raise ServiceException(f"Failed to create category: {e}") from e


def update(category_id: str, category: CategoryUpdate, repo: CategoryRepository) -> Category:
    logger.info("Updating category with ID: %s", category_id)
    try:
        result = repo.update(category_id, category)
        logger.info("Category updated successfully: %s", category_id)
        return result
    except RepositoryError as e:
        logger.error("Failed to update category %s: %s", category_id, e)
        if "not found" in str(e).lower():
            raise EntityNotFoundError("Category", category_id) from e
        raise ServiceException(f"Failed to update category: {e}") from e


def delete(category_id: str, repo: CategoryRepository) -> None:
    logger.info("Deleting category with ID: %s", category_id)
    try:
        repo.delete(category_id)
        logger.info("Category deleted successfully: %s", category_id)
    except RepositoryError as e:
        logger.error("Failed to delete category %s: %s", category_id, e)
        if "not found" in str(e).lower():
            raise EntityNotFoundError("Category", category_id) from e
        raise ServiceException(f"Failed to delete category: {e}") from e


def find_by_id(category_id: str, repo: CategoryRepository) -> Category:
    logger.info("Finding category by ID: %s", category_id)
    try:
        result = repo.find_by_id(category_id)
        if not result:
            logger.info("Category not found: %s", category_id)
            raise EntityNotFoundError("Category", category_id)
        logger.info("Category found: %s", category_id)
        return result
    except RepositoryError as e:
        logger.error("Failed to find category %s: %s", category_id, e)
        raise ServiceException(f"Failed to find category: {e}") from e
