from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import Field
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import Any

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    heading: str | Any = Field(default=None, union_mode='left_to_right')
    names: list[str] | Any = Field(default=None, union_mode='left_to_right')

class BackgroundImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    alt: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_url: str | Any = Field(default=None, union_mode='left_to_right')

class TitleVisual(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    alt: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_url: str | Any = Field(default=None, union_mode='left_to_right')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    alt: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    thumbnail_url: str | Any = Field(default=None, union_mode='left_to_right')

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    episode_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    episode_number: int | Any = Field(default=None, union_mode='left_to_right')
    summary: str | Any = Field(default=None, union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    name: str | Any = Field(default=None, union_mode='left_to_right')
    season_number: int | Any = Field(default=None, union_mode='left_to_right')
    is_selected: bool | Any = Field(default=None, union_mode='left_to_right')
    episodes: list[Episode] | Any = Field(default=None, union_mode='left_to_right')

class Recommendation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_id: str | Any = Field(default=None, union_mode='left_to_right')
    entity_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    image: Image | Any = Field(default=None, union_mode='left_to_right')

class EntityModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_id: str | Any = Field(default=None, union_mode='left_to_right')
    entity_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    url: str | Any = Field(default=None, union_mode='left_to_right')
    language: str | Any = Field(default=None, union_mode='left_to_right')
    region: str | Any = Field(default=None, union_mode='left_to_right')
    has_content: bool | Any = Field(default=None, union_mode='left_to_right')
    title: str | Any = Field(default=None, union_mode='left_to_right')
    series_title: str | Any = Field(default=None, union_mode='left_to_right')
    category: str | Any = Field(default=None, union_mode='left_to_right')
    synopsis: str | Any = Field(default=None, union_mode='left_to_right')
    summary: str | Any = Field(default=None, union_mode='left_to_right')
    release: str | Any = Field(default=None, union_mode='left_to_right')
    release_year: int | Any = Field(default=None, union_mode='left_to_right')
    runtime_ms: int | Any = Field(default=None, union_mode='left_to_right')
    seasons_available: str | Any = Field(default=None, union_mode='left_to_right')
    genres: list[str] | Any = Field(default=None, union_mode='left_to_right')
    maturity_rating: str | Any = Field(default=None, union_mode='left_to_right')
    advisories: list[Any] | Any = Field(default=None, union_mode='left_to_right')
    features: list[str] | Any = Field(default=None, union_mode='left_to_right')
    credits: list[Credit] | Any = Field(default=None, union_mode='left_to_right')
    background_image: BackgroundImage | Any = Field(default=None, union_mode='left_to_right')
    title_visual: TitleVisual | Any = Field(default=None, union_mode='left_to_right')
    selected_season_id: UUID | Any = Field(default=None, union_mode='left_to_right')
    seasons: list[Season] | Any = Field(default=None, union_mode='left_to_right')
    recommendations: list[Recommendation] | Any = Field(default=None, union_mode='left_to_right')
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
