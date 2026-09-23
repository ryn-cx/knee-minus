# ruff: noqa: D100
from typing import TYPE_CHECKING

from good_ass_pydantic_integrator import load

from .optional_models import EntityModel as OptionalModel
from .strict_models import EntityModel as StrictModel

if TYPE_CHECKING:
    from .strict_models import (
        BackgroundImage,
        Credit,
        EntityModel,
        Episode,
        Image,
        Recommendation,
        Season,
        TitleVisual,
    )
else:
    from .optional_models import (
        BackgroundImage,
        Credit,
        EntityModel,
        Episode,
        Image,
        Recommendation,
        Season,
        TitleVisual,
    )

__all__ = [
    "BackgroundImage",
    "Credit",
    "EntityModel",
    "Episode",
    "Image",
    "Recommendation",
    "Season",
    "TitleVisual",
    "model_validate_json",
]


def model_validate_json(data: str | bytes | object, log_id: str) -> EntityModel:
    """Read a downloaded file into EntityModel."""
    return load.model_validate_json(StrictModel, OptionalModel, data, log_id)
