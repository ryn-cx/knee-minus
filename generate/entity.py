# TODO: Validate
"""Rebuilds EntityModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically
from good_ass_pydantic_integrator import generate_model

from generate.constants import FILES_PATH, KNEEMINUS_PATH
from generate.utils import download_if_missing
from kneeminus import KneeMinus

ENTITIES = [
    # Moana 2, a movie.
    ("entity-a21ee2fc-421e-4839-bfcc-0bf2ba815875", None),
    # The Mandalorian, a series.
    ("entity-422f6dcc-226f-44e7-98d4-22de69b31cf3", None),
    # The Mandalorian, season 1.
    (
        "entity-422f6dcc-226f-44e7-98d4-22de69b31cf3",
        "38ff3861-23ba-44b4-a2de-d756de57ba41",
    ),
]
"""Each entity the model is built from, with the season it was asked for."""


# TODO: Validate
def recording_name(entity_id: str, season_id: str | None) -> str:
    """Return the name the recording for an entity and a season is filed under."""
    if season_id is None:
        return entity_id
    return f"{entity_id}-season-{season_id}"


# TODO: Validate
def generate_entity(client: KneeMinus) -> None:
    """Rebuild EntityModel."""
    for entity_id, season_id in ENTITIES:
        download_if_missing(
            FILES_PATH,
            "EntityModel",
            recording_name(entity_id, season_id),
            lambda entity_id=entity_id, season_id=season_id: client.entity.download(
                entity_id,
                season_id=season_id,
            ),
        )
    generate_model(FILES_PATH, KNEEMINUS_PATH, "EntityModel")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_entity(KneeMinus(build_client_automatically()))
