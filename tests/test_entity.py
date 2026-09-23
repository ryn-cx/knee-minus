# TODO: Validate
from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest

from kneeminus.exceptions import EntityNotFoundError

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

NOT_ENTITIES = [
    pytest.param(
        "entity-00000000-0000-0000-0000-000000000000",
        id="entity that does not exist",
    ),
    pytest.param("0000000", id="id that is not an entity slug"),
]


# TODO: Validate
@pytest.mark.parametrize(("entity_id", "season_id"), ENTITIES)
def test_download(client: KneeMinus, entity_id: str, season_id: str | None) -> None:
    entity = client.entity(entity_id, season_id=season_id)

    assert entity.page_id == entity_id
    assert entity.title
    if season_id is not None:
        assert entity.selected_season_id == UUID(season_id)


# TODO: Validate
@pytest.mark.parametrize("entity_id", NOT_ENTITIES)
def test_download_invalid(client: KneeMinus, entity_id: str) -> None:
    with pytest.raises(EntityNotFoundError):
        client.entity.download(entity_id)
