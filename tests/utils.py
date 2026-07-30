# TODO: Validate
"""Utils."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path
    from typing import Any

    from good_ass_pydantic_integrator import GAPIBaseModel, GAPIClient

    from kneeminus.base_api_endpoint import BaseEndpoint


def json_path(gapi_client: GAPIClient[Any], name: str) -> Path:
    return gapi_client.json_files_folder() / f"{name}.json"


def multipage_json_path(gapi_client: GAPIClient[Any], name: str) -> Path:
    return (
        gapi_client.json_files_folder().parent
        / "Multipage"
        / gapi_client.json_files_folder().stem
        / f"{name}.json"
    )


def errors_json_path(gapi_client: GAPIClient[Any], name: str) -> Path:
    return (
        gapi_client.json_files_folder().parent
        / "Errors"
        / gapi_client.json_files_folder().stem
        / f"{name}.json"
    )


def json_content[T: GAPIBaseModel](gapi_client: BaseEndpoint[T, ...], name: str) -> str:
    return json_path(gapi_client, name).read_text()


def loaded_json(gapi_client: BaseEndpoint[Any, ...], name: str) -> dict[str, Any]:
    return json.loads(json_content(gapi_client, name))


def parsed_json[T: GAPIBaseModel](gapi_client: BaseEndpoint[T, ...], name: str) -> T:
    return gapi_client.parse(loaded_json(gapi_client, name))


def page_dicts(
    gapi_client: BaseEndpoint[Any, ...],
    name: str,
) -> list[dict[str, Any]]:
    """Recorded page(s) as a list of raw dicts, wrapping a single page."""
    content: list[dict[str, Any]] | dict[str, Any] = json.loads(
        json_path(gapi_client, name).read_text(),
    )
    return content if isinstance(content, list) else [content]


def page_models[T: GAPIBaseModel](
    gapi_client: BaseEndpoint[T, ...],
    name: str,
) -> list[T]:
    """Recorded page(s) as a list of parsed models, wrapping a single page."""
    return [gapi_client.parse(page) for page in page_dicts(gapi_client, name)]


def download_and_save(
    gapi_client: GAPIClient[Any],
    name: str,
    get: Callable[[], dict[str, Any] | list[dict[str, Any]]],
) -> Path:
    file = json_path(gapi_client, name)
    if file.exists():
        pytest.skip(f"File already recorded for {type(gapi_client).__name__}/{name}")
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps(get(), indent=2))
    return file


def assert_error(
    gapi_client: GAPIClient[Any],
    name: str,
    download: Callable[[], object],
    error: type[Exception],
) -> None:
    if get_error_path(gapi_client, name).exists():
        pytest.skip(f"File already recorded for {type(gapi_client).__name__}/{name}")
    with pytest.raises(error) as excinfo:
        download()
    record_error(gapi_client, name, getattr(excinfo.value, "response", None))


def get_error_path(gapi_client: GAPIClient[Any], name: str) -> Path:
    return errors_json_path(gapi_client, name)


def record_error(
    gapi_client: GAPIClient[Any],
    name: str,
    data: dict[str, Any] | None = None,
) -> None:
    path = get_error_path(gapi_client, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(data, indent=2) if data is not None else ""
    path.write_text(content)
