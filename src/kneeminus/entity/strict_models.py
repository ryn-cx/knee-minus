from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import ConfigDict
from pydantic import AwareDatetime, BaseModel, Field
from uuid import UUID
from typing import Any

class DefaultImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class BackgroundImage(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class Alignments(BaseModel):
    model_config = ConfigDict(defer_build=True)
    text: str
    vertical: str

class FooterItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class DefaultImage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MaxWidths(BaseModel):
    model_config = ConfigDict(defer_build=True)
    sm_max_width: int = Field(..., alias='smMaxWidth')
    md_max_width: int = Field(..., alias='mdMaxWidth')
    lg_max_width: int = Field(..., alias='lgMaxWidth')

class Data(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str | None = Field(None, alias='className')
    color: str | None = None

class Mark(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data | None = None

class ContentItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark]

class ContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem1]

class RichText(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem]

class Child1(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class ColSize(BaseModel):
    model_config = ConfigDict(defer_build=True)
    desktop: int
    tablet: int
    mobile: int

class Child(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alignments: Alignments
    footer: list[FooterItem]
    children: list[Child1]
    col_size: ColSize = Field(..., alias='colSize')
    gap: str
    grid_item_index: int = Field(..., alias='gridItemIndex')

class Offers(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_id: str = Field(..., alias='_id')
    field_type: str = Field(..., alias='_type')
    alignment: str
    children: list[Child]
    col_size: ColSize = Field(..., alias='colSize')
    gap: str

class DefaultImage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage2 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage2 = Field(..., alias='xsmallImage')
    small_image: SmallImage2 = Field(..., alias='smallImage')
    medium_image: MediumImage2 = Field(..., alias='mediumImage')
    large_image: LargeImage2 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage2 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage2 = Field(..., alias='xxlargeImage')
    loading: str

class Payload(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class Glimpse(BaseModel):
    model_config = ConfigDict(defer_build=True)
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload

class MetricsData(BaseModel):
    model_config = ConfigDict(defer_build=True)
    glimpse: Glimpse

class BadgeRowItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    is_badge: bool = Field(..., alias='isBadge')

class Data1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str = Field(..., alias='className')

class Mark1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data1

class Data2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: str | list[str]
    copy_: str | None = Field(None, alias='copy')
    class_name: str | None = Field(None, alias='className')
    href: str | None = None
    title: str | None = None
    type: str | None = None
    as_: str | None = Field(None, alias='as')

class ContentItem3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    marks: list[Mark1] | None = None
    value: str | None = None
    content: list[None] | None = None
    data: Data2 | None = None

class ContentItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem3]

class RichText1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem2]

class Child6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText1 = Field(..., alias='richText')

class Child5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child6]
    size: str

class Footer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_id: str = Field(..., alias='_id')
    field_type: str = Field(..., alias='_type')
    children: list[Child5]
    text_alignment: str = Field(..., alias='textAlignment')

class DefaultImage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Data3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str = Field(..., alias='className')

class Mark2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data3 | None = None

class ContentItem5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark2]

class ContentItem4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem5]

class RichText2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem4]

class CellContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
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
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    class_name: str = Field(..., alias='className')
    cell_content: list[CellContentItem] | None = Field(None, alias='cellContent')

class Style(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str

class CellContentItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: str | list[str]
    copy_: str | None = Field(None, alias='copy')
    common_href: str | None = Field(None, alias='commonHref')
    size: str
    title: str | None = None
    style: Style | None = None
    type: str | None = None
    element_id: str | None = Field(None, alias='elementId')
    data_test_id: str | None = Field(None, alias='dataTestId')
    href: str | None = None
    target_blank: bool | None = Field(None, alias='targetBlank')
    format: list[str] | None = None

class HeaderFooter(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    cell_content: list[CellContentItem1] | None = Field(None, alias='cellContent')

class HeaderRow1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header_bodies: list[HeaderBody] = Field(..., alias='headerBodies')
    header_footers: list[HeaderFooter] = Field(..., alias='headerFooters')

class HeaderRow(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    header_row: HeaderRow1 = Field(..., alias='headerRow')
    column_count: int = Field(..., alias='columnCount')
    max_width: str = Field(..., alias='maxWidth')

class Mark3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data3 | None = None

class Data5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    as_: str = Field(..., alias='as')
    children: str
    class_name: str = Field(..., alias='className')

class ContentItem7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str | None = None
    marks: list[Mark3]
    content: list[None] | None = None
    data: Data5 | None = None

class ContentItem6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem7]

class RichText3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem6]

class Child7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText3 = Field(..., alias='richText')

class Data6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str = Field(..., alias='className')

class Mark4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data6

class ContentItem9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark4]

