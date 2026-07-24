import pytest
from get_around import build_client_automatically

from kneeminus import KneeMinus


@pytest.fixture(scope="session")
def client() -> KneeMinus:
    return KneeMinus(get_around_client=build_client_automatically())
