# TODO: Validate
"""Rebuilds EntityModel."""

from __future__ import annotations

import logging

from get_around import build_client_automatically

from generate.constants import FILES_PATH, KNEEMINUS_PATH
from generate.utils import download_if_missing, load_ids, rebuild_model
from kneeminus import KneeMinus
from kneeminus.entity import read_entity

ENTITIES = load_ids("EntityModel")
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
    rebuild_model(
        FILES_PATH,
        KNEEMINUS_PATH,
        "EntityModel",
        read_entity,
        name_of=lambda entity: recording_name(*entity),
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_entity(KneeMinus(build_client_automatically()))
