class TestCategoryCRUD:
    def test_create_category(self, created_category, category_create_payload):
        assert created_category["name"] == category_create_payload["name"]
        assert "id" in created_category
        assert created_category["id"] is not None

    def test_get_category(self, test_client, created_category):
        response = test_client.get(f"/api/v1/categories/{created_category['id']}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_category["id"]
        assert data["name"] == created_category["name"]

    def test_update_category(self, test_client, created_category):
        update_payload = {"name": "Fashion"}
        response = test_client.put(
            f"/api/v1/categories/{created_category["id"]}", json=update_payload
        )

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == created_category["id"]
        assert data["name"] == update_payload["name"]

    def test_delete_category(self, test_client, created_category):
        response = test_client.delete(f"/api/v1/categories/{created_category["id"]}")

        assert response.status_code == 204
        assert response.content == b""

        # Verify the category is deleted
        get_response = test_client.get(f"/api/v1/categories/{created_category["id"]}")
        assert get_response.status_code == 404
