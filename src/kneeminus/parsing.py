# TODO: Validate
"""Helpers the parsed models are read out of a page with.

A page is read as the JSON it was rendered from rather than through a model of
the whole of it, since the whole of it is far larger than the parts that are
kept.
"""

from __future__ import annotations

import re
from typing import Any

BROWSE_URL = "https://www.disneyplus.com/browse/{slug}"
"""Where a page is served."""

RIPCUT_URL = (
    "https://disney.images.edge.bamgrid.com/ripcut-delivery/v2/variant/disney/"
    "{image_id}/compose?format=webp&width={width}"
)
"""Where an image is served, for an image the page names but does not link to."""

IMAGE_WIDTH = 800
"""How wide an image built from its id is asked for."""

LINE_BREAK_TAG = re.compile(r"<br\s*/?>", re.IGNORECASE)
"""The tag a summary breaks its lines with."""

HTML_TAG = re.compile(r"<[^>]+>")
"""Any other tag a summary is written with."""

ENTITY_SLUG_PREFIX = "entity-"
"""What the id of an entity is written after in the slug its page is named by."""

EPISODE_TITLE = re.compile(r"^S(?P<season>\d+):E(?P<episode>\d+)\s+(?P<name>.+)$")
"""How an episode title writes which season and episode it is."""

NUMBERED_EPISODE_TITLE = re.compile(
    r"^(?:[^:]+:\s*)?E(?P<episode>\d+)\s+(?P<name>.+)$",
)


# TODO: Validate
def mapping(value: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return `value` when it is an object, and an empty one when it is not."""
    return value if isinstance(value, dict) else {}


# TODO: Validate
def sequence(value: Any) -> list[Any]:  # noqa: ANN401 - Any JSON value.
    """Return `value` when it is a list, and an empty one when it is not."""
    return value if isinstance(value, list) else []


# TODO: Validate
def text_or_none(value: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return `value` as text, with a missing or empty value as None."""
    if value is None:
        return None
    text = str(value)
    return text or None


# TODO: Validate
def number_or_none(value: Any) -> float | None:  # noqa: ANN401 - Any JSON value.
    """Return `value` when it is a number, and None when it is not."""
    if isinstance(value, bool) or not isinstance(value, int | float):
        return None
    return value


# TODO: Validate
def texts(values: Any) -> list[str]:  # noqa: ANN401 - Any JSON value.
    """Return a list of values as the text each one is written as."""
    return [str(value) for value in sequence(values) if value is not None]


# TODO: Validate
def plain_text(value: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return text written with HTML tags as the text alone."""
    text = text_or_none(value)
    if text is None:
        return None
    return text_or_none(HTML_TAG.sub("", LINE_BREAK_TAG.sub("\n", text)).strip())


# TODO: Validate
def browse_url(slug: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the address the page named by `slug` is served at."""
    if not (name := text_or_none(slug)):
        return None
    return BROWSE_URL.format(slug=name)


# TODO: Validate
def entity_id(slug: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return the id of the entity a page slug names."""
    if not (name := text_or_none(slug)):
        return None
    return text_or_none(name.removeprefix(ENTITY_SLUG_PREFIX))


# TODO: Validate
def image(raw_image: Any) -> dict[str, Any] | None:  # noqa: ANN401 - Any JSON value.
    """Return one image, as the component that carries it gives it.

    An image the page loads later carries no address, so its address is built
    from the id it is served under.
    """
    named_image = mapping(raw_image)
    if not named_image:
        return None
    default_image = mapping(named_image.get("defaultImage"))
    image_id = text_or_none(default_image.get("ripcutId"))
    url = text_or_none(default_image.get("source"))
    return {
        "image_id": image_id,
        "alt": text_or_none(named_image.get("alt")),
        "url": url or _built_url(image_id),
    }


# TODO: Validate
def _built_url(image_id: str | None) -> str | None:
    """Return the address an image with this id is served at."""
    if not image_id:
        return None
    return RIPCUT_URL.format(image_id=image_id, width=IMAGE_WIDTH)


# TODO: Validate
def episode_numbers(title: Any) -> tuple[int | None, int | None, str | None]:  # noqa: ANN401
    """Return the season, the episode number and the name an episode title writes.

    A title that is not written that way keeps its whole text as the name.
    """
    name = text_or_none(title)
    if name is None:
        return None, None, None
    found = EPISODE_TITLE.match(name)
    if found is not None:
        return int(found["season"]), int(found["episode"]), found["name"]
    found = NUMBERED_EPISODE_TITLE.match(name)
    if found is None:
        return None, None, name
    return None, int(found["episode"]), found["name"]