class ContentItem8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem9]

class RichText4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem8]

class CellContentItem2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText4 | None = Field(None, alias='richText')
    children: str | None = None
    size: str | None = None

class RowDatum(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child7] | None = None
    cell_content: list[CellContentItem2] | None = Field(None, alias='cellContent')
    column_id: str | None = Field(None, alias='columnId')
    is_selected: bool | None = Field(None, alias='isSelected')

class Row(BaseModel):
    model_config = ConfigDict(defer_build=True)
    row_data: list[RowDatum] = Field(..., alias='rowData')
    id: str

class BadgeRowItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    is_badge: bool = Field(..., alias='isBadge')

class Mark5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data6 | None = None

class Data8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: str | list[str]
    copy_: str | None = Field(None, alias='copy')
    class_name: str = Field(..., alias='className')
    href: str | None = None
    title: str | None = None
    type: str | None = None
    as_: str | None = Field(None, alias='as')

class ContentItem11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    marks: list[Mark5] | None = None
    value: str | None = None
    content: list[None] | None = None
    data: Data8 | None = None

class ContentItem10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem11]

class RichText5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem10]

class Child9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText5 = Field(..., alias='richText')

class Child8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child9]
    size: str

class Footer1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_id: str = Field(..., alias='_id')
    field_type: str = Field(..., alias='_type')
    children: list[Child8]
    text_alignment: str = Field(..., alias='textAlignment')

class Data9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str = Field(..., alias='className')

class Mark6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data9 | None = None

class ContentItem13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str | None = None
    marks: list[Mark6] | None = None
    content: list[None] | None = None

class ContentItem12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem13]

class RichText6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem12]

class CellContentItem3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText6 | None = Field(None, alias='richText')
    size: str | None = None

class HeaderBody1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    cell_content: list[CellContentItem3] | None = Field(..., alias='cellContent')
    class_name: str = Field(..., alias='className')

class Mark7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data9

class ContentItem15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark7]

class ContentItem14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem15]

class RichText7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem14]

class Style1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    background: str
    color: str

class CellContentItem4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
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
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    cell_content: list[CellContentItem4] = Field(..., alias='cellContent')

class HeaderRow3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    header_bodies: list[HeaderBody1] = Field(..., alias='headerBodies')
    header_footers: list[HeaderFooter1] = Field(..., alias='headerFooters')

class HeaderRow2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    id: str
    header_row: HeaderRow3 = Field(..., alias='headerRow')
    column_count: int = Field(..., alias='columnCount')
    max_width: str = Field(..., alias='maxWidth')

class Mark8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data9 | None = None

class ContentItem17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark8]

class ContentItem16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem17]

class RichText8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem16]

class Child10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText8 = Field(..., alias='richText')

class Mark9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data9

class ContentItem19(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark9]

class ContentItem18(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem19]

class RichText9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem18]

class CellContentItem5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText9 = Field(..., alias='richText')

class RowDatum1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child10] | None = None
    cell_content: list[CellContentItem5] | None = Field(None, alias='cellContent')
    column_id: str | None = Field(None, alias='columnId')
    is_selected: bool | None = Field(None, alias='isSelected')

class Row1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    row_data: list[RowDatum1] = Field(..., alias='rowData')
    id: str

