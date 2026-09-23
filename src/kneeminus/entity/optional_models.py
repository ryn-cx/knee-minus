from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Any

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    heading: str | None = None
    names: list[str] | None = None

class BackgroundImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_id: UUID | None = None
    alt: str | None = None
    url: str | None = None

class TitleVisual(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_id: UUID | None = None
    alt: str | None = None
    url: str | None = None

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_id: UUID | None = None
    alt: str | None = None
    url: str | None = None

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    episode_id: UUID | None = None
    title: str | None = None
    name: str | None = None
    season_number: int | None = None
    episode_number: int | None = None
    summary: str | None = None
    image: Image | None = None

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_id: UUID | None = None
    name: str | None = None
    season_number: int | None = None
    is_selected: bool | None = None
    episodes: list[Episode] | None = None

class Recommendation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_id: str | None = None
    entity_id: UUID | None = None
    title: str | None = None
    url: str | None = None
    image: Image | None = None

class EntityModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_id: str | None = None
    entity_id: UUID | None = None
    url: str | None = None
    language: str | None = None
    region: str | None = None
    has_content: bool | None = None
    title: str | None = None
    series_title: str | None = None
    category: str | None = None
    synopsis: str | None = None
    summary: str | None = None
    release: str | None = None
    release_year: int | None = None
    runtime_ms: int | None = None
    seasons_available: str | None = None
    genres: list[str] | None = None
    maturity_rating: str | None = None
    advisories: list[Any] | None = None
    features: list[str] | None = None
    credits: list[Credit] | None = None
    background_image: Any | BackgroundImage | None = None
    title_visual: Any | TitleVisual | None = None
    selected_season_id: Any | UUID | None = None
    seasons: list[Season] | None = None
    recommendations: list[Recommendation] | None = None
    _raw_input: Any = PrivateAttr(default=None)

    @model_validator(mode='wrap')
    @classmethod
    def _capture_raw_input(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
        """Validate the model and keep the input it was built from."""
        model = handler(data)
        model._raw_input = data
        return model

    @property
    def raw_input(self) -> Any:
        """The input this model was validated from, as it was handed over."""
        return self._raw_input
