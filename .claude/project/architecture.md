# FastAPI Hexagonal Architecture Starter - Architecture

## Architectural Style

This project follows **Hexagonal Architecture** (Ports & Adapters) combined with **Domain-Driven Design** principles.

## Directory Structure

### Current Structure

```
app/
├── api/                      # API Layer (FastAPI routes)
│   ├── routes/
│   │   └── __init__.py       # Route modules go here
│   ├── schemas.py            # Request/Response models (Pydantic)
│   └── dependencies.py       # FastAPI dependency injection
│
├── domain/                   # Core Domain Layer
│   ├── models/
│   │   └── __init__.py       # Domain entities (business objects)
│   ├── ports/
│   │   └── repositories/     # Repository interfaces (output ports)
│   ├── services/             # Domain services (business logic)
│   └── exceptions.py         # Domain-specific exceptions
│
├── external/                 # Infrastructure Layer (Adapters)
│   ├── adapters/
│   │   ├── repositories/
│   │   │   └── exceptions.py       # Repository exceptions
│   │   └── logging/
│   │       └── python_logger.py    # Logging adapter
│   ├── db/
│   │   ├── connection.py     # Database connection management
│   │   ├── sequences.py      # Database sequences (ID generation)
│   │   └── cli.py            # Database CLI commands
│   └── exceptions.py         # Infrastructure exceptions
│
├── settings/                 # Configuration Layer
│   ├── base.py               # Base settings
│   └── environments.py       # Environment-specific settings
│
└── main.py                   # Application entry point

tests/                        # Test Suite
├── e2e/                      # End-to-end tests
├── integration/              # Integration tests
└── unit/                     # Unit tests
```

### API Layer (`app/api/`)

**Purpose**: HTTP interface layer using FastAPI.

**Components**:
- `routes/` - Endpoint definitions organized by resource
- `schemas.py` - Pydantic models for request/response validation
- `dependencies.py` - Dependency injection setup

**Key Principles**:
- Thin layer that delegates to domain services
- Handles HTTP concerns (validation, serialization, status codes)
- Depends on domain layer, not vice versa

### Domain Layer (`app/domain/`)

**Purpose**: Contains the application core, business logic, and interface definitions (ports).

**Components**:
- `models/` - Domain entities
- `ports/repositories/` - Repository interfaces (output ports)
- `services/` - Domain services (business logic)
- `exceptions.py` - Domain-specific exceptions

**Key Principles**:
- Defines contracts/interfaces that the application needs
- No dependencies on external libraries or frameworks
- Stable and rarely changes
- Infrastructure depends on this, not vice versa

### Infrastructure Layer (`app/external/`)

**Purpose**: Contains concrete implementations of ports and external system integrations.

**Components**:
- `adapters/repositories/` - SQL repository implementations
- `adapters/logging/` - Logging implementations
- `db/` - Database utilities and connection management

**Key Principles**:
- Implements interfaces defined in `domain/ports/`
- Depends on domain (dependency inversion)
- Can be swapped without affecting domain logic
- Contains framework-specific and technology-specific code

### Settings Layer (`app/settings/`)

**Purpose**: Application configuration management.

**Components**:
- `base.py` - Base configuration settings
- `environments.py` - Environment-specific configurations (dev, prod, test)

## Dependency Direction

```
┌─────────────────────────────────────────┐
│           API Layer (FastAPI)           │
│          app/api/routes/                │
└──────────────┬──────────────────────────┘
               │ depends on
               ↓
┌─────────────────────────────────────────┐
│          Domain Layer (Core)            │
│    app/domain/models/                   │
│    app/domain/ports/                    │
│    app/domain/services/                 │
└──────────────┬──────────────────────────┘
               ↑ implements
               │
┌──────────────┴──────────────────────────┐
│    Infrastructure Layer (Adapters)      │
│    app/external/adapters/               │
│    app/external/db/                     │
└─────────────────────────────────────────┘
```

**Critical Rule**: Dependencies point INWARD toward the domain. The domain never imports from infrastructure or API layers.

## Repository Pattern

**Interface Location**: `app/domain/ports/repositories/`
- Defines the contract for data access
- Uses domain entities
- Abstract base classes or Protocols

**Implementation Location**: `app/external/adapters/repositories/`
- Concrete implementations (SQL, NoSQL, etc.)
- Implements port interfaces
- Handles persistence details

### Example

```python
# app/domain/ports/repositories/item_repository.py
from abc import ABC, abstractmethod
from app.domain.models.item import Item

class ItemRepository(ABC):
    @abstractmethod
    async def find_by_id(self, item_id: str) -> Item | None:
        pass

    @abstractmethod
    async def save(self, item: Item) -> None:
        pass

# app/external/adapters/repositories/sql_item.py
from app.domain.ports.repositories.item_repository import ItemRepository
from app.domain.models.item import Item

class SQLItemRepository(ItemRepository):
    async def find_by_id(self, item_id: str) -> Item | None:
        # PostgreSQL implementation using SQLModel
        pass

    async def save(self, item: Item) -> None:
        # PostgreSQL implementation using SQLModel
        pass
```

## Benefits

1. **Testability**: Mock ports easily without touching adapters
2. **Flexibility**: Swap database, external APIs, or messaging systems without changing domain
3. **Clarity**: Clear separation between business logic and technical details
4. **Maintainability**: Changes to infrastructure don't ripple into domain
