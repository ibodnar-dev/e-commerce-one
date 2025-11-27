from app.domain.models.data import CategoryCreate
from app.external.adapters.repositories.category import SQLCategoryRepository


class TestCategoryCRUD:
    category_name = "test category"

    def test_create(self, category_repo: SQLCategoryRepository):
        category = CategoryCreate(name=self.category_name)
        created = category_repo.create(category)

        assert created.name == self.category_name
        assert created.parent_id is None

    def test_update(self, category_repo: SQLCategoryRepository): ...
