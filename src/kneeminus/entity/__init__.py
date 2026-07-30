"""Contains the Entity class."""

from __future__ import annotations

from logging import NullHandler, getLogger
from typing import TYPE_CHECKING, Any, override
from uuid import UUID

from kneeminus.base_api_endpoint import BaseEndpoint
from kneeminus.entity.models import EntityModel

if TYPE_CHECKING:
    from good_ass_pydantic_integrator.constants import INPUT_TYPE

logger = getLogger(__name__)
logger.addHandler(NullHandler())

# A/B testing scaffolding that carries no media data. It is by far the largest and
# most deeply nested entry in `mainContent`, and modelling it makes generating the
# model take minutes instead of seconds, so it is dropped before validation.
IGNORED_TYPES = frozenset({"ExperimentContainer"})


class Entity(BaseEndpoint[EntityModel, [str | UUID]]):
    """Manage the entity file.

    Downloads https://www.disneyplus.com/browse/entity-<entity_id>, extracts the
    __NEXT_DATA__ JSON from the page, and keeps only `mainContent`, grouped by
    `_type`. The full page JSON is still what gets saved to disk, so the grouping
    is only ever applied on the way into a model.

    Example headers
        - GET /browse/entity-3135b0cb-a002-438d-a9fd-60d86284c93f HTTP/1.1
        - Host: www.disneyplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Sec-GPC: 1
        - Connection: keep-alive
        - Cookie: __REDACTED__
        - Upgrade-Insecure-Requests: 1
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: same-origin
        - Sec-Fetch-User: ?1
        - Priority: u=0, i
    """

    _response_model = EntityModel

    @override
    @classmethod
    def transform_input(cls, data: INPUT_TYPE) -> INPUT_TYPE:  # type: ignore[misc]
        document: Any = data
        main_content = document["props"]["pageProps"]["stitchDocument"]["mainContent"]
        grouped: dict[str, Any] = {}
        for item in main_content:
            key = item["_type"]
            if key in IGNORED_TYPES:
                continue
            if key == "CustomHTML":
                grouped.setdefault(key, []).append(item)
            elif key == "Section":
                # Some pages repeat Section entries, only the first one is used.
                grouped.setdefault(key, item)
            else:
                if key in grouped:
                    msg = f"Duplicate single-item _type {key!r} in main content."
                    raise ValueError(msg)
                grouped[key] = item
        return grouped

    @override
    def download(
        self,
        entity_id: str | UUID,
        season_id: str | UUID | None = None,
    ) -> dict[str, Any]:
        log_id = self.get_log_id(self.download, locals())
        # A bare UUID is turned into the ``entity-<uuid>`` browse slug; a str is
        # used as-is (it may already be the full ``entity-...`` form).
        slug = f"entity-{entity_id}" if isinstance(entity_id, UUID) else entity_id
        url = f"https://www.disneyplus.com/browse/{slug}"
        if season_id is not None:
            url = f"{url}?season={season_id}"
        return self._client.download(url, log_id=log_id)

    @override
    def download_and_parse(
        self,
        entity_id: str | UUID,
        season_id: str | UUID | None = None,
    ) -> EntityModel:
        return self.parse(self.download(entity_id, season_id))
