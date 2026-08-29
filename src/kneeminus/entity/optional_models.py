from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from uuid import UUID
from typing import Any

class DefaultImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class BackgroundImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage | None = Field(None, alias='xsmallImage')
    small_image: SmallImage | None = Field(None, alias='smallImage')
    medium_image: MediumImage | None = Field(None, alias='mediumImage')
    large_image: LargeImage | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage | None = Field(None, alias='xxlargeImage')

class Alignments(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text: str | None = None
    vertical: str | None = None

class FooterItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    common_href: str | None = Field(None, alias='commonHref')
    href: str | None = None
    size: str | None = None
    title: str | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')

class DefaultImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MaxWidths(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    sm_max_width: int | None = Field(None, alias='smMaxWidth')
    md_max_width: int | None = Field(None, alias='mdMaxWidth')
    lg_max_width: int | None = Field(None, alias='lgMaxWidth')

class Data(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')
    color: str | None = None

class Mark(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data | None = None

class ContentItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark] | None = None

class ContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem1] | None = None

class RichText(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem] | None = None

class Child1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    default_image: DefaultImage1 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage1 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage1 | None = Field(None, alias='smallImage')
    medium_image: MediumImage1 | None = Field(None, alias='mediumImage')
    large_image: LargeImage1 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage1 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage1 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    rich_text: RichText | None = Field(None, alias='richText')

class ColSize(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: int | None = None
    tablet: int | None = None
    mobile: int | None = None

class Child(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alignments: Alignments | None = None
    footer: list[FooterItem] | None = None
    children: list[Child1] | None = None
    col_size: ColSize | None = Field(None, alias='colSize')
    gap: str | None = None
    grid_item_index: int | None = Field(None, alias='gridItemIndex')

class Offers(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    field_type: str | None = Field(None, alias='_type')
    alignment: str | None = None
    children: list[Child] | None = None
    col_size: ColSize | None = Field(None, alias='colSize')
    gap: str | None = None

class DefaultImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class ImageVariants(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage2 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage2 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage2 | None = Field(None, alias='smallImage')
    medium_image: MediumImage2 | None = Field(None, alias='mediumImage')
    large_image: LargeImage2 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage2 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage2 | None = Field(None, alias='xxlargeImage')
    loading: str | None = None

class Payload(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_type: str | None = Field(None, alias='contentType')
    element_id: UUID | None = Field(None, alias='elementId')
    element_id_type: str | None = Field(None, alias='elementIdType')
    element_index: int | None = Field(None, alias='elementIndex')
    element_type: str | None = Field(None, alias='elementType')
    interaction_type: str | None = Field(None, alias='interactionType')
    is_authenticated: bool | None = Field(None, alias='isAuthenticated')
    item_info_block: str | None = Field(None, alias='itemInfoBlock')
    action_info_block: str | None = Field(None, alias='actionInfoBlock')
    program_type: str | None = Field(None, alias='programType')
    content_keys: dict[str, Any] | None = Field(None, alias='contentKeys')

class Glimpse(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    event_urn: str | None = Field(None, alias='eventUrn')
    payload: Payload | None = None

class MetricsData(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse | None = None

class BadgeRowItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    column_id: str | None = Field(None, alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool | None = Field(None, alias='isHeader')
    is_badge: bool | None = Field(None, alias='isBadge')

class Data1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')

class Mark1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data1 | None = None

class Data2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: str | list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    class_name: str | None = Field(None, alias='className')
    href: str | None = None
    title: str | None = None
    type: str | None = None
    as_: str | None = Field(None, alias='as')

class ContentItem3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    marks: list[Mark1] | None = None
    value: str | None = None
    content: list[Any] | None = None
    data: Data2 | None = None

class ContentItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem3] | None = None

class RichText1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem2] | None = None

class Child6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText1 | None = Field(None, alias='richText')

class Child5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child6] | None = None
    size: str | None = None

class Footer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    field_type: str | None = Field(None, alias='_type')
    children: list[Child5] | None = None
    text_alignment: str | None = Field(None, alias='textAlignment')

class DefaultImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class Data3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')

class Mark2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data3 | None = None

class ContentItem5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark2] | None = None

class ContentItem4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem5] | None = None

class RichText2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem4] | None = None

class CellContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage3 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage3 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage3 | None = Field(None, alias='smallImage')
    medium_image: MediumImage3 | None = Field(None, alias='mediumImage')
    large_image: LargeImage3 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage3 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage3 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    size: str | None = None
    rich_text: RichText2 | None = Field(None, alias='richText')

class HeaderBody(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    column_id: str | None = Field(None, alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool | None = Field(None, alias='isHeader')
    class_name: str | None = Field(None, alias='className')
    cell_content: list[CellContentItem] | None = Field(None, alias='cellContent')

class Style(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None

class CellContentItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: str | list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    common_href: str | None = Field(None, alias='commonHref')
    size: str | None = None
    title: str | None = None
    style: Style | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')
    href: str | None = None
    target_blank: bool | None = Field(None, alias='targetBlank')
    format: list[str] | None = None

class HeaderFooter(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    column_id: str | None = Field(None, alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool | None = Field(None, alias='isHeader')
    cell_content: list[CellContentItem1] | None = Field(None, alias='cellContent')

class HeaderRow1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header_bodies: list[HeaderBody] | None = Field(None, alias='headerBodies')
    header_footers: list[HeaderFooter] | None = Field(None, alias='headerFooters')

class HeaderRow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    header_row: HeaderRow1 | None = Field(None, alias='headerRow')
    column_count: int | None = Field(None, alias='columnCount')
    max_width: str | None = Field(None, alias='maxWidth')

class Mark3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data3 | None = None

class Data5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    as_: str | None = Field(None, alias='as')
    children: str | None = None
    class_name: str | None = Field(None, alias='className')

class ContentItem7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark3] | None = None
    content: list[Any] | None = None
    data: Data5 | None = None

class ContentItem6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem7] | None = None

class RichText3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem6] | None = None

class Child7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText3 | None = Field(None, alias='richText')

class Data6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')

class Mark4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data6 | None = None

class ContentItem9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark4] | None = None

class ContentItem8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem9] | None = None

class RichText4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem8] | None = None

class CellContentItem2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText4 | None = Field(None, alias='richText')
    children: str | None = None
    size: str | None = None

class RowDatum(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child7] | None = None
    cell_content: list[CellContentItem2] | None = Field(None, alias='cellContent')
    column_id: str | None = Field(None, alias='columnId')
    is_selected: bool | None = Field(None, alias='isSelected')

class Row(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    row_data: list[RowDatum] | None = Field(None, alias='rowData')
    id: str | None = None

class BadgeRowItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    column_id: str | None = Field(None, alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool | None = Field(None, alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    is_badge: bool | None = Field(None, alias='isBadge')

class Mark5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data6 | None = None

class Data8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: str | list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    class_name: str | None = Field(None, alias='className')
    href: str | None = None
    title: str | None = None
    type: str | None = None
    as_: str | None = Field(None, alias='as')

class ContentItem11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    marks: list[Mark5] | None = None
    value: str | None = None
    content: list[Any] | None = None
    data: Data8 | None = None

class ContentItem10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem11] | None = None

class RichText5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem10] | None = None

class Child9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText5 | None = Field(None, alias='richText')

class Child8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child9] | None = None
    size: str | None = None

class Footer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    field_type: str | None = Field(None, alias='_type')
    children: list[Child8] | None = None
    text_alignment: str | None = Field(None, alias='textAlignment')

class Data9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')

class Mark6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data9 | None = None

class ContentItem13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark6] | None = None
    content: list[Any] | None = None

class ContentItem12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem13] | None = None

class RichText6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem12] | None = None

