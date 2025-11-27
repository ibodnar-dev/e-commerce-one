from uuid import UUID

from sqlmodel import Session

from app.domain.models import Category
from app.domain.models.data import CategoryCreate, CategoryUpdate
from app.domain.ports.repositories import CategoryRepository
from app.external.adapters.logging import get_logger
from app.external.adapters.repositories.exceptions import RepositoryError

logger = get_logger(__name__)


class SQLCategoryRepository(CategoryRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, category: CategoryCreate) -> Category:
        try:
            db_category = Category.model_validate(category)
            self._session.add(db_category)
            self._session.flush()
            return db_category
        except Exception as e:
            logger.exception(f"Error creating category: {e}", extra={"category": category})
            raise RepositoryError(f"Error creating category: {e}") from e

    def update(self, category_id: str, update_model: CategoryUpdate) -> Category:
        try:
            db_category = self.find_by_id(category_id)
            if not db_category:
                raise RepositoryError(f"Category with ID {category_id} not found")
            category_data = update_model.model_dump(exclude_unset=True)
            db_category.sqlmodel_update(category_data)
            self._session.add(db_category)
            self._session.flush()
            return db_category
        except Exception as e:
            logger.exception(f"Error updating category: {e}", extra={"update_model": update_model})
            raise RepositoryError(f"Error updating category: {e}") from e

    def delete(self, category_id: str) -> None:
        pass

    def find_by_id(self, category_id: str) -> Category | None:
        try:
            return self._session.get(Category, UUID(category_id))
        except Exception as e:
            logger.exception(f"Error finding category by ID: {e}", extra={"category_id": category_id})
            raise RepositoryError(f"Error finding category by ID: {e}") from e
