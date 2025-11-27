from abc import abstractmethod, ABC
from uuid import UUID

from app.domain.models import Category
from app.domain.models.data import CategoryUpdate


class CategoryRepository(ABC):
    @abstractmethod
    def create(self, category: Category) -> Category:
        """
        Create a new category. To create a subcategory,
        set the parent_id field to the ID of the parent category.
        """

    @abstractmethod
    def update(self, category_id: str, category: CategoryUpdate) -> Category:
        """
        Update an existing category.
        """

    @abstractmethod
    def delete(self, category_id: str) -> None:
        """
        Delete a category.
        """

    @abstractmethod
    def find_by_id(self, category_id: str) -> Category | None:
        """
        Find a category by ID. If the category does not exist, return None.
        """
