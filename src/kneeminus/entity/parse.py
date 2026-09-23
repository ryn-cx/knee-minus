# TODO: Validate
"""Read the essentials of a movie or a series out of its page."""

from __future__ import annotations

import re
from typing import Any

from kneeminus.parsing import (
    browse_url,
    entity_id,
    episode_numbers,
    image,
    mapping,
    number_or_none,
    plain_text,
    sequence,
    text_or_none,
    texts,
)

HERO_TYPE = "DetailEntityHero"
"""The component the page leads with, which is the title and its artwork."""

DETAILS_TYPE = "MediaDetails"
"""The component that lists what the page says about the title."""

EPISODES_TYPE = "Episodes"
"""The component that lists the episodes of the season being shown."""

RECOMMENDATIONS_SECTION_ID = "you-may-also-like"
"""The id of the section that lists the "You May Also Like" titles."""

IMAGE_CARD_TYPE = "ImageCard"
"""The component a recommended title is shown as."""

BROWSE_PATH = "/browse/"
"""What a recommended title's link starts with, before its slug."""

FIRST_YEAR = re.compile(r"\d{4}")
"""The year a release is written with, which is the first one of a range."""


# TODO: Validate
def parse_entity(page: Any) -> dict[str, Any]:  # noqa: ANN401 - Any JSON value.
    """Return the essentials of an entity page, as the parsed model reads them."""
    page_props = mapping(mapping(mapping(page).get("props")).get("pageProps"))
    page_id = text_or_none(page_props.get("pageId"))
    main_content = sequence(
        mapping(page_props.get("stitchDocument")).get("mainContent"),
    )
    hero = _component(main_content, HERO_TYPE)
    details = _component(main_content, DETAILS_TYPE)
    episodes = _component(main_content, EPISODES_TYPE)
    release = text_or_none(details.get("release")) or text_or_none(
        hero.get("releaseYear"),
    )
    maturity_rating = _maturity_rating(details)

    return {
        "page_id": page_id,
        "entity_id": entity_id(page_id),
        "url": browse_url(page_id),
        "language": text_or_none(page_props.get("language")),
        "region": text_or_none(page_props.get("region")),
        "has_content": bool(page_props.get("hasContent")),
        "title": text_or_none(details.get("title")),
        "series_title": text_or_none(episodes.get("seriesTitle")),
        "category": _category(details.get("customField")),
        "synopsis": plain_text(hero.get("synopsisText")),
        "summary": plain_text(details.get("summary")),
        "release": release,
        "release_year": _release_year(release),
        "runtime_ms": number_or_none(details.get("runtimeMs")),
        "seasons_available": text_or_none(hero.get("seasonsAvailable")),
        "genres": texts(details.get("genres")) or texts(hero.get("genres")),
        "maturity_rating": maturity_rating,
        "advisories": _advisories(details),
        "features": _features(hero, maturity_rating),
        "credits": _credits(details),
        "background_image": image(hero.get("backgroundImage")),
        "title_visual": image(hero.get("titleVisual")),
        "selected_season_id": text_or_none(episodes.get("selectedSeasonId")),
        "seasons": _seasons(episodes),
        "recommendations": _recommendations(
            _section(main_content, RECOMMENDATIONS_SECTION_ID),
        ),
    }


# TODO: Validate
def _component(main_content: list[Any], component_type: str) -> dict[str, Any]:
    """Return the first component of this type the page is built from."""
    for listed_component in main_content:
        component = mapping(listed_component)
        if component.get("_type") == component_type:
            return component
    return {}


# TODO: Validate
def _section(main_content: list[Any], section_id: str) -> dict[str, Any]:
    """Return the section of the page with this id."""
    for listed_component in main_content:
        component = mapping(listed_component)
        if component.get("id") == section_id:
            return component
    return {}


# TODO: Validate
def _category(custom_field: Any) -> str | None:  # noqa: ANN401 - Any JSON value.
    """Return what kind of title this is, e.g. `Movie`."""
    written_field = text_or_none(custom_field)
    if written_field is None:
        return None
    _label, _, category = written_field.partition(":")
    return text_or_none(category.strip())


# TODO: Validate
def _release_year(release: str | None) -> int | None:
    """Return the year a title was released, as the first year of its range."""
    if not release:
        return None
    found = FIRST_YEAR.search(release)
    return int(found[0]) if found else None


# TODO: Validate
def _ratings(details: dict[str, Any]) -> list[dict[str, Any]]:
    """Return every rating the page gives the title."""
    return [mapping(rating) for rating in sequence(details.get("ratings"))]


# TODO: Validate
def _maturity_rating(details: dict[str, Any]) -> str | None:
    """Return the age rating of the title, e.g. `TV-14`."""
    for rating in _ratings(details):
        if name := text_or_none(mapping(rating.get("image")).get("alt")):
            return name
    return None