class CellContentItem3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText6 | None = Field(None, alias='richText')
    size: str | None = None

class HeaderBody1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    column_id: str | None = Field(None, alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool | None = Field(None, alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    cell_content: Any | list[CellContentItem3] | None = Field(None, alias='cellContent')
    class_name: str | None = Field(None, alias='className')

class Mark7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data9 | None = None

class ContentItem15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark7] | None = None

class ContentItem14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem15] | None = None

class RichText7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem14] | None = None

class Style1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    background: str | None = None
    color: str | None = None

class CellContentItem4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    size: str | None = None
    rich_text: RichText7 | None = Field(None, alias='richText')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    href: str | None = None
    title: str | None = None
    style: Style1 | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')

class HeaderFooter1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    column_id: str | None = Field(None, alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool | None = Field(None, alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    cell_content: list[CellContentItem4] | None = Field(None, alias='cellContent')

class HeaderRow3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    header_bodies: list[HeaderBody1] | None = Field(None, alias='headerBodies')
    header_footers: list[HeaderFooter1] | None = Field(None, alias='headerFooters')

class HeaderRow2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    id: str | None = None
    header_row: HeaderRow3 | None = Field(None, alias='headerRow')
    column_count: int | None = Field(None, alias='columnCount')
    max_width: str | None = Field(None, alias='maxWidth')

class Mark8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data9 | None = None

class ContentItem17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark8] | None = None

class ContentItem16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem17] | None = None

