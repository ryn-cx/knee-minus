"""Contains the KneeMinus class."""

from __future__ import annotations

import json
import re
import time
from http import HTTPStatus
from logging import NullHandler, getLogger
from typing import Any

from get_around import GetAround

from kneeminus.entity import Entity
from kneeminus.exceptions import ExtractionError, HTTPError

logger = getLogger(__name__)
logger.addHandler(NullHandler())

_NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(?P<json>.*?)</script>',
    re.DOTALL,
)


class KneeMinus:
    """Disney+ API wrapper."""

    def __init__(
        self,
        get_around_client: GetAround | None = None,
        locale: str = "en-US",
    ) -> None:
        """Initialize the KneeMinus client."""
        self.locale = locale
        self.get_around_client = get_around_client or GetAround()

        self.entity = Entity(self)

    def _headers(self) -> dict[str, str]:
        return {
            # "Host": Set by httpx
            # "User-Agent": Set by httpx
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": f"{self.locale},en;q=0.9",
            # "Accept-Encoding": Set by httpx
            "Referer": "https://www.disneyplus.com/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0, i",
        }

    @staticmethod
    def _extract_next_data(html: str) -> dict[str, Any]:
        match = _NEXT_DATA_RE.search(html)
        if match is None:
            msg = "Could not find __NEXT_DATA__ script tag in the page HTML"
            raise ExtractionError(msg)
        parsed: dict[str, Any] = json.loads(match.group("json"))
        return parsed

    def download(self, url: str, *, log_id: str) -> dict[str, Any]:
        """Download a page and return its decoded `__NEXT_DATA__` JSON."""
        logger.debug("Downloading: %s", log_id)
        start = time.monotonic()
        response = self.get_around_client.get(
            url,
            headers=self._headers(),
            follow_redirects=True,
        )
        if response.status_code != HTTPStatus.OK:
            raise HTTPError(response.status_code, response.text)
        logger.debug("Downloaded %s (%.4f s)", log_id, time.monotonic() - start)
        return self._extract_next_data(response.text)
