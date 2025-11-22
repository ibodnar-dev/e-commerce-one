from app.external.exceptions import ExternalError


class RepositoryError(ExternalError):
    """Base repository exception."""


class DBError(RepositoryError):
    """Raised when a database operation fails."""