class Subchart(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    badge_row: list[BadgeRowItem1] = Field(..., alias='badgeRow')
    column_count: int = Field(..., alias='columnCount')
    footer: Footer1
    header_row: HeaderRow2 = Field(..., alias='headerRow')
    highlighted_column_ids: list[None] = Field(..., alias='highlightedColumnIds')
    is_expandable: bool = Field(..., alias='isExpandable')
    is_header_row_with_badge: bool = Field(..., alias='isHeaderRowWithBadge')
    max_width: str = Field(..., alias='maxWidth')
    rows: list[Row1]
    should_expand_on_load: bool = Field(..., alias='shouldExpandOnLoad')

class Child4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: UUID | str = Field(..., alias='_id', union_mode='left_to_right')
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
    highlighted_column_ids: list[None] | None = Field(None, alias='highlightedColumnIds')
    is_expandable: bool | None = Field(None, alias='isExpandable')
    is_header_row_with_badge: bool | None = Field(None, alias='isHeaderRowWithBadge')
    max_width: str | None = Field(None, alias='maxWidth')
    rows: list[Row] | None = None
    subcharts: list[Subchart] | None = None

class Data13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str | None = Field(None, alias='className')
    color: str | None = None

class Mark10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data13

class ContentItem21(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark10]

class ContentItem20(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem21]

class RichText10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem20]

class Child3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: UUID | str = Field(..., alias='_id', union_mode='left_to_right')
    children: list[Child4] | None = None
    rich_text: RichText10 | None = Field(None, alias='richText')
    tab_id: str | None = Field(None, alias='tabId')
    tab_name: str | None = Field(None, alias='tabName')

