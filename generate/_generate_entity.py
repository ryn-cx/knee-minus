from __future__ import annotations

import json
import logging
from typing import Any

from get_around import build_client_automatically
from good_ass_pydantic_integrator.generate import generate_model
from good_ass_pydantic_integrator.recordings import (
    RecordingId,
    download_missing,
    drop_redundant_recordings,
    load_ids,
)

from generate.constants import GENERATOR_PATHS
from kneeminus import KneeMinus
from kneeminus.entity.parse import parse_entity

MODEL_NAME = "EntityModel"


# TODO: Validate
def read_recording(content: str) -> Any:  # noqa: ANN401 - Any JSON value.
    """Return what a recorded page parses into, which is what the model reads."""
    return parse_entity(json.loads(content))


# TODO: Validate
class EntityId(RecordingId[KneeMinus]):
    entity_id: str
    season_id: str | None = None

    # TODO: Validate
    def recording_name(self) -> str:
        if self.season_id is None:
            return self.entity_id
        return f"{self.entity_id}-season-{self.season_id}"

    # TODO: Validate
    def download(self, client: KneeMinus) -> str:
        return client.entity.download(self.entity_id, season_id=self.season_id)


ENTITIES = load_ids(GENERATOR_PATHS, MODEL_NAME, EntityId)


# TODO: Validate
def generate_entity(client: KneeMinus) -> None:
    download_missing(GENERATOR_PATHS, MODEL_NAME, ENTITIES, client)
    generate_model(
        GENERATOR_PATHS.files_path,
        GENERATOR_PATHS.package_path,
        MODEL_NAME,
        read_recording,
    )
    # Judged on the whole page rather than on what is parsed out of it, so a
    # recording that says something new about the rest of the page is kept.
    drop_redundant_recordings(GENERATOR_PATHS, MODEL_NAME, EntityId)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    generate_entity(KneeMinus(build_client_automatically()))
