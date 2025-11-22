from app.external.exceptions import ExternalException


class RepositoryException(ExternalException):
    """Base repository exception."""


class DatabaseException(RepositoryException):
    """Raised when a database operation fails."""
