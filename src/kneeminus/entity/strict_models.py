from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import BaseModel
from uuid import UUID
from typing import Any

class Credit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    heading: str
    names: list[str]

class BackgroundImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_id: UUID
    alt: str
    url: str

class TitleVisual(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_id: UUID
    alt: str
    url: str

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    image_id: UUID
    alt: str
    url: str

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    episode_id: UUID
    title: str
    name: str
    season_number: int
    episode_number: int
    summary: str
    image: Image

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    season_id: UUID
    name: str
    season_number: int
    is_selected: bool
    episodes: list[Episode]

class Recommendation(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_id: str
    entity_id: UUID
    title: str
    url: str
    image: Image

class EntityModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_id: str
    entity_id: UUID
    url: str
    language: str
    region: str
    has_content: bool
    title: str | None
    series_title: str | None
    category: str | None
    synopsis: str | None
    summary: str | None
    release: str | None
    release_year: int | None
    runtime_ms: int | None
    seasons_available: str | None
    genres: list[str]
    maturity_rating: str | None
    advisories: list[None]
    features: list[str]
    credits: list[Credit]
    background_image: BackgroundImage | None
    title_visual: TitleVisual | None
    selected_season_id: UUID | None
    seasons: list[Season]
    recommendations: list[Recommendation]
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
