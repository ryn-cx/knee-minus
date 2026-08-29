# TODO: Validate
"""Contains the Entity class."""

from __future__ import annotations

import json
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any
from uuid import UUID

from kneeminus.base_api_endpoint import BaseEndpoint
from kneeminus.entity.models import EntityModel, model_validate_json
from kneeminus.exceptions import EntityNotFoundError, ResourceNotFoundError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

STRIPPED_PAGE_PROPS = (
    "remoteConfig",
    "dictionary",
    "debug",
    "metricsData",
    "identitySDKConfig",
)
"""The page props that say nothing about the media.

`remoteConfig` is the site's per-country configuration and `dictionary` its
interface translations; between them they are over ninety per cent of the page.
The rest is telemetry and SDK setup.
"""


# TODO: Validate
def read_entity(data: str) -> dict[str, Any]:
    """Parse a downloaded entity file and drop what is not about the media.

    `load` reads a downloaded page with this, and the model generator reads the
    recorded pages with it too, so the two can never disagree.
    """
    page = json.loads(data)
    page.pop("runtimeConfig", None)
    page_props = page.get("props", {}).get("pageProps", {})
    for name in STRIPPED_PAGE_PROPS:
        page_props.pop(name, None)
    return page


# TODO: Validate
class Entity(BaseEndpoint):
    """Manage the entity file, which is a movie or a series.

    Source: https://www.disneyplus.com/browse/entity-{entity_id}

    Example request:
        - GET /browse/entity-{entity_id} HTTP/1.1
        - Host: www.disneyplus.com
        - User-Agent: __REDACTED__
        - Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
        - Accept-Language: en-US,en;q=0.9
        - Accept-Encoding: gzip, deflate, br, zstd
        - Sec-GPC: 1
        - Connection: keep-alive
        - Referer: https://www.disneyplus.com/
        - Cookie: __REDACTED__
        - Upgrade-Insecure-Requests: 1
        - Sec-Fetch-Dest: document
        - Sec-Fetch-Mode: navigate
        - Sec-Fetch-Site: same-origin
        - Sec-Fetch-User: ?1
        - Priority: u=0, i
    """

    # TODO: Validate
    def __call__(
        self,
        entity_id: str | UUID,
        *,
        season_id: str | UUID | None = None,
    ) -> EntityModel:
        """Look the entity up and return the model it is read into."""
        log_id = self.get_log_id(self.__call__, locals())
        return self.load(self.download(entity_id, season_id=season_id), log_id)

    # TODO: Validate
    def download(
        self,
        entity_id: str | UUID,
        *,
        season_id: str | UUID | None = None,
    ) -> str:
        """Download the entity file."""
        log_id = self.get_log_id(self.download, locals())
        # A bare UUID is turned into the browse slug the site names a page by; a
        # str is used as it is, since it may already be that slug.
        slug = f"entity-{entity_id}" if isinstance(entity_id, UUID) else entity_id
        params = {} if season_id is None else {"season": str(season_id)}
        try:
            response = self._client.download(
                endpoint=f"browse/{slug}",
                params=params,
                headers={"referer": "https://www.disneyplus.com/"},
                log_id=log_id,
            )
        except ResourceNotFoundError as err:
            raise EntityNotFoundError(slug, err.status_code, err.response) from err
        return self._validate_download(response, slug)

    # TODO: Validate
    def _validate_download(self, response: str, slug: str) -> str:
        """Check that the page is the one that was asked for."""
        page_id = json.loads(response)["props"]["pageProps"]["pageId"]
        if page_id != slug:
            raise EntityNotFoundError(slug, HTTPStatus.OK, response)
        return response

    # TODO: Validate
    def load(self, data: str, log_id: str = "") -> EntityModel:
        """Read a downloaded entity file into its model, without the rest of the page.

        Everything the page carries that is not the media is dropped first.
        """
        return model_validate_json(read_entity(data), log_id or self.default_log_id)