class RichText8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem16] | None = None

class Child10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText8 | None = Field(None, alias='richText')

class Mark9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data9 | None = None

class ContentItem19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark9] | None = None

class ContentItem18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem19] | None = None

class RichText9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem18] | None = None

class CellContentItem5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText9 | None = Field(None, alias='richText')

class RowDatum1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child10] | None = None
    cell_content: list[CellContentItem5] | None = Field(None, alias='cellContent')
    column_id: str | None = Field(None, alias='columnId')
    is_selected: bool | None = Field(None, alias='isSelected')

class Row1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    row_data: list[RowDatum1] | None = Field(None, alias='rowData')
    id: str | None = None

class Subchart(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    badge_row: list[BadgeRowItem1] | None = Field(None, alias='badgeRow')
    column_count: int | None = Field(None, alias='columnCount')
    footer: Footer1 | None = None
    header_row: HeaderRow2 | None = Field(None, alias='headerRow')
    highlighted_column_ids: list[Any] | None = Field(None, alias='highlightedColumnIds')
    is_expandable: bool | None = Field(None, alias='isExpandable')
    is_header_row_with_badge: bool | None = Field(None, alias='isHeaderRowWithBadge')
    max_width: str | None = Field(None, alias='maxWidth')
    rows: list[Row1] | None = None
    should_expand_on_load: bool | None = Field(None, alias='shouldExpandOnLoad')

class Child4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | str | None = Field(None, alias='_id', union_mode='left_to_right')
    title: str | None = None
    url: str | None = None
    image_variants: ImageVariants | None = Field(None, alias='imageVariants')
    aspect_ratio: float | None = Field(None, alias='aspectRatio')
    loading: str | None = None
    index: int | None = None
    item_info_block: str | None = Field(None, alias='itemInfoBlock')
    action_info_block: str | None = Field(None, alias='actionInfoBlock')
    is_episode: bool | None = Field(None, alias='isEpisode')
    metrics_data: MetricsData | None = Field(None, alias='metricsData')
    badge_row: list[BadgeRowItem] | None = Field(None, alias='badgeRow')
    column_count: int | None = Field(None, alias='columnCount')
    custom_top_padding: str | None = Field(None, alias='customTopPadding')
    footer: Footer | None = None
    header_row: HeaderRow | None = Field(None, alias='headerRow')
    highlighted_column_ids: list[Any] | None = Field(None, alias='highlightedColumnIds')
    is_expandable: bool | None = Field(None, alias='isExpandable')
    is_header_row_with_badge: bool | None = Field(None, alias='isHeaderRowWithBadge')
    max_width: str | None = Field(None, alias='maxWidth')
    rows: list[Row] | None = None
    subcharts: list[Subchart] | None = None

class Data13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')
    color: str | None = None

class Mark10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data13 | None = None

class ContentItem21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark10] | None = None

class ContentItem20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem21] | None = None

class RichText10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem20] | None = None

class Child3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | str | None = Field(None, alias='_id', union_mode='left_to_right')
    children: list[Child4] | None = None
    rich_text: RichText10 | None = Field(None, alias='richText')
    tab_id: str | None = Field(None, alias='tabId')
    tab_name: str | None = Field(None, alias='tabName')

