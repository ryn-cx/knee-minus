from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel

from tests.utils import download_and_save, parse_json

if TYPE_CHECKING:
    from kneeminus import KneeMinus
    from kneeminus.entity import Entity


class TestData(BaseModel):
    id: str
    name: str


TEST_DATA = [
    # Test series.
    TestData(
        id="entity-cac75c8f-a9e2-4d95-ac73-1cf1cc7b9568",
        name="The Simpsons",
    ),
    # Test movie.
    TestData(
        id="entity-a21ee2fc-421e-4839-bfcc-0bf2ba815875",
        name="Moana 2",
    ),
]


@pytest.fixture(scope="session")
def endpoint(client: KneeMinus) -> Entity:
    return client.entity


@pytest.fixture(params=TEST_DATA, ids=lambda test_data: test_data.name)
def test_data(request: pytest.FixtureRequest) -> TestData:
    return request.param


class TestEntity:
    def test_download(self, endpoint: Entity, test_data: TestData) -> None:
        download_and_save(
            endpoint,
            test_data.name,
            lambda: endpoint.download(test_data.id),
        )

    def test_parse(self, endpoint: Entity, test_data: TestData) -> None:
        entity = parse_json(endpoint, test_data.name)
        assert (
            entity.props.page_props.stitch_document.main_content[1].title
            == test_data.name
        )

    def test_extract(self, endpoint: Entity, test_data: TestData) -> None:
        entity = parse_json(endpoint, test_data.name)
        assert endpoint.extract(entity).media_details.title == test_data.name
