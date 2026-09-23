# TODO: Validate
from __future__ import annotations

from pathlib import Path

import pytest

from kneeminus import KneeMinus

FILES_PATH = Path(__file__).parent.parent / "generate" / "_files"
"""The recorded pages, which are parsed without going near the network."""

MOVIE_ID = "entity-a21ee2fc-421e-4839-bfcc-0bf2ba815875"
"""Moana 2, a film."""

SEASON_ID = "38ff3861-23ba-44b4-a2de-d756de57ba41"
"""Season 1 of The Mandalorian."""

SERIES_NAME = f"entity-422f6dcc-226f-44e7-98d4-22de69b31cf3-season-{SEASON_ID}"
"""The Mandalorian, shown at its first season."""

EMPTY_ID = "entity-36611632-719a-4389-978f-3cb6866707f3"
"""A page the region has nothing on."""

MOVIE_RELEASE_YEAR = 2024
"""The year Moana 2 came out."""

MOVIE_RUNTIME_MS = 6204000
"""How long Moana 2 runs, in milliseconds."""

SEASON_EPISODE_COUNT = 8
"""How many episodes each season of The Mandalorian has."""

RECOMMENDATION_COUNT = 8
"""How many titles Moana 2 lists under "You May Also Like"."""

MOANA_ID = "entity-e8896bfa-1052-41f7-ae2e-00255d77cf05"
"""Moana, the first title Moana 2 recommends."""


# TODO: Validate
@pytest.fixture(scope="session")
def client() -> KneeMinus:
    return KneeMinus()


# TODO: Validate
def recorded(name: str) -> str:
    return (FILES_PATH / "EntityModel" / f"{name}.json").read_text(encoding="utf-8")


# TODO: Validate
def test_movie(client: KneeMinus) -> None:
    movie = client.entity.load(recorded(MOVIE_ID))

    assert movie.page_id == MOVIE_ID
    assert movie.url.endswith(MOVIE_ID)
    assert movie.has_content
    assert movie.title == "Moana 2"
    assert movie.category == "Movie"
    assert movie.release_year == MOVIE_RELEASE_YEAR
    assert movie.runtime_ms == MOVIE_RUNTIME_MS
    assert "Animation" in movie.genres
    assert movie.maturity_rating == "PG"
    assert movie.features == ["audio_description", "closed_captions"]
    assert movie.credits[0].heading == "Director"
    assert "David G. Derrick, Jr." in movie.credits[0].names
    assert movie.background_image
    assert movie.background_image.url.startswith("https://")
    assert not movie.seasons


# TODO: Validate
def test_recommendations(client: KneeMinus) -> None:
    movie = client.entity.load(recorded(MOVIE_ID))
    first_recommendation = movie.recommendations[0]

    assert len(movie.recommendations) == RECOMMENDATION_COUNT
    assert first_recommendation.title == "Moana"
    assert first_recommendation.page_id == MOANA_ID
    assert str(first_recommendation.entity_id) in MOANA_ID
    assert first_recommendation.url.endswith(MOANA_ID)
    assert str(first_recommendation.image.image_id) in first_recommendation.image.url


# TODO: Validate
def test_series(client: KneeMinus) -> None:
    series = client.entity.load(recorded(SERIES_NAME))

    assert series.title == "The Mandalorian"
    assert series.series_title == "The Mandalorian"
    assert series.seasons_available == "3 Seasons"
    assert series.maturity_rating == "TV-14"
    assert str(series.selected_season_id) == SEASON_ID
    assert [season.season_number for season in series.seasons] == [1, 2, 3]
    assert [season.is_selected for season in series.seasons] == [True, False, False]


# TODO: Validate
def test_episodes(client: KneeMinus) -> None:
    series = client.entity.load(recorded(SERIES_NAME))
    # The page carries the episodes of the season it is showing, and the ones of
    # every other season are written out for search engines.
    last_season = series.seasons[-1]
    first_episode = last_season.episodes[0]

    assert len(last_season.episodes) == SEASON_EPISODE_COUNT
    assert first_episode.title == "S3:E1 Chapter 17: The Apostate"
    assert first_episode.name == "Chapter 17: The Apostate"
    assert first_episode.season_number == len(series.seasons)
    assert first_episode.episode_number == 1
    assert first_episode.summary
    # An episode the page loads later carries no address, so its address is
    # built from the id it is served under.
    assert str(first_episode.image.image_id) in first_episode.image.url


# TODO: Validate
def test_empty_page(client: KneeMinus) -> None:
    page = client.entity.load(recorded(EMPTY_ID))

    assert page.page_id == EMPTY_ID
    assert not page.has_content
    assert page.title is None
    assert not page.seasons
    assert not page.recommendations
