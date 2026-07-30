from pydantic import ConfigDict, Field
from uuid import UUID
from good_ass_pydantic_integrator import GAPIBaseModel
from typing import Any

class DefaultImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class BackgroundImage(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage = Field(..., alias='xsmallImage')
    small_image: SmallImage = Field(..., alias='smallImage')
    medium_image: MediumImage = Field(..., alias='mediumImage')
    large_image: LargeImage = Field(..., alias='largeImage')
    xlarge_image: XlargeImage = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage = Field(..., alias='xxlargeImage')

class Alignments(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text: str
    vertical: str

class FooterItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[str]
    copy_: str = Field(..., alias='copy')
    common_href: str = Field(..., alias='commonHref')
    href: str
    size: str
    title: str
    type: str
    element_id: str = Field(..., alias='elementId')
    data_test_id: str = Field(..., alias='dataTestId')

class DefaultImage1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MaxWidths(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    sm_max_width: int = Field(..., alias='smMaxWidth')
    md_max_width: int = Field(..., alias='mdMaxWidth')
    lg_max_width: int = Field(..., alias='lgMaxWidth')

class Data(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    class_name: str | None = Field(None, alias='className')
    color: str | None = None

class Mark(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    data: Data | None = None

class ContentItem1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    value: str
    marks: list[Mark]

class ContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    content: list[ContentItem1]

class RichText(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    content: list[ContentItem]

class Child1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    default_image: DefaultImage1 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage1 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage1 | None = Field(None, alias='smallImage')
    medium_image: MediumImage1 | None = Field(None, alias='mediumImage')
    large_image: LargeImage1 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage1 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage1 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    rich_text: RichText | None = Field(None, alias='richText')

class ColSize(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    desktop: int
    tablet: int
    mobile: int

class Child(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alignments: Alignments
    footer: list[FooterItem]
    children: list[Child1]
    col_size: ColSize = Field(..., alias='colSize')
    gap: str
    grid_item_index: int = Field(..., alias='gridItemIndex')

class Offers(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_id: str = Field(..., alias='_id')
    field_type: str = Field(..., alias='_type')
    alignment: str
    children: list[Child]
    col_size: ColSize = Field(..., alias='colSize')
    gap: str

class DefaultImage2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class DetailIcon(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage2 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage2 = Field(..., alias='xsmallImage')
    small_image: SmallImage2 = Field(..., alias='smallImage')
    medium_image: MediumImage2 = Field(..., alias='mediumImage')
    large_image: LargeImage2 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage2 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage2 = Field(..., alias='xxlargeImage')

class DefaultImage3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class SmallImage3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class MediumImage3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class LargeImage3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class TitleVisual(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage3 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage3 = Field(..., alias='xsmallImage')
    small_image: SmallImage3 = Field(..., alias='smallImage')
    medium_image: MediumImage3 = Field(..., alias='mediumImage')
    large_image: LargeImage3 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage3 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage3 = Field(..., alias='xxlargeImage')

class DetailEntityHero(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    background_image: BackgroundImage = Field(..., alias='backgroundImage')
    offers: Offers
    children: None
    detail_icons: list[DetailIcon] = Field(..., alias='detailIcons')
    release_year: str = Field(..., alias='releaseYear')
    seasons_available: str | None = Field(None, alias='seasonsAvailable')
    genres: list[str]
    locale: str
    promotion: None
    promotion_sub_label: None = Field(..., alias='promotionSubLabel')
    synopsis_text: str = Field(..., alias='synopsisText')
    title_visual: TitleVisual = Field(..., alias='titleVisual')
    is_replay_title: bool = Field(..., alias='isReplayTitle')
    loading_strategy: str = Field(..., alias='loadingStrategy')
    runtime_ms: int | None = Field(None, alias='runtimeMs')

class DefaultImage4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Image(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage4 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage4 = Field(..., alias='xsmallImage')
    small_image: SmallImage4 = Field(..., alias='smallImage')
    medium_image: MediumImage4 = Field(..., alias='mediumImage')
    large_image: LargeImage4 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage4 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage4 = Field(..., alias='xxlargeImage')

class Rating(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str
    image: Image
    advisories: list[None]

class Item(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    display_text: str = Field(..., alias='displayText')

class Credit(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    heading: str
    items: list[Item]

class Labels(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    details: str
    genres: str
    release: str
    runtime: str

class MediaDetails(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    title: str
    summary: str
    release: str
    genres: list[str] | None = None
    ratings: list[Rating]
    credits: list[Credit]
    labels: Labels
    locale: str
    loading_strategy: str = Field(..., alias='loadingStrategy')
    runtime_ms: int | None = Field(None, alias='runtimeMs')
    custom_field: str | None = Field(None, alias='customField')

class DefaultImage5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage5(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage5 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage5 = Field(..., alias='xsmallImage')
    small_image: SmallImage5 = Field(..., alias='smallImage')
    medium_image: MediumImage5 = Field(..., alias='mediumImage')
    large_image: LargeImage5 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage5 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage5 = Field(..., alias='xxlargeImage')
    loading: str

class Metadata(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    summary: str

class Payload(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    content_type: str = Field(..., alias='contentType')
    element_id: UUID = Field(..., alias='elementId')
    element_id_type: str = Field(..., alias='elementIdType')
    element_index: int = Field(..., alias='elementIndex')
    element_type: str = Field(..., alias='elementType')
    interaction_type: str = Field(..., alias='interactionType')
    is_authenticated: bool = Field(..., alias='isAuthenticated')
    item_info_block: str = Field(..., alias='itemInfoBlock')
    action_info_block: str = Field(..., alias='actionInfoBlock')
    program_type: str = Field(..., alias='programType')
    content_keys: dict[str, Any] = Field(..., alias='contentKeys')

class Glimpse(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload

class MetricsData(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    glimpse: Glimpse

class Episode(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    title: str
    image_variants: ImageVariants = Field(..., alias='imageVariants')
    aspect_ratio: float = Field(..., alias='aspectRatio')
    loading: str
    metadata: Metadata
    collection_group_key: str = Field(..., alias='collectionGroupKey')
    metrics_data: MetricsData = Field(..., alias='metricsData')

class Season(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    id: UUID
    name: str

class DefaultImage6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage6(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Data1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    class_name: str = Field(..., alias='className')

class Mark1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    data: Data1 | None = None

class ContentItem3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    value: str
    marks: list[Mark1]

class ContentItem2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    content: list[ContentItem3]

class RichText1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    type: str
    content: list[ContentItem2]

class Style(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    color: str

class ModalContentItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str | None = None
    default_image: DefaultImage6 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage6 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage6 | None = Field(None, alias='smallImage')
    medium_image: MediumImage6 | None = Field(None, alias='mediumImage')
    large_image: LargeImage6 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage6 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage6 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    rich_text: RichText1 | None = Field(None, alias='richText')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    common_href: str | None = Field(None, alias='commonHref')
    href: str | None = None
    size: str | None = None
    title: str | None = None
    style: Style | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')
    css: str | None = None

class Style1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    text_align: str = Field(..., alias='textAlign')

class Payload1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    container_style: str = Field(..., alias='containerStyle')
    container_type: str = Field(..., alias='containerType')
    elements: list[None]
    elements_per_width: int = Field(..., alias='elementsPerWidth')
    horizontal_position: int = Field(..., alias='horizontalPosition')
    vertical_position: int = Field(..., alias='verticalPosition')
    container_key: str = Field(..., alias='containerKey')

class Glimpse1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload1

class MetricsData1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    glimpse: Glimpse1

class EpisodeSelectModal(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    is_exit_intent: bool = Field(..., alias='isExitIntent')
    should_open_on_page_load: bool = Field(..., alias='shouldOpenOnPageLoad')
    text_alignment: str = Field(..., alias='textAlignment')
    modal_content: list[ModalContentItem] = Field(..., alias='modalContent')
    style: Style1
    id: str
    metrics_data: MetricsData1 = Field(..., alias='metricsData')

class DefaultImage7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage7(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage7 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage7 = Field(..., alias='xsmallImage')
    small_image: SmallImage7 = Field(..., alias='smallImage')
    medium_image: MediumImage7 = Field(..., alias='mediumImage')
    large_image: LargeImage7 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage7 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage7 = Field(..., alias='xxlargeImage')
    loading: str

class Payload2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    content_type: str = Field(..., alias='contentType')
    element_id: UUID = Field(..., alias='elementId')
    element_id_type: str = Field(..., alias='elementIdType')
    element_index: int = Field(..., alias='elementIndex')
    element_type: str = Field(..., alias='elementType')
    interaction_type: str = Field(..., alias='interactionType')
    is_authenticated: bool = Field(..., alias='isAuthenticated')
    item_info_block: str = Field(..., alias='itemInfoBlock')
    action_info_block: str = Field(..., alias='actionInfoBlock')
    program_type: str = Field(..., alias='programType')
    content_keys: dict[str, Any] = Field(..., alias='contentKeys')

class Glimpse2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload2

class MetricsData2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    glimpse: Glimpse2

class Episode1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    title: str
    image_variants: ImageVariants1 = Field(..., alias='imageVariants')
    aspect_ratio: float = Field(..., alias='aspectRatio')
    loading: str
    metadata: Metadata
    metrics_data: MetricsData2 = Field(..., alias='metricsData')

class SeoSeason(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    season_id: UUID = Field(..., alias='seasonId')
    season_name: str = Field(..., alias='seasonName')
    episodes: list[Episode1]

class Episodes(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    title: str
    series_title: str = Field(..., alias='seriesTitle')
    episodes: list[Episode]
    seasons: list[Season]
    selected_season_id: UUID = Field(..., alias='selectedSeasonId')
    episode_select_modal: EpisodeSelectModal = Field(..., alias='episodeSelectModal')
    loading_strategy: str = Field(..., alias='loadingStrategy')
    seo_seasons: list[SeoSeason] | None = Field(None, alias='seoSeasons')

class Style2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    background: str

class Padding(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    top: str
    bottom: str

class MobileOptions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    full_width: bool = Field(..., alias='fullWidth')
    is_hidden: bool | None = Field(None, alias='isHidden')

class TabletOptions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    full_width: bool = Field(..., alias='fullWidth')

class DesktopOptions(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    full_width: bool = Field(..., alias='fullWidth')

class DefaultImage8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage8(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage8 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage8 = Field(..., alias='xsmallImage')
    small_image: SmallImage8 = Field(..., alias='smallImage')
    medium_image: MediumImage8 = Field(..., alias='mediumImage')
    large_image: LargeImage8 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage8 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage8 = Field(..., alias='xxlargeImage')
    loading: str

class Glimpse3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload2

class MetricsData3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    glimpse: Glimpse3

class Child4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    title: str
    url: str
    image_variants: ImageVariants2 = Field(..., alias='imageVariants')
    aspect_ratio: float = Field(..., alias='aspectRatio')
    loading: str
    index: int
    item_info_block: str = Field(..., alias='itemInfoBlock')
    action_info_block: str = Field(..., alias='actionInfoBlock')
    is_episode: bool = Field(..., alias='isEpisode')
    metrics_data: MetricsData3 = Field(..., alias='metricsData')

class Child3(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    children: list[Child4]

class Title(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    as_: str = Field(..., alias='as')
    children: str
    class_name: str = Field(..., alias='className')
    size: str

class Child2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child3]
    title: Title
    disable_tile_click: bool = Field(..., alias='disableTileClick')
    container_info_block: str = Field(..., alias='containerInfoBlock')
    data_test_id: str = Field(..., alias='dataTestId')
    container_style: str = Field(..., alias='containerStyle')

class Glimpse4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    container_key: str = Field(..., alias='containerKey')
    container_type: str = Field(..., alias='containerType')
    container_style: str = Field(..., alias='containerStyle')
    vertical_position: int = Field(..., alias='verticalPosition')

class MetricsData4(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    glimpse: Glimpse4

class Section(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    id: str
    alignment: str
    style: Style2
    data_testid: str = Field(..., alias='data-testid')
    padding: Padding
    loading_strategy: str = Field(..., alias='loadingStrategy')
    mobile_options: MobileOptions = Field(..., alias='mobileOptions')
    tablet_options: TabletOptions = Field(..., alias='tabletOptions')
    desktop_options: DesktopOptions = Field(..., alias='desktopOptions')
    children: list[Child2]
    metrics_data: MetricsData4 = Field(..., alias='metricsData')

class CustomHtmlItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    html: str | None = None
    css: str | None = None
    js: str | None = None

class PreconnectLink(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    rel: str
    href: str
    cross_origin: str = Field(..., alias='crossOrigin')

class PriorityMetaTag(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    http_equiv: str | None = Field(None, alias='httpEquiv')
    content: str
    name: str | None = None

class MetaTag(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    item_prop: str | None = Field(None, alias='itemProp')
    content: str
    property: str | None = None
    name: str | None = None

class LinkTag(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    rel: str
    href: str

class EpisodeItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    name: str
    episode_number: int = Field(..., alias='episodeNumber')

class ContainsSeasonItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    name: str
    season_number: int = Field(..., alias='seasonNumber')
    episode: list[EpisodeItem]

class Item1(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    field_id: str = Field(..., alias='@id')
    url: str
    name: str

class ItemListElementItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    position: int
    item: Item1

class FieldGraphItem(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='@type')
    image: str | None = None
    name: str | None = None
    description: str | None = None
    content_rating: str | None = Field(None, alias='contentRating')
    date_published: str | None = Field(None, alias='datePublished')
    genre: list[str] | None = None
    primary_image_of_page: str | None = Field(None, alias='primaryImageOfPage')
    contains_season: list[ContainsSeasonItem] | None = Field(None, alias='containsSeason')
    item_list_element: list[ItemListElementItem] | None = Field(None, alias='itemListElement')

class LdJson(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_context: str = Field(..., alias='@context')
    field_graph: list[FieldGraphItem] = Field(..., alias='@graph')

class DebugMetaTag(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    content: str

class Metadata2(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    field_type: str = Field(..., alias='_type')
    locale: str
    title: str
    genre: list[str] | None = None
    preconnect_links: list[PreconnectLink] = Field(..., alias='preconnectLinks')
    priority_meta_tags: list[PriorityMetaTag] = Field(..., alias='priorityMetaTags')
    meta_tags: list[MetaTag] = Field(..., alias='metaTags')
    link_tags: list[LinkTag] = Field(..., alias='linkTags')
    ld_json: LdJson = Field(..., alias='ldJSON')
    debug_meta_tags: list[DebugMetaTag] = Field(..., alias='debugMetaTags')

class EntityModel(GAPIBaseModel):
    model_config = ConfigDict(extra='forbid')
    detail_entity_hero: DetailEntityHero = Field(..., alias='DetailEntityHero')
    media_details: MediaDetails = Field(..., alias='MediaDetails')
    episodes: Episodes | None = Field(None, alias='Episodes')
    section: Section = Field(..., alias='Section')
    custom_html: list[CustomHtmlItem] = Field(..., alias='CustomHTML')
    metadata: Metadata2 = Field(..., alias='Metadata')