class Title(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    as_: str = Field(..., alias='as')
    children: str
    class_name: str = Field(..., alias='className')
    size: str

class CapsuleProps(BaseModel):
    model_config = ConfigDict(defer_build=True)
    button_background: str = Field(..., alias='buttonBackground')
    selected_text_color: str = Field(..., alias='selectedTextColor')

class Child2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child3]
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
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class DetailIcon(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class DefaultImage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class SmallImage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class MediumImage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class LargeImage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class TitleVisual(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class DefaultImage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Image(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage6 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage6 = Field(..., alias='xsmallImage')
    small_image: SmallImage6 = Field(..., alias='smallImage')
    medium_image: MediumImage6 = Field(..., alias='mediumImage')
    large_image: LargeImage6 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage6 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage6 = Field(..., alias='xxlargeImage')

class Rating(BaseModel):
    model_config = ConfigDict(defer_build=True)
    title: str
    image: Image
    advisories: list[None]

class Item(BaseModel):
    model_config = ConfigDict(defer_build=True)
    display_text: str = Field(..., alias='displayText')

class Credit(BaseModel):
    model_config = ConfigDict(defer_build=True)
    heading: str
    items: list[Item]

class Labels(BaseModel):
    model_config = ConfigDict(defer_build=True)
    details: str
    genres: str
    release: str
    runtime: str

class DefaultImage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage7(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants1(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class Metadata(BaseModel):
    model_config = ConfigDict(defer_build=True)
    summary: str

class Glimpse1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload

class MetricsData1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    glimpse: Glimpse1

class Episode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    title: str
    image_variants: ImageVariants1 = Field(..., alias='imageVariants')
    aspect_ratio: float = Field(..., alias='aspectRatio')
    loading: str
    metadata: Metadata
    collection_group_key: str = Field(..., alias='collectionGroupKey')
    metrics_data: MetricsData1 = Field(..., alias='metricsData')

class Season(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: UUID
    name: str

class DefaultImage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage8(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Data14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str = Field(..., alias='className')

class Mark11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data14 | None = None

class ContentItem23(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str
    marks: list[Mark11]

class ContentItem22(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem23]

class RichText11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem22]

class Style2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str

class ModalContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
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
    model_config = ConfigDict(defer_build=True)
    text_align: str = Field(..., alias='textAlign')

class Payload2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_style: str = Field(..., alias='containerStyle')
    container_type: str = Field(..., alias='containerType')
    elements: list[None]
    elements_per_width: int = Field(..., alias='elementsPerWidth')
    horizontal_position: int = Field(..., alias='horizontalPosition')
    vertical_position: int = Field(..., alias='verticalPosition')
    container_key: str = Field(..., alias='containerKey')

class Glimpse2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload2

class MetricsData2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    glimpse: Glimpse2

class EpisodeSelectModal(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    is_exit_intent: bool = Field(..., alias='isExitIntent')
    should_open_on_page_load: bool = Field(..., alias='shouldOpenOnPageLoad')
    text_alignment: str = Field(..., alias='textAlignment')
    modal_content: list[ModalContentItem] = Field(..., alias='modalContent')
    style: Style3
    id: str
    metrics_data: MetricsData2 = Field(..., alias='metricsData')

class DefaultImage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage9(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants2(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage9 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage9 = Field(..., alias='xsmallImage')
    small_image: SmallImage9 = Field(..., alias='smallImage')
    medium_image: MediumImage9 = Field(..., alias='mediumImage')
    large_image: LargeImage9 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage9 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage9 = Field(..., alias='xxlargeImage')
    loading: str

class Payload3(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class Glimpse3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload3

class MetricsData3(BaseModel):
    model_config = ConfigDict(defer_build=True)
    glimpse: Glimpse3

class Episode1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    title: str
    image_variants: ImageVariants2 = Field(..., alias='imageVariants')
    aspect_ratio: float = Field(..., alias='aspectRatio')
    loading: str
    metadata: Metadata
    metrics_data: MetricsData3 = Field(..., alias='metricsData')

class SeoSeason(BaseModel):
    model_config = ConfigDict(defer_build=True)
    season_id: UUID = Field(..., alias='seasonId')
    season_name: str = Field(..., alias='seasonName')
    episodes: list[Episode1]

class Style4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    background: str

class Padding(BaseModel):
    model_config = ConfigDict(defer_build=True)
    top: str
    bottom: str | None = None

class MobileOptions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    full_width: bool | None = Field(None, alias='fullWidth')
    is_hidden: bool | None = Field(None, alias='isHidden')

class TabletOptions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    full_width: bool | None = Field(None, alias='fullWidth')
    is_hidden: bool | None = Field(None, alias='isHidden')

class DesktopOptions(BaseModel):
    model_config = ConfigDict(defer_build=True)
    full_width: bool = Field(..., alias='fullWidth')

class Glimpse4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_key: str = Field(..., alias='containerKey')
    container_type: str = Field(..., alias='containerType')
    container_style: str = Field(..., alias='containerStyle')
    vertical_position: int = Field(..., alias='verticalPosition')

class MetricsData4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    glimpse: Glimpse4

class PreconnectLink(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rel: str
    href: str
    cross_origin: str = Field(..., alias='crossOrigin')

class PriorityMetaTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    http_equiv: str | None = Field(None, alias='httpEquiv')
    content: str
    name: str | None = None

class MetaTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    item_prop: str | None = Field(None, alias='itemProp')
    content: str
    property: str | None = None
    name: str | None = None

class LinkTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    rel: str
    href: str

class EpisodeItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    name: str
    episode_number: int = Field(..., alias='episodeNumber')

class ContainsSeasonItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    name: str
    season_number: int = Field(..., alias='seasonNumber')
    episode: list[EpisodeItem]

class Item1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    field_id: str = Field(..., alias='@id')
    url: str
    name: str

class ItemListElementItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='@type')
    position: int
    item: Item1

class FieldGraphItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
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

class LdJson(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_context: str = Field(..., alias='@context')
    field_graph: list[FieldGraphItem] = Field(..., alias='@graph')

class DebugMetaTag(BaseModel):
    model_config = ConfigDict(defer_build=True)
    name: str
    content: str

class MainContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str | None = Field(None, alias='_id')
    background_image: BackgroundImage | None = Field(None, alias='backgroundImage')
    offers: Offers | None = None
    children: list[Child2] | None = None
    detail_icons: list[DetailIcon] | None = Field(None, alias='detailIcons')
    release_year: str | None = Field(None, alias='releaseYear')
    seasons_available: str | None = Field(None, alias='seasonsAvailable')
    genres: list[str] | None = None
    locale: str | None = None
    promotion: None = Field(None)
    promotion_sub_label: None = Field(None, alias='promotionSubLabel')
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
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage10(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Child11(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage10 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage10 = Field(..., alias='xsmallImage')
    small_image: SmallImage10 = Field(..., alias='smallImage')
    medium_image: MediumImage10 = Field(..., alias='mediumImage')
    large_image: LargeImage10 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage10 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage10 = Field(..., alias='xxlargeImage')
    max_widths: MaxWidths = Field(..., alias='maxWidths')

class LeftItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    action_key: str = Field(..., alias='actionKey')
    children: list[Child11]
    href: str
    title: str
    type: str
    element_id: str = Field(..., alias='elementId')
    data_test_id: str = Field(..., alias='dataTestId')

class RightItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    action_key: str = Field(..., alias='actionKey')
    children: list[str]
    copy_: str = Field(..., alias='copy')
    class_name: str = Field(..., alias='className')
    href: str
    size: str
    title: str
    type: str
    element_id: str = Field(..., alias='elementId')
    data_test_id: str = Field(..., alias='dataTestId')
    common_href: str | None = Field(None, alias='commonHref')

class StaticContainer(BaseModel):
    model_config = ConfigDict(defer_build=True)
    left: list[LeftItem]
    right: list[RightItem]
    center: list[None]

class PreContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    is_sticky: bool = Field(..., alias='isSticky')
    is_overlap: bool = Field(..., alias='isOverlap')
    static_container: StaticContainer = Field(..., alias='staticContainer')
    is_hidden_at_top: bool | None = Field(None, alias='isHiddenAtTop')
    sticky_background_override: str | None = Field(None, alias='stickyBackgroundOverride')

class Headline(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: str
    as_: str = Field(..., alias='as')
    class_name: str | None = Field(None, alias='className')

class Child15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    html_key: str = Field(..., alias='htmlKey')
    copy_: str = Field(..., alias='copy')
    href: str
    auto_localize_url: bool | None = Field(None, alias='autoLocalizeUrl')
    target: str | None = None
    rel: list[None] | None = None
    class_name: str | None = Field(None, alias='className')

class Child14(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
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
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')

class Child13(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
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
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    title: str | None = None
    direction: str
    children: list[Child13]
    mobile_alignment: str | None = Field(None, alias='mobileAlignment')
    tablet_alignment: str | None = Field(None, alias='tabletAlignment')
    desktop_alignment: str | None = Field(None, alias='desktopAlignment')

class Block(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child12]

class Data15(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    title: str
    blocks: list[Block]
    light_mode: bool = Field(..., alias='lightMode')
    class_name: str = Field(..., alias='className')
    field_hash: str = Field(..., alias='_hash')
    field_created_at: AwareDatetime = Field(..., alias='_createdAt')

class Glimpse5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_key: str = Field(..., alias='containerKey')
    container_type: str = Field(..., alias='containerType')
    vertical_position: int = Field(..., alias='verticalPosition')
    container_style: str = Field(..., alias='containerStyle')

class MetricsData5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    glimpse: Glimpse5

class PostContentItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    data: Data15
    enable_cmp: bool = Field(..., alias='enableCMP')
    locale: str
    lang_selector_languages: None = Field(..., alias='langSelectorLanguages')
    region_groupings: None = Field(..., alias='regionGroupings')
    metrics_data: MetricsData5 = Field(..., alias='metricsData')

class Data16(BaseModel):
    model_config = ConfigDict(defer_build=True)
    class_name: str | None = Field(..., alias='className')

class Mark12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    data: Data16 | None = None

class Data17(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    action_key: str = Field(..., alias='actionKey')
    children: list[str]
    copy_: str = Field(..., alias='copy')
    class_name: str = Field(..., alias='className')
    href: str
    target_blank: bool | None = Field(None, alias='targetBlank')
    title: str
    type: str

class ContentItem25(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    value: str | None = None
    marks: list[Mark12] | None = None
    content: list[None] | None = None
    data: Data17 | None = None

class ContentItem24(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem25]

class RichText12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    type: str
    content: list[ContentItem24]

class DefaultImage12(BaseModel):
    model_config = ConfigDict(defer_build=True)
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Style5(BaseModel):
    model_config = ConfigDict(defer_build=True)
    color: str

class ModalContentItem1(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
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
    model_config = ConfigDict(defer_build=True)
    text_align: str = Field(..., alias='textAlign')

class Payload4(BaseModel):
    model_config = ConfigDict(defer_build=True)
    container_style: str = Field(..., alias='containerStyle')
    container_type: str = Field(..., alias='containerType')
    elements: list[None]
    elements_per_width: int = Field(..., alias='elementsPerWidth')
    horizontal_position: int = Field(..., alias='horizontalPosition')
    vertical_position: int = Field(..., alias='verticalPosition')
    container_key: str = Field(..., alias='containerKey')

class Glimpse6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload4

class MetricsData6(BaseModel):
    model_config = ConfigDict(defer_build=True)
    glimpse: Glimpse6

class Modal(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    is_exit_intent: bool = Field(..., alias='isExitIntent')
    should_open_on_page_load: bool = Field(..., alias='shouldOpenOnPageLoad')
    text_alignment: str = Field(..., alias='textAlignment')
    modal_content: list[ModalContentItem1] = Field(..., alias='modalContent')
    style: Style6
    id: str
    metrics_data: MetricsData6 = Field(..., alias='metricsData')

class Url(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_id: str = Field(..., alias='_id')
    key: str | None = None
    url: str
    analytics_name: str

class CannonballLinkManager(BaseModel):
    model_config = ConfigDict(defer_build=True)
    field_id: str = Field(..., alias='_id')
    urls: list[Url]

class ImageCardModalConfig(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signup_url: str = Field(..., alias='signupUrl')
    login_url: str = Field(..., alias='loginUrl')
    signup_text: str = Field(..., alias='signupText')
    login_text: str = Field(..., alias='loginText')
    modal_copy: str = Field(..., alias='modalCopy')

class Overrides(BaseModel):
    model_config = ConfigDict(defer_build=True)
    cannonball_link_manager: CannonballLinkManager = Field(..., alias='cannonballLinkManager')
    image_card_modal_config: ImageCardModalConfig = Field(..., alias='imageCardModalConfig')

class StitchDocument(BaseModel):
    model_config = ConfigDict(defer_build=True)
    main_content: list[MainContentItem] = Field(..., alias='mainContent')
    head_content: list[None] | None = Field(None, alias='headContent')
    pre_content: list[list[PreContentItem]] | None = Field(None, alias='preContent')
    post_content: list[PostContentItem] | None = Field(None, alias='postContent')
    modals: list[Modal] | None = None
    overrides: Overrides | None = None

class FeatureFlags(BaseModel):
    model_config = ConfigDict(defer_build=True)
    block_datadog_rum: bool = Field(..., alias='blockDatadogRum')
    enable_identity_sdkv5: bool = Field(..., alias='enableIdentitySDKV5')
    enable_always_reload_on_consent_change: bool = Field(..., alias='enableAlwaysReloadOnConsentChange')

class Signup(BaseModel):
    model_config = ConfigDict(defer_build=True)
    label: str
    url: str

class ToastCtaProps(BaseModel):
    model_config = ConfigDict(defer_build=True)
    signup: Signup

class PageProps(BaseModel):
    model_config = ConfigDict(defer_build=True)
    available_locales: list[str] = Field(..., alias='availableLocales')
    stitch_document: StitchDocument = Field(..., alias='stitchDocument')
    has_content: bool = Field(..., alias='hasContent')
    page_id: str = Field(..., alias='pageId')
    language: str
    region: str
    pathname: str
    location: str
    disable_redirect: bool = Field(..., alias='disableRedirect')
    feature_flags: FeatureFlags | None = Field(None, alias='featureFlags')
    toast_cta_props: ToastCtaProps | None = Field(None, alias='toastCtaProps')
    rtl_supported_locales: list[str] | None = Field(None, alias='rtlSupportedLocales')

class Props(BaseModel):
    model_config = ConfigDict(defer_build=True)
    page_props: PageProps = Field(..., alias='pageProps')
    field__n_ssp: bool = Field(..., alias='__N_SSP')

class Query(BaseModel):
    model_config = ConfigDict(defer_build=True)
    slug: str
    season: UUID | None = None

class EntityModel(BaseModel):
    model_config = ConfigDict(defer_build=True)
    props: Props
    page: str
    query: Query
    build_id: str = Field(..., alias='buildId')
    asset_prefix: str = Field(..., alias='assetPrefix')
    is_fallback: bool = Field(..., alias='isFallback')
    is_experimental_compile: bool = Field(..., alias='isExperimentalCompile')
    gssp: bool
    script_loader: list[None] = Field(..., alias='scriptLoader')
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
