# TODO: Validate
import pytest
from get_around import build_client_automatically

from kneeminus import KneeMinus


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> KneeMinus:
    return KneeMinus(build_client_automatically())
