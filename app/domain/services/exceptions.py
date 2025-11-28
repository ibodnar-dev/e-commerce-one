from app.domain.exceptions import DomainException


class ServiceException(DomainException):
    """
    Base services exception.
    """


class EntityNotFoundError(ServiceException):
    """
    Raised when an entity is not found in the repository.
    """

    def __init__(self, entity_type: str, entity_id: str):
        self.entity_type = entity_type
        self.entity_id = entity_id
        super().__init__(f"{entity_type} with ID '{entity_id}' not found")


class EntityAlreadyExistsError(ServiceException):
    """
    Raised when attempting to create an entity that already exists.
    """

    def __init__(self, entity_type: str, identifier: str):
        self.entity_type = entity_type
        self.identifier = identifier
        super().__init__(f"{entity_type} with identifier '{identifier}' already exists")
