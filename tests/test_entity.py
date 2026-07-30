from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parsed_json

if TYPE_CHECKING:
    from kneeminus import KneeMinus
    from kneeminus.entity import Entity


class TestData(BaseModel):
    id: UUID
    name: str
    season_id: UUID | None = None
    show_name: str | None = None
    season_name: str | None = None

    @property
    def file_name(self) -> str:
        """Saved JSON file name.

        `show_name` and `season_name` combined when both are set (e.g. a
        specific season), otherwise `show_name`, otherwise `name`.
        """
        if self.show_name and self.season_name:
            return f"{self.show_name} {self.season_name}"
        return self.show_name or self.name


TEST_DATA = [
    # Test series.
    TestData(
        id=UUID("cac75c8f-a9e2-4d95-ac73-1cf1cc7b9568"),
        name="The Simpsons",
    ),
    # Test series, specific season.
    TestData(
        id=UUID("cac75c8f-a9e2-4d95-ac73-1cf1cc7b9568"),
        name="The Simpsons",
        season_id=UUID("fbfaed8f-e7b8-4b24-ab63-c042905f7e47"),
        show_name="The Simpsons",
        season_name="Season 18",
    ),
    # Test movie.
    TestData(
        id=UUID("a21ee2fc-421e-4839-bfcc-0bf2ba815875"),
        name="Moana 2",
    ),
    # Test series that repeats the `Section` entry in `mainContent`.
    TestData(
        id=UUID("e316aa0d-6df1-445b-98d9-ea1d165bcf81"),
        name="CSI: Crime Scene Investigation",
        # The title contains a colon, which is not a valid file name character.
        show_name="CSI Crime Scene Investigation",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: KneeMinus) -> Entity:
    return client.entity


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.file_name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


class TestEntity:
    def test_download(self, endpoint: Entity, test_data: TestData) -> None:
        download_and_save(
            endpoint,
            test_data.file_name,
            lambda: endpoint.download(test_data.id, test_data.season_id),
        )

    def test_parse(self, endpoint: Entity, test_data: TestData) -> None:
        parsed = parsed_json(endpoint, test_data.file_name)
        assert parsed.media_details.title == test_data.name
        if test_data.season_id:
            assert parsed.episodes
            assert parsed.episodes.selected_season_id == test_data.season_id