# TODO: Validate
def _advisories(details: dict[str, Any]) -> list[str]:
    """Return what the rating warns the title carries, e.g. `Violence`."""
    return [
        advisory
        for rating in _ratings(details)
        for advisory in texts(rating.get("advisories"))
    ]


# TODO: Validate
def _features(hero: dict[str, Any], maturity_rating: str | None) -> list[str]:
    """Return what the title is marked as offering, e.g. `audio_description`.

    The icons a title is marked with are its rating followed by its features,
    so the rating is left out here.
    """
    return [
        name
        for icon in sequence(hero.get("detailIcons"))
        if (name := text_or_none(mapping(icon).get("_id"))) and name != maturity_rating
    ]


# TODO: Validate
def _credits(details: dict[str, Any]) -> list[dict[str, Any]]:
    """Return everyone the title credits, grouped by what they are credited as."""
    credited: list[dict[str, Any]] = []
    for listed_credit in sequence(details.get("credits")):
        credit = mapping(listed_credit)
        heading = text_or_none(credit.get("heading"))
        credited.append(
            {
                "heading": heading.rstrip(": ") if heading else None,
                "names": [
                    name
                    for person in sequence(credit.get("items"))
                    if (name := text_or_none(mapping(person).get("displayText")))
                ],
            },
        )
    return credited


# TODO: Validate
def _seasons(episodes: dict[str, Any]) -> list[dict[str, Any]]:
    """Return every season of the series, with the episodes the page lists.

    The page carries the episodes of the season it is showing, and the ones of
    every other season are written out for search engines.
    """
    episodes_by_season = _episodes_by_season(episodes)
    selected_season_id = text_or_none(episodes.get("selectedSeasonId"))
    seasons: list[dict[str, Any]] = []
    for position, listed_season in enumerate(sequence(episodes.get("seasons")), 1):
        season = mapping(listed_season)
        season_id = text_or_none(season.get("id"))
        season_episodes = _episodes(episodes_by_season.get(season_id, []))
        seasons.append(
            {
                "season_id": season_id,
                "name": text_or_none(season.get("name")),
                "season_number": _season_number(season_episodes, position),
                "is_selected": season_id == selected_season_id,
                "episodes": season_episodes,
            },
        )
    return seasons


# TODO: Validate
def _episodes_by_season(episodes: dict[str, Any]) -> dict[str | None, list[Any]]:
    """Return the episodes the page lists, keyed by the season they belong to."""
    listed_episodes = {
        text_or_none(episodes.get("selectedSeasonId")): sequence(
            episodes.get("episodes"),
        ),
    }
    for listed_season in sequence(episodes.get("seoSeasons")):
        season = mapping(listed_season)
        listed_episodes[text_or_none(season.get("seasonId"))] = sequence(
            season.get("episodes"),
        )
    return listed_episodes


# TODO: Validate
def _season_number(season_episodes: list[dict[str, Any]], position: int) -> int:
    """Return which season this is, as its episodes number it or as it is listed."""
    for season_episode in season_episodes:
        if season_episode["season_number"] is not None:
            return season_episode["season_number"]
    return position


# TODO: Validate
def _episodes(listed_episodes: list[Any]) -> list[dict[str, Any]]:
    """Return the episodes of one season, as the cards that list them give them."""
    return [
        _episode(listed_episode, position)
        for position, listed_episode in enumerate(listed_episodes, 1)
    ]


# TODO: Validate
def _episode(listed_episode: Any, position: int) -> dict[str, Any]:  # noqa: ANN401
    """Return one episode, as the card that lists it gives it."""
    episode = mapping(listed_episode)
    title = text_or_none(episode.get("title"))
    season_number, episode_number, name = episode_numbers(title)
    return {
        "episode_id": text_or_none(episode.get("_id")),
        "title": title,
        "name": name,
        "season_number": season_number,
        "episode_number": episode_number or position,
        "summary": plain_text(mapping(episode.get("metadata")).get("summary")),
        "image": image(episode.get("imageVariants")),
    }


# TODO: Validate
def _recommendations(section: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the titles listed under "You May Also Like"."""
    return [
        _recommendation(card)
        for slider in sequence(section.get("children"))
        for slider_item in sequence(mapping(slider).get("children"))
        for listed_card in sequence(mapping(slider_item).get("children"))
        if (card := mapping(listed_card)).get("_type") == IMAGE_CARD_TYPE
    ]


# TODO: Validate
def _recommendation(card: dict[str, Any]) -> dict[str, Any]:
    """Return one recommended title, as the card that lists it gives it."""
    card_url = text_or_none(card.get("url"))
    page_id = card_url.removeprefix(BROWSE_PATH) if card_url else None
    return {
        "page_id": page_id,
        "entity_id": entity_id(page_id),
        "title": text_or_none(card.get("title")),
        "url": browse_url(page_id),
        "image": image(card.get("imageVariants")),
    }