class Title(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    as_: str | None = Field(None, alias='as')
    children: str | None = None
    class_name: str | None = Field(None, alias='className')
    size: str | None = None

class CapsuleProps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    button_background: str | None = Field(None, alias='buttonBackground')
    selected_text_color: str | None = Field(None, alias='selectedTextColor')

class Child2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child3] | None = None
    title: Title | None = None
    disable_tile_click: bool | None = Field(None, alias='disableTileClick')
    container_info_block: str | None = Field(None, alias='containerInfoBlock')
    data_test_id: str | None = Field(None, alias='dataTestId')
    container_style: str | None = Field(None, alias='containerStyle')
    size: str | None = None
    initial_tab_id: str | None = Field(None, alias='initialTabId')
    capsule_props: CapsuleProps | None = Field(None, alias='capsuleProps')
    display_mode: str | None = Field(None, alias='displayMode')

class DefaultImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class DetailIcon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage4 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage4 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage4 | None = Field(None, alias='smallImage')
    medium_image: MediumImage4 | None = Field(None, alias='mediumImage')
    large_image: LargeImage4 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage4 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage4 | None = Field(None, alias='xxlargeImage')

class DefaultImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class TitleVisual(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage5 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage5 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage5 | None = Field(None, alias='smallImage')
    medium_image: MediumImage5 | None = Field(None, alias='mediumImage')
    large_image: LargeImage5 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage5 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage5 | None = Field(None, alias='xxlargeImage')

class DefaultImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class Image(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage6 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage6 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage6 | None = Field(None, alias='smallImage')
    medium_image: MediumImage6 | None = Field(None, alias='mediumImage')
    large_image: LargeImage6 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage6 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage6 | None = Field(None, alias='xxlargeImage')

class Rating(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    title: str | None = None
    image: Image | None = None
    advisories: list[Any] | None = None

class Item(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_text: str | None = Field(None, alias='displayText')

class Credit(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    heading: str | None = None
    items: list[Item] | None = None

class Labels(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    details: str | None = None
    genres: str | None = None
    release: str | None = None
    runtime: str | None = None

class DefaultImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class ImageVariants1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage7 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage7 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage7 | None = Field(None, alias='smallImage')
    medium_image: MediumImage7 | None = Field(None, alias='mediumImage')
    large_image: LargeImage7 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage7 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage7 | None = Field(None, alias='xxlargeImage')
    loading: str | None = None

class Metadata(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    summary: str | None = None

class Glimpse1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    event_urn: str | None = Field(None, alias='eventUrn')
    payload: Payload | None = None

class MetricsData1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse1 | None = None

class Episode(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | None = Field(None, alias='_id')
    title: str | None = None
    image_variants: ImageVariants1 | None = Field(None, alias='imageVariants')
    aspect_ratio: float | None = Field(None, alias='aspectRatio')
    loading: str | None = None
    metadata: Metadata | None = None
    collection_group_key: str | None = Field(None, alias='collectionGroupKey')
    metrics_data: MetricsData1 | None = Field(None, alias='metricsData')

class Season(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    id: UUID | None = None
    name: str | None = None

class DefaultImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class Data14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')

class Mark11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data14 | None = None

class ContentItem23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark11] | None = None

class ContentItem22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem23] | None = None

class RichText11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem22] | None = None

class Style2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None

class ModalContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage8 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage8 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage8 | None = Field(None, alias='smallImage')
    medium_image: MediumImage8 | None = Field(None, alias='mediumImage')
    large_image: LargeImage8 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage8 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage8 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    rich_text: RichText11 | None = Field(None, alias='richText')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    common_href: str | None = Field(None, alias='commonHref')
    href: str | None = None
    size: str | None = None
    title: str | None = None
    style: Style2 | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')
    css: str | None = None

class Style3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_align: str | None = Field(None, alias='textAlign')

class Payload2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_style: str | None = Field(None, alias='containerStyle')
    container_type: str | None = Field(None, alias='containerType')
    elements: list[Any] | None = None
    elements_per_width: int | None = Field(None, alias='elementsPerWidth')
    horizontal_position: int | None = Field(None, alias='horizontalPosition')
    vertical_position: int | None = Field(None, alias='verticalPosition')
    container_key: str | None = Field(None, alias='containerKey')

class Glimpse2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    event_urn: str | None = Field(None, alias='eventUrn')
    payload: Payload2 | None = None

class MetricsData2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse2 | None = None

class EpisodeSelectModal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    is_exit_intent: bool | None = Field(None, alias='isExitIntent')
    should_open_on_page_load: bool | None = Field(None, alias='shouldOpenOnPageLoad')
    text_alignment: str | None = Field(None, alias='textAlignment')
    modal_content: list[ModalContentItem] | None = Field(None, alias='modalContent')
    style: Style3 | None = None
    id: str | None = None
    metrics_data: MetricsData2 | None = Field(None, alias='metricsData')

class DefaultImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class ImageVariants2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage9 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage9 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage9 | None = Field(None, alias='smallImage')
    medium_image: MediumImage9 | None = Field(None, alias='mediumImage')
    large_image: LargeImage9 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage9 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage9 | None = Field(None, alias='xxlargeImage')
    loading: str | None = None

class Payload3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    content_type: str | None = Field(None, alias='contentType')
    element_id: UUID | None = Field(None, alias='elementId')
    element_id_type: str | None = Field(None, alias='elementIdType')
    element_index: int | None = Field(None, alias='elementIndex')
    element_type: str | None = Field(None, alias='elementType')
    interaction_type: str | None = Field(None, alias='interactionType')
    is_authenticated: bool | None = Field(None, alias='isAuthenticated')
    item_info_block: str | None = Field(None, alias='itemInfoBlock')
    action_info_block: str | None = Field(None, alias='actionInfoBlock')
    program_type: str | None = Field(None, alias='programType')
    content_keys: dict[str, Any] | None = Field(None, alias='contentKeys')

class Glimpse3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    event_urn: str | None = Field(None, alias='eventUrn')
    payload: Payload3 | None = None

class MetricsData3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse3 | None = None

class Episode1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | None = Field(None, alias='_id')
    title: str | None = None
    image_variants: ImageVariants2 | None = Field(None, alias='imageVariants')
    aspect_ratio: float | None = Field(None, alias='aspectRatio')
    loading: str | None = None
    metadata: Metadata | None = None
    metrics_data: MetricsData3 | None = Field(None, alias='metricsData')

class SeoSeason(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season_id: UUID | None = Field(None, alias='seasonId')
    season_name: str | None = Field(None, alias='seasonName')
    episodes: list[Episode1] | None = None

class Style4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    background: str | None = None

class Padding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    top: str | None = None
    bottom: str | None = None

class MobileOptions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    full_width: bool | None = Field(None, alias='fullWidth')
    is_hidden: bool | None = Field(None, alias='isHidden')

class TabletOptions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    full_width: bool | None = Field(None, alias='fullWidth')
    is_hidden: bool | None = Field(None, alias='isHidden')

class DesktopOptions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    full_width: bool | None = Field(None, alias='fullWidth')

class Glimpse4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_key: str | None = Field(None, alias='containerKey')
    container_type: str | None = Field(None, alias='containerType')
    container_style: str | None = Field(None, alias='containerStyle')
    vertical_position: int | None = Field(None, alias='verticalPosition')

class MetricsData4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse4 | None = None

class PreconnectLink(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rel: str | None = None
    href: str | None = None
    cross_origin: str | None = Field(None, alias='crossOrigin')

class PriorityMetaTag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    http_equiv: str | None = Field(None, alias='httpEquiv')
    content: str | None = None
    name: str | None = None

class MetaTag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    item_prop: str | None = Field(None, alias='itemProp')
    content: str | None = None
    property: str | None = None
    name: str | None = None

class LinkTag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    rel: str | None = None
    href: str | None = None

class EpisodeItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    episode_number: int | None = Field(None, alias='episodeNumber')

class ContainsSeasonItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    name: str | None = None
    season_number: int | None = Field(None, alias='seasonNumber')
    episode: list[EpisodeItem] | None = None

class Item1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    field_id: str | None = Field(None, alias='@id')
    url: str | None = None
    name: str | None = None

class ItemListElementItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    position: int | None = None
    item: Item1 | None = None

class FieldGraphItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='@type')
    image: str | None = None
    name: str | None = None
    description: str | None = None
    content_rating: str | None = Field(None, alias='contentRating')
    date_published: str | None = Field(None, alias='datePublished')
    genre: list[str] | None = None
    primary_image_of_page: str | None = Field(None, alias='primaryImageOfPage')
    contains_season: list[ContainsSeasonItem] | None = Field(None, alias='containsSeason')
    item_list_element: list[ItemListElementItem] | None = Field(None, alias='itemListElement')

class LdJson(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_context: str | None = Field(None, alias='@context')
    field_graph: list[FieldGraphItem] | None = Field(None, alias='@graph')

class DebugMetaTag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    content: str | None = None

class MainContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    background_image: BackgroundImage | None = Field(None, alias='backgroundImage')
    offers: Offers | None = None
    children: Any | list[Child2] | None = None
    detail_icons: list[DetailIcon] | None = Field(None, alias='detailIcons')
    release_year: str | None = Field(None, alias='releaseYear')
    seasons_available: str | None = Field(None, alias='seasonsAvailable')
    genres: list[str] | None = None
    locale: str | None = None
    promotion: Any | None = None
    promotion_sub_label: Any | None = Field(None, alias='promotionSubLabel')
    synopsis_text: str | None = Field(None, alias='synopsisText')
    title_visual: TitleVisual | None = Field(None, alias='titleVisual')
    is_replay_title: bool | None = Field(None, alias='isReplayTitle')
    loading_strategy: str | None = Field(None, alias='loadingStrategy')
    title: str | None = None
    summary: str | None = None
    release: str | None = None
    ratings: list[Rating] | None = None
    credits: list[Credit] | None = None
    labels: Labels | None = None
    series_title: str | None = Field(None, alias='seriesTitle')
    episodes: list[Episode] | None = None
    seasons: list[Season] | None = None
    selected_season_id: UUID | None = Field(None, alias='selectedSeasonId')
    episode_select_modal: EpisodeSelectModal | None = Field(None, alias='episodeSelectModal')
    seo_seasons: list[SeoSeason] | None = Field(None, alias='seoSeasons')
    id: str | None = None
    alignment: str | None = None
    style: Style4 | None = None
    data_testid: str | None = Field(None, alias='data-testid')
    padding: Padding | None = None
    mobile_options: MobileOptions | None = Field(None, alias='mobileOptions')
    tablet_options: TabletOptions | None = Field(None, alias='tabletOptions')
    desktop_options: DesktopOptions | None = Field(None, alias='desktopOptions')
    metrics_data: MetricsData4 | None = Field(None, alias='metricsData')
    html: str | None = None
    css: str | None = None
    js: str | None = None
    class_name: str | None = Field(None, alias='className')
    genre: list[str] | None = None
    preconnect_links: list[PreconnectLink] | None = Field(None, alias='preconnectLinks')
    priority_meta_tags: list[PriorityMetaTag] | None = Field(None, alias='priorityMetaTags')
    meta_tags: list[MetaTag] | None = Field(None, alias='metaTags')
    link_tags: list[LinkTag] | None = Field(None, alias='linkTags')
    ld_json: LdJson | None = Field(None, alias='ldJSON')
    debug_meta_tags: list[DebugMetaTag] | None = Field(None, alias='debugMetaTags')
    runtime_ms: int | None = Field(None, alias='runtimeMs')
    custom_field: str | None = Field(None, alias='customField')

class DefaultImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class Child11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage10 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage10 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage10 | None = Field(None, alias='smallImage')
    medium_image: MediumImage10 | None = Field(None, alias='mediumImage')
    large_image: LargeImage10 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage10 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage10 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')

class LeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[Child11] | None = None
    href: str | None = None
    title: str | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')

class RightItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    class_name: str | None = Field(None, alias='className')
    href: str | None = None
    size: str | None = None
    title: str | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')
    common_href: str | None = Field(None, alias='commonHref')

class StaticContainer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    left: list[LeftItem] | None = None
    right: list[RightItem] | None = None
    center: list[Any] | None = None

class PreContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    is_sticky: bool | None = Field(None, alias='isSticky')
    is_overlap: bool | None = Field(None, alias='isOverlap')
    static_container: StaticContainer | None = Field(None, alias='staticContainer')
    is_hidden_at_top: bool | None = Field(None, alias='isHiddenAtTop')
    sticky_background_override: str | None = Field(None, alias='stickyBackgroundOverride')

class Headline(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: str | None = None
    as_: str | None = Field(None, alias='as')
    class_name: str | None = Field(None, alias='className')

class Child15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    html_key: str | None = Field(None, alias='htmlKey')
    copy_: str | None = Field(None, alias='copy')
    href: str | None = None
    auto_localize_url: bool | None = Field(None, alias='autoLocalizeUrl')
    target: str | None = None
    rel: list[Any] | None = None
    class_name: str | None = Field(None, alias='className')

class Child14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    title: str | None = None
    direction: str | None = None
    children: list[Child15] | None = None
    mobile_alignment: str | None = Field(None, alias='mobileAlignment')
    tablet_alignment: str | None = Field(None, alias='tabletAlignment')
    desktop_alignment: str | None = Field(None, alias='desktopAlignment')
    html_key: str | None = Field(None, alias='htmlKey')
    icon: str | None = None
    copy_: str | None = Field(None, alias='copy')
    href: str | None = None
    target: str | None = None

class DefaultImage11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')

class Child13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    html_key: str | None = Field(None, alias='htmlKey')
    label: str | None = None
    mobile_collapse: bool | None = Field(None, alias='mobileCollapse')
    headline: Headline | None = None
    children: str | list[Child14] | None = None
    direction: str | None = None
    title: str | None = None
    mobile_alignment: str | None = Field(None, alias='mobileAlignment')
    tablet_alignment: str | None = Field(None, alias='tabletAlignment')
    desktop_alignment: str | None = Field(None, alias='desktopAlignment')
    alt: str | None = None
    default_image: DefaultImage11 | None = Field(None, alias='defaultImage')
    alt_text: str | None = Field(None, alias='altText')
    as_: str | None = Field(None, alias='as')
    class_name: str | None = Field(None, alias='className')
    copy_: str | None = Field(None, alias='copy')
    show_year: bool | None = Field(None, alias='showYear')

class Child12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    title: str | None = None
    direction: str | None = None
    children: list[Child13] | None = None
    mobile_alignment: str | None = Field(None, alias='mobileAlignment')
    tablet_alignment: str | None = Field(None, alias='tabletAlignment')
    desktop_alignment: str | None = Field(None, alias='desktopAlignment')

class Block(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child12] | None = None

class Data15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    title: str | None = None
    blocks: list[Block] | None = None
    light_mode: bool | None = Field(None, alias='lightMode')
    class_name: str | None = Field(None, alias='className')
    field_hash: str | None = Field(None, alias='_hash')
    field_created_at: AwareDatetime | None = Field(None, alias='_createdAt')

class Glimpse5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_key: str | None = Field(None, alias='containerKey')
    container_type: str | None = Field(None, alias='containerType')
    vertical_position: int | None = Field(None, alias='verticalPosition')
    container_style: str | None = Field(None, alias='containerStyle')

class MetricsData5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse5 | None = None

class PostContentItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    data: Data15 | None = None
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    locale: str | None = None
    lang_selector_languages: Any | None = Field(None, alias='langSelectorLanguages')
    region_groupings: Any | None = Field(None, alias='regionGroupings')
    metrics_data: MetricsData5 | None = Field(None, alias='metricsData')

class Data16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    class_name: str | None = Field(None, alias='className')

class Mark12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    data: Data16 | None = None

class Data17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    class_name: str | None = Field(None, alias='className')
    href: str | None = None
    target_blank: bool | None = Field(None, alias='targetBlank')
    title: str | None = None
    type: str | None = None

class ContentItem25(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    value: str | None = None
    marks: list[Mark12] | None = None
    content: list[Any] | None = None
    data: Data17 | None = None

class ContentItem24(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem25] | None = None

class RichText12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    content: list[ContentItem24] | None = None

class DefaultImage12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class Style5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    color: str | None = None

class ModalContentItem1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText12 | None = Field(None, alias='richText')
    alt: str | None = None
    default_image: DefaultImage12 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage10 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage10 | None = Field(None, alias='smallImage')
    medium_image: MediumImage10 | None = Field(None, alias='mediumImage')
    large_image: LargeImage10 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage10 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage10 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[str] | None = None
    copy_: str | None = Field(None, alias='copy')
    common_href: str | None = Field(None, alias='commonHref')
    href: str | None = None
    size: str | None = None
    title: str | None = None
    style: Style5 | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')
    css: str | None = None

class Style6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    text_align: str | None = Field(None, alias='textAlign')

class Payload4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    container_style: str | None = Field(None, alias='containerStyle')
    container_type: str | None = Field(None, alias='containerType')
    elements: list[Any] | None = None
    elements_per_width: int | None = Field(None, alias='elementsPerWidth')
    horizontal_position: int | None = Field(None, alias='horizontalPosition')
    vertical_position: int | None = Field(None, alias='verticalPosition')
    container_key: str | None = Field(None, alias='containerKey')

class Glimpse6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    event_urn: str | None = Field(None, alias='eventUrn')
    payload: Payload4 | None = None

class MetricsData6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse6 | None = None

class Modal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    is_exit_intent: bool | None = Field(None, alias='isExitIntent')
    should_open_on_page_load: bool | None = Field(None, alias='shouldOpenOnPageLoad')
    text_alignment: str | None = Field(None, alias='textAlignment')
    modal_content: list[ModalContentItem1] | None = Field(None, alias='modalContent')
    style: Style6 | None = None
    id: str | None = None
    metrics_data: MetricsData6 | None = Field(None, alias='metricsData')

class Url(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    key: str | None = None
    url: str | None = None
    analytics_name: str | None = None

class CannonballLinkManager(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    urls: list[Url] | None = None

class ImageCardModalConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signup_url: str | None = Field(None, alias='signupUrl')
    login_url: str | None = Field(None, alias='loginUrl')
    signup_text: str | None = Field(None, alias='signupText')
    login_text: str | None = Field(None, alias='loginText')
    modal_copy: str | None = Field(None, alias='modalCopy')

class Overrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cannonball_link_manager: CannonballLinkManager | None = Field(None, alias='cannonballLinkManager')
    image_card_modal_config: ImageCardModalConfig | None = Field(None, alias='imageCardModalConfig')

class StitchDocument(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    main_content: list[MainContentItem] | None = Field(None, alias='mainContent')
    head_content: list[Any] | None = Field(None, alias='headContent')
    pre_content: list[list[PreContentItem]] | None = Field(None, alias='preContent')
    post_content: list[PostContentItem] | None = Field(None, alias='postContent')
    modals: list[Modal] | None = None
    overrides: Overrides | None = None

class FeatureFlags(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    block_datadog_rum: bool | None = Field(None, alias='blockDatadogRum')
    enable_identity_sdkv5: bool | None = Field(None, alias='enableIdentitySDKV5')
    enable_always_reload_on_consent_change: bool | None = Field(None, alias='enableAlwaysReloadOnConsentChange')

class Signup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    url: str | None = None

class ToastCtaProps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signup: Signup | None = None

class PageProps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available_locales: list[str] | None = Field(None, alias='availableLocales')
    stitch_document: StitchDocument | None = Field(None, alias='stitchDocument')
    has_content: bool | None = Field(None, alias='hasContent')
    page_id: str | None = Field(None, alias='pageId')
    language: str | None = None
    region: str | None = None
    pathname: str | None = None
    location: str | None = None
    disable_redirect: bool | None = Field(None, alias='disableRedirect')
    feature_flags: FeatureFlags | None = Field(None, alias='featureFlags')
    toast_cta_props: ToastCtaProps | None = Field(None, alias='toastCtaProps')
    rtl_supported_locales: list[str] | None = Field(None, alias='rtlSupportedLocales')

class Props(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_props: PageProps | None = Field(None, alias='pageProps')
    field__n_ssp: bool | None = Field(None, alias='__N_SSP')

class Query(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    slug: str | None = None
    season: UUID | None = None

class EntityModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    props: Props | None = None
    page: str | None = None
    query: Query | None = None
    build_id: str | None = Field(None, alias='buildId')
    asset_prefix: str | None = Field(None, alias='assetPrefix')
    is_fallback: bool | None = Field(None, alias='isFallback')
    is_experimental_compile: bool | None = Field(None, alias='isExperimentalCompile')
    gssp: bool | None = None
    script_loader: list[Any] | None = Field(None, alias='scriptLoader')
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
