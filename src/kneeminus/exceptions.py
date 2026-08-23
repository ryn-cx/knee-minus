# TODO: Validate
"""Exceptions."""

from __future__ import annotations

from typing import Any


# TODO: Validate
class KneeMinusError(Exception):
    """Base exception for KneeMinus."""

    response: str | dict[str, Any] | None = None
    """The response that caused the error."""


# TODO: Validate
class HTTPError(KneeMinusError):
    """Raised when HTTP request fails with unexpected status code."""

    # TODO: Validate
    def __init__(
        self,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize the HTTPError with the status code and response body."""
        self.status_code = status_code
        self.response = response
        super().__init__(f"Unexpected response status code: {status_code}")


# TODO: Validate
class ResourceNotFoundError(HTTPError):
    """Raised when the site reports that the requested page does not exist."""


# TODO: Validate
class EntityNotFoundError(ResourceNotFoundError):
    """Raised when the requested entity does not exist."""

    # TODO: Validate
    def __init__(
        self,
        entity_id: str,
        status_code: int,
        response: str | dict[str, Any] | None,
    ) -> None:
        """Initialize with the entity id and the originating response."""
        self.entity_id = entity_id
        super().__init__(status_code, response)


# TODO: Validate
class ExtractionError(KneeMinusError):
    """Raised when the downloaded page carries no __NEXT_DATA__ script."""

    # TODO: Validate
    def __init__(self, response: str) -> None:
        """Initialize with the page the script was looked for in."""
        self.response = response
        super().__init__("The downloaded page carries no __NEXT_DATA__ script")
