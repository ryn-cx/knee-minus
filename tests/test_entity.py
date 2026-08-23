# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from kneeminus.entity.models import EntityModel
from kneeminus.exceptions import EntityNotFoundError
from tests.utils import RecordedEndpoint

if TYPE_CHECKING:
    from kneeminus import KneeMinus

ENTITIES = [
    # https://www.disneyplus.com/browse/entity-a21ee2fc-421e-4839-bfcc-0bf2ba815875
    pytest.param(
        "entity-a21ee2fc-421e-4839-bfcc-0bf2ba815875",
        None,
        id="moana 2, a movie",
    ),
    # https://www.disneyplus.com/browse/entity-422f6dcc-226f-44e7-98d4-22de69b31cf3
    pytest.param(
        "entity-422f6dcc-226f-44e7-98d4-22de69b31cf3",
        None,
        id="the mandalorian, a series",
    ),
    pytest.param(
        "entity-422f6dcc-226f-44e7-98d4-22de69b31cf3",
        "38ff3861-23ba-44b4-a2de-d756de57ba41",
        id="the mandalorian, season 1",
    ),
]


# TODO: Validate
def recording_name(entity_id: str, season_id: str | None) -> str:
    """Return the name the recording for an entity and a season is filed under."""
    if season_id is None:
        return entity_id
    return f"{entity_id}-season-{season_id}"


# TODO: Validate
class EntityTest(RecordedEndpoint):
    MODEL = EntityModel
    # The build id and the scripts the page loads change every time Disney+
    # deploys, whichever entity is asked for.
    IGNORED = ("EntityModel.build_id", "EntityModel.script_loader")


# TODO: Validate
@pytest.mark.parametrize(("entity_id", "season_id"), ENTITIES)
def test_download(client: KneeMinus, entity_id: str, season_id: str | None) -> None:
    EntityTest.download_test(
        recording_name(entity_id, season_id),
        lambda: client.entity.download(entity_id, season_id=season_id),
    )


# TODO: Validate
@pytest.mark.parametrize(("entity_id", "season_id"), ENTITIES)
def test_parse(client: KneeMinus, entity_id: str, season_id: str | None) -> None:
    entity = client.entity.load(
        EntityTest.recorded_content(recording_name(entity_id, season_id)),
    )
    assert entity.props.page_props.page_id == entity_id


# TODO: Validate
@pytest.mark.parametrize(
    "entity_id",
    [
        pytest.param(
            "entity-00000000-0000-0000-0000-000000000000",
            id="entity that does not exist",
        ),
        pytest.param("0000000", id="id that is not an entity slug"),
    ],
)
def test_download_invalid(client: KneeMinus, entity_id: str) -> None:
    EntityTest.error_test(
        entity_id,
        lambda: client.entity.download(entity_id),
        EntityNotFoundError,
    )
