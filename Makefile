.PHONY: test-e2e test-integration test-unit test-all help build-app-dev

help:
	@echo "Available commands:"
	@echo "  make build-app-dev     - Build the application Docker image"
	@echo "  make test-unit         - Run unit tests"
	@echo "  make test-integration  - Run integration tests (ENV=integration)"
	@echo "  make test-e2e          - Run e2e tests (ENV=e2e)"
	@echo "  make test-all          - Run all tests in sequence"

dc-up-db-dev:
	@echo "Starting postgres-dev"
	docker-compose -f infra/docker/local/docker-compose.yaml up postgres-dev -d

dc-up-db-test:
	@echo "Starting postgres-dev"
	docker-compose -f infra/docker/local/docker-compose.yaml up postgres-test -d --wait

dc-down:
	@echo "Stopping all docker containers"
	docker-compose -f infra/docker/local/docker-compose.yaml down

build-app-dev:
	@echo "Building application Docker image"
	docker build -f infra/docker/local/Dockerfile -t e-commerce-one:latest .

test-unit:
	@echo "Running unit tests..."
	source .venv/bin/activate && pytest tests/unit -vs

test-integration: dc-up-db-test
	@echo "Running integration tests with ENV=integration..."
	source .venv/bin/activate && export ENV=integration && db-setup && pytest tests/integration -v

test-e2e: dc-up-db-test
	@echo "Running e2e tests with ENV=e2e..."
	source .venv/bin/activate && export ENV=integration && db-setup && pytest tests/e2e -v

test-all:
	@echo "Running all test suites..."
	@$(MAKE) test-unit
	@$(MAKE) test-integration
	@$(MAKE) test-e2e
