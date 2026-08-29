from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, Field
from typing import Any
from uuid import UUID

class Application(BaseModel):
    age_gate_denied_heading: str
    age_gate_denied_body: str
    age_gate_prompt_body: str
    age_gate_prompt_error: str
    article_back_to_top: str
    article_byline: str
    article_copy_link: str
    article_copy_to_clipboard_error: str
    article_copy_to_clipboard_success: str
    article_email_link: str
    article_revised: str
    article_share_link: str
    article_tags: str
    btn_choose_plan: str
    btn_login: str
    btn_ok_continue: str
    filter_and_sort_filters_label: str
    filter_and_sort_no_results: str
    filter_and_sort_no_results_sub: str
    filter_and_sort_reset: str
    filter_and_sort_sort_by: str
    d23countdownclock_days: str
    d23countdownclock_hours: str
    d23countdownclock_minutes: str
    d23countdownclock_seconds: str
    next_episode_episode_subtitle: str
    pagination_next: str
    pagination_previous: str
    pagination_show_all: str
    runtime_hours: str
    runtime_minutes: str
    search_placeholder: str
    unauthdetail_modal_copy: str
    unauthdetail_signupcta: str
    unauthdetail_you_may_also_like: str

class Accessibility(BaseModel):
    badge_label_event_live_tts: str
    btn_banner_web_close_tts: str
    btn_flip_card_close: str
    btn_flip_card_open: str
    btn_go_to_item_tts: str
    btn_live_modal_web_close_tts: str
    btn_nav_toggle_tts: str
    comp_chart_cell_feature_included_tts: str
    comp_chart_cell_feature_not_included_tts: str
    comp_chart_compare_plan_tts: str
    filter_and_sort_reset: str
    formerror_zipcode_invalid: str
    formerror_zipcode_required: str
    formlabel_submit: str
    formlabel_zipcode: str
    gallery_navigation_tts: str
    hero_gallery_tts: str
    index_number_generic: str
    pagination_next_tts: str
    pause: str
    plan_builder_reset_message: str
    play: str
    select_option_tts: str
    dropdown_season_label: str
    select_add_on_custom: str
    select_add_on: str
    skiptocontent_tts: str
    toast_close: str
    video_controls_pause: str
    video_controls_play: str

class Ratings(BaseModel):
    image_rating_kijkwijzer_12: str
    image_rating_kijkwijzer_16: str
    image_rating_kijkwijzer_6: str
    image_rating_kijkwijzer_9: str
    image_rating_kijkwijzer_al: str
    image_rating_mpaa_g: str
    image_rating_mpaa_nc_17: str = Field(..., alias='image_rating_mpaa_nc-17')
    image_rating_mpaa_pg: str
    image_rating_mpaa_pg_13: str = Field(..., alias='image_rating_mpaa_pg-13')
    image_rating_mpaa_r: str
    image_rating_ncs_g: str
    image_rating_ncs_m: str
    image_rating_ncs_ma15: str
    image_rating_ncs_pg: str
    image_rating_oflc_g: str
    image_rating_oflc_m: str
    image_rating_oflc_pg: str
    image_rating_oflc_r15: str
    image_rating_oflc_r16: str
    image_rating_oflc_rp13: str
    image_rating_oflc_rp16: str
    image_rating_tvpg_tv_14: str = Field(..., alias='image_rating_tvpg_tv-14')
    image_rating_tvpg_tv_g: str = Field(..., alias='image_rating_tvpg_tv-g')
    image_rating_tvpg_tv_ma: str = Field(..., alias='image_rating_tvpg_tv-ma')
    image_rating_tvpg_tv_pg: str = Field(..., alias='image_rating_tvpg_tv-pg')
    image_rating_tvpg_tv_y: str = Field(..., alias='image_rating_tvpg_tv-y')
    image_rating_tvpg_tv_y7: str = Field(..., alias='image_rating_tvpg_tv-y7')

class UnifiedCommerceOnboarding(BaseModel):
    next_landing_button1: str
    next_landing_button2: str
    next_landing_header: str
    next_landing_subhead: str

class Seo(BaseModel):
    description_collection_brand: str
    title_collection_brand: str
    title_details_event: str
    title_details_movie: str
    title_details_series: str

class Dictionary(BaseModel):
    application: Application
    accessibility: Accessibility
    ratings: Ratings
    unified_commerce_onboarding: UnifiedCommerceOnboarding = Field(..., alias='unified-commerce-onboarding')
    seo: Seo

class FeatureFlags(BaseModel):
    block_datadog_rum: bool = Field(..., alias='blockDatadogRum')
    enable_identity_sdkv5: bool = Field(..., alias='enableIdentitySDKV5')
    enable_always_reload_on_consent_change: bool = Field(..., alias='enableAlwaysReloadOnConsentChange')

class IdentitySdkConfig(BaseModel):
    client_id: str = Field(..., alias='clientId')
    enabled: bool
    environment: str
    rollout_percentage: int = Field(..., alias='rolloutPercentage')
    script_url: str = Field(..., alias='scriptUrl')
    flag: str
    enable_identity_sdkv5: bool = Field(..., alias='enableIdentitySDKV5')

class DefaultImage(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MaxWidths(BaseModel):
    sm_max_width: int = Field(..., alias='smMaxWidth')
    md_max_width: int = Field(..., alias='mdMaxWidth')
    lg_max_width: int = Field(..., alias='lgMaxWidth')

class Child(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage = Field(..., alias='xsmallImage')
    small_image: SmallImage = Field(..., alias='smallImage')
    medium_image: MediumImage = Field(..., alias='mediumImage')
    large_image: LargeImage = Field(..., alias='largeImage')
    xlarge_image: XlargeImage = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage = Field(..., alias='xxlargeImage')
    max_widths: MaxWidths = Field(..., alias='maxWidths')

class LeftItem(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    action_key: str = Field(..., alias='actionKey')
    children: list[Child]
    href: str
    title: str
    type: str
    element_id: str = Field(..., alias='elementId')
    data_test_id: str = Field(..., alias='dataTestId')

class RightItem(BaseModel):
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
    left: list[LeftItem]
    right: list[RightItem]
    center: list[None]

class PreContentItem(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    is_sticky: bool = Field(..., alias='isSticky')
    is_overlap: bool = Field(..., alias='isOverlap')
    static_container: StaticContainer = Field(..., alias='staticContainer')
    is_hidden_at_top: bool | None = Field(None, alias='isHiddenAtTop')
    sticky_background_override: str | None = Field(None, alias='stickyBackgroundOverride')

class DefaultImage1(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage1(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage1(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage1(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage1(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage1(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage1(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class BackgroundImage(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage1 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage1 = Field(..., alias='xsmallImage')
    small_image: SmallImage1 = Field(..., alias='smallImage')
    medium_image: MediumImage1 = Field(..., alias='mediumImage')
    large_image: LargeImage1 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage1 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage1 = Field(..., alias='xxlargeImage')

class Alignments(BaseModel):
    text: str
    vertical: str

class FooterItem(BaseModel):
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

class DefaultImage2(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage2(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage2(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage2(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage2(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage2(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage2(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Data(BaseModel):
    class_name: str | None = Field(None, alias='className')
    color: str | None = None

class Mark(BaseModel):
    type: str
    data: Data | None = None

class ContentItem1(BaseModel):
    type: str
    value: str
    marks: list[Mark]

class ContentItem(BaseModel):
    type: str
    content: list[ContentItem1]

class RichText(BaseModel):
    type: str
    content: list[ContentItem]

class Child2(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    default_image: DefaultImage2 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage2 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage2 | None = Field(None, alias='smallImage')
    medium_image: MediumImage2 | None = Field(None, alias='mediumImage')
    large_image: LargeImage2 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage2 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage2 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    rich_text: RichText | None = Field(None, alias='richText')

class ColSize(BaseModel):
    desktop: int
    tablet: int
    mobile: int

class Child1(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alignments: Alignments
    footer: list[FooterItem]
    children: list[Child2]
    col_size: ColSize = Field(..., alias='colSize')
    gap: str
    grid_item_index: int = Field(..., alias='gridItemIndex')

class Offers(BaseModel):
    field_id: str = Field(..., alias='_id')
    field_type: str = Field(..., alias='_type')
    alignment: str
    children: list[Child1]
    col_size: ColSize = Field(..., alias='colSize')
    gap: str

class DefaultImage3(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage3(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage3(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage3(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage3(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage3(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage3(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants(BaseModel):
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
    loading: str

class Payload(BaseModel):
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
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload

class MetricsData(BaseModel):
    glimpse: Glimpse

class BadgeRowItem(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    is_badge: bool = Field(..., alias='isBadge')

class Data1(BaseModel):
    class_name: str = Field(..., alias='className')

class Mark1(BaseModel):
    type: str
    data: Data1

class Data2(BaseModel):
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
    type: str
    marks: list[Mark1] | None = None
    value: str | None = None
    content: list[None] | None = None
    data: Data2 | None = None

class ContentItem2(BaseModel):
    type: str
    content: list[ContentItem3]

class RichText1(BaseModel):
    type: str
    content: list[ContentItem2]

class Child7(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText1 = Field(..., alias='richText')

class Child6(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child7]
    size: str

class Footer(BaseModel):
    field_id: str = Field(..., alias='_id')
    field_type: str = Field(..., alias='_type')
    children: list[Child6]
    text_alignment: str = Field(..., alias='textAlignment')

class DefaultImage4(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage4(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage4(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage4(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage4(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage4(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage4(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Data3(BaseModel):
    class_name: str = Field(..., alias='className')

class Mark2(BaseModel):
    type: str
    data: Data3 | None = None

class ContentItem5(BaseModel):
    type: str
    value: str
    marks: list[Mark2]

class ContentItem4(BaseModel):
    type: str
    content: list[ContentItem5]

class RichText2(BaseModel):
    type: str
    content: list[ContentItem4]

class CellContentItem(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str | None = None
    default_image: DefaultImage4 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage4 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage4 | None = Field(None, alias='smallImage')
    medium_image: MediumImage4 | None = Field(None, alias='mediumImage')
    large_image: LargeImage4 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage4 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage4 | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')
    size: str | None = None
    rich_text: RichText2 | None = Field(None, alias='richText')

class HeaderBody(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    class_name: str = Field(..., alias='className')
    cell_content: list[CellContentItem] | None = Field(None, alias='cellContent')

class Style(BaseModel):
    color: str

class CellContentItem1(BaseModel):
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
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    cell_content: list[CellContentItem1] | None = Field(None, alias='cellContent')

class HeaderRow1(BaseModel):
    header_bodies: list[HeaderBody] = Field(..., alias='headerBodies')
    header_footers: list[HeaderFooter] = Field(..., alias='headerFooters')

class HeaderRow(BaseModel):
    field_type: str = Field(..., alias='_type')
    id: str
    header_row: HeaderRow1 = Field(..., alias='headerRow')
    column_count: int = Field(..., alias='columnCount')
    max_width: str = Field(..., alias='maxWidth')

class Mark3(BaseModel):
    type: str
    data: Data3 | None = None

class Data5(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    as_: str = Field(..., alias='as')
    children: str
    class_name: str = Field(..., alias='className')

class ContentItem7(BaseModel):
    type: str
    value: str | None = None
    marks: list[Mark3]
    content: list[None] | None = None
    data: Data5 | None = None

class ContentItem6(BaseModel):
    type: str
    content: list[ContentItem7]

class RichText3(BaseModel):
    type: str
    content: list[ContentItem6]

class Child8(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText3 = Field(..., alias='richText')

class Data6(BaseModel):
    class_name: str = Field(..., alias='className')

class Mark4(BaseModel):
    type: str
    data: Data6

class ContentItem9(BaseModel):
    type: str
    value: str
    marks: list[Mark4]

class ContentItem8(BaseModel):
    type: str
    content: list[ContentItem9]

class RichText4(BaseModel):
    type: str
    content: list[ContentItem8]

class CellContentItem2(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText4 | None = Field(None, alias='richText')
    children: str | None = None
    size: str | None = None

class RowDatum(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child8] | None = None
    cell_content: list[CellContentItem2] | None = Field(None, alias='cellContent')
    column_id: str | None = Field(None, alias='columnId')
    is_selected: bool | None = Field(None, alias='isSelected')

class Row(BaseModel):
    row_data: list[RowDatum] = Field(..., alias='rowData')
    id: str

class BadgeRowItem1(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    is_badge: bool = Field(..., alias='isBadge')

class Mark5(BaseModel):
    type: str
    data: Data6 | None = None

class Data8(BaseModel):
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
    type: str
    marks: list[Mark5] | None = None
    value: str | None = None
    content: list[None] | None = None
    data: Data8 | None = None

class ContentItem10(BaseModel):
    type: str
    content: list[ContentItem11]

class RichText5(BaseModel):
    type: str
    content: list[ContentItem10]

class Child10(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText5 = Field(..., alias='richText')

class Child9(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child10]
    size: str

class Footer1(BaseModel):
    field_id: str = Field(..., alias='_id')
    field_type: str = Field(..., alias='_type')
    children: list[Child9]
    text_alignment: str = Field(..., alias='textAlignment')

class Data9(BaseModel):
    class_name: str = Field(..., alias='className')

class Mark6(BaseModel):
    type: str
    data: Data9 | None = None

class ContentItem13(BaseModel):
    type: str
    value: str | None = None
    marks: list[Mark6] | None = None
    content: list[None] | None = None

class ContentItem12(BaseModel):
    type: str
    content: list[ContentItem13]

class RichText6(BaseModel):
    type: str
    content: list[ContentItem12]

class CellContentItem3(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText6 | None = Field(None, alias='richText')
    size: str | None = None

class HeaderBody1(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    cell_content: list[CellContentItem3] | None = Field(..., alias='cellContent')
    class_name: str = Field(..., alias='className')

class Mark7(BaseModel):
    type: str
    data: Data9

class ContentItem15(BaseModel):
    type: str
    value: str
    marks: list[Mark7]

class ContentItem14(BaseModel):
    type: str
    content: list[ContentItem15]

class RichText7(BaseModel):
    type: str
    content: list[ContentItem14]

class Style1(BaseModel):
    background: str
    color: str

class CellContentItem4(BaseModel):
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
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    column_id: str = Field(..., alias='columnId')
    is_highlighted: bool | None = Field(None, alias='isHighlighted')
    is_header: bool = Field(..., alias='isHeader')
    text_alignment: str | None = Field(None, alias='textAlignment')
    cell_content: list[CellContentItem4] = Field(..., alias='cellContent')

class HeaderRow3(BaseModel):
    header_bodies: list[HeaderBody1] = Field(..., alias='headerBodies')
    header_footers: list[HeaderFooter1] = Field(..., alias='headerFooters')

class HeaderRow2(BaseModel):
    field_type: str = Field(..., alias='_type')
    id: str
    header_row: HeaderRow3 = Field(..., alias='headerRow')
    column_count: int = Field(..., alias='columnCount')
    max_width: str = Field(..., alias='maxWidth')

class Mark8(BaseModel):
    type: str
    data: Data9 | None = None

class ContentItem17(BaseModel):
    type: str
    value: str
    marks: list[Mark8]

class ContentItem16(BaseModel):
    type: str
    content: list[ContentItem17]

class RichText8(BaseModel):
    type: str
    content: list[ContentItem16]

class Child11(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText8 = Field(..., alias='richText')

class Mark9(BaseModel):
    type: str
    data: Data9

class ContentItem19(BaseModel):
    type: str
    value: str
    marks: list[Mark9]

class ContentItem18(BaseModel):
    type: str
    content: list[ContentItem19]

class RichText9(BaseModel):
    type: str
    content: list[ContentItem18]

class CellContentItem5(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText9 = Field(..., alias='richText')

class RowDatum1(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child11] | None = None
    cell_content: list[CellContentItem5] | None = Field(None, alias='cellContent')
    column_id: str | None = Field(None, alias='columnId')
    is_selected: bool | None = Field(None, alias='isSelected')

class Row1(BaseModel):
    row_data: list[RowDatum1] = Field(..., alias='rowData')
    id: str

class Subchart(BaseModel):
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

class Child5(BaseModel):
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
    class_name: str | None = Field(None, alias='className')
    color: str | None = None

class Mark10(BaseModel):
    type: str
    data: Data13

class ContentItem21(BaseModel):
    type: str
    value: str
    marks: list[Mark10]

class ContentItem20(BaseModel):
    type: str
    content: list[ContentItem21]

class RichText10(BaseModel):
    type: str
    content: list[ContentItem20]

class Child4(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: UUID | str = Field(..., alias='_id', union_mode='left_to_right')
    children: list[Child5] | None = None
    rich_text: RichText10 | None = Field(None, alias='richText')
    tab_id: str | None = Field(None, alias='tabId')
    tab_name: str | None = Field(None, alias='tabName')

class Title(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    as_: str = Field(..., alias='as')
    children: str
    class_name: str = Field(..., alias='className')
    size: str

class CapsuleProps(BaseModel):
    button_background: str = Field(..., alias='buttonBackground')
    selected_text_color: str = Field(..., alias='selectedTextColor')

class Child3(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child4]
    title: Title | None = None
    disable_tile_click: bool | None = Field(None, alias='disableTileClick')
    container_info_block: str | None = Field(None, alias='containerInfoBlock')
    data_test_id: str | None = Field(None, alias='dataTestId')
    container_style: str | None = Field(None, alias='containerStyle')
    size: str | None = None
    initial_tab_id: str | None = Field(None, alias='initialTabId')
    capsule_props: CapsuleProps | None = Field(None, alias='capsuleProps')
    display_mode: str | None = Field(None, alias='displayMode')

class DefaultImage5(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage5(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage5(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage5(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage5(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage5(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage5(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class DetailIcon(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage5 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage5 = Field(..., alias='xsmallImage')
    small_image: SmallImage5 = Field(..., alias='smallImage')
    medium_image: MediumImage5 = Field(..., alias='mediumImage')
    large_image: LargeImage5 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage5 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage5 = Field(..., alias='xxlargeImage')

class DefaultImage6(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage6(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class SmallImage6(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class MediumImage6(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class LargeImage6(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage6(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage6(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: UUID = Field(..., alias='ripcutId')
    transform: str
    max: list[int]
    image_id: UUID = Field(..., alias='imageId')

class TitleVisual(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage6 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage6 = Field(..., alias='xsmallImage')
    small_image: SmallImage6 = Field(..., alias='smallImage')
    medium_image: MediumImage6 = Field(..., alias='mediumImage')
    large_image: LargeImage6 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage6 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage6 = Field(..., alias='xxlargeImage')

class DefaultImage7(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage7(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage7(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage7(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage7(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage7(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage7(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Image(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage7 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage7 = Field(..., alias='xsmallImage')
    small_image: SmallImage7 = Field(..., alias='smallImage')
    medium_image: MediumImage7 = Field(..., alias='mediumImage')
    large_image: LargeImage7 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage7 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage7 = Field(..., alias='xxlargeImage')

class Rating(BaseModel):
    title: str
    image: Image
    advisories: list[None]

class Item(BaseModel):
    display_text: str = Field(..., alias='displayText')

class Credit(BaseModel):
    heading: str
    items: list[Item]

class Labels(BaseModel):
    details: str
    genres: str
    release: str
    runtime: str

class DefaultImage8(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage8(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage8(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage8(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage8(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage8(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage8(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants1(BaseModel):
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

class Metadata(BaseModel):
    summary: str

class Glimpse1(BaseModel):
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload

class MetricsData1(BaseModel):
    glimpse: Glimpse1

class Episode(BaseModel):
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
    id: UUID
    name: str

class DefaultImage9(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage9(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage9(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage9(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage9(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage9(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage9(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Data14(BaseModel):
    class_name: str = Field(..., alias='className')

class Mark11(BaseModel):
    type: str
    data: Data14 | None = None

class ContentItem23(BaseModel):
    type: str
    value: str
    marks: list[Mark11]

class ContentItem22(BaseModel):
    type: str
    content: list[ContentItem23]

class RichText11(BaseModel):
    type: str
    content: list[ContentItem22]

class Style2(BaseModel):
    color: str

class ModalContentItem(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    alt: str | None = None
    default_image: DefaultImage9 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage9 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage9 | None = Field(None, alias='smallImage')
    medium_image: MediumImage9 | None = Field(None, alias='mediumImage')
    large_image: LargeImage9 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage9 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage9 | None = Field(None, alias='xxlargeImage')
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
    text_align: str = Field(..., alias='textAlign')

class Payload2(BaseModel):
    container_style: str = Field(..., alias='containerStyle')
    container_type: str = Field(..., alias='containerType')
    elements: list[None]
    elements_per_width: int = Field(..., alias='elementsPerWidth')
    horizontal_position: int = Field(..., alias='horizontalPosition')
    vertical_position: int = Field(..., alias='verticalPosition')
    container_key: str = Field(..., alias='containerKey')

class Glimpse2(BaseModel):
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload2

class MetricsData2(BaseModel):
    glimpse: Glimpse2

class EpisodeSelectModal(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    is_exit_intent: bool = Field(..., alias='isExitIntent')
    should_open_on_page_load: bool = Field(..., alias='shouldOpenOnPageLoad')
    text_alignment: str = Field(..., alias='textAlignment')
    modal_content: list[ModalContentItem] = Field(..., alias='modalContent')
    style: Style3
    id: str
    metrics_data: MetricsData2 = Field(..., alias='metricsData')

class DefaultImage10(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XsmallImage10(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class SmallImage10(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class MediumImage10(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class LargeImage10(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XlargeImage10(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class XxlargeImage10(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    ripcut_id: UUID = Field(..., alias='ripcutId')
    image_id: UUID = Field(..., alias='imageId')

class ImageVariants2(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    alt: str
    default_image: DefaultImage10 = Field(..., alias='defaultImage')
    xsmall_image: XsmallImage10 = Field(..., alias='xsmallImage')
    small_image: SmallImage10 = Field(..., alias='smallImage')
    medium_image: MediumImage10 = Field(..., alias='mediumImage')
    large_image: LargeImage10 = Field(..., alias='largeImage')
    xlarge_image: XlargeImage10 = Field(..., alias='xlargeImage')
    xxlarge_image: XxlargeImage10 = Field(..., alias='xxlargeImage')
    loading: str

class Payload3(BaseModel):
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
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload3

class MetricsData3(BaseModel):
    glimpse: Glimpse3

class Episode1(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: UUID = Field(..., alias='_id')
    title: str
    image_variants: ImageVariants2 = Field(..., alias='imageVariants')
    aspect_ratio: float = Field(..., alias='aspectRatio')
    loading: str
    metadata: Metadata
    metrics_data: MetricsData3 = Field(..., alias='metricsData')

class SeoSeason(BaseModel):
    season_id: UUID = Field(..., alias='seasonId')
    season_name: str = Field(..., alias='seasonName')
    episodes: list[Episode1]

class Style4(BaseModel):
    background: str

class Padding(BaseModel):
    top: str
    bottom: str | None = None

class MobileOptions(BaseModel):
    full_width: bool | None = Field(None, alias='fullWidth')
    is_hidden: bool | None = Field(None, alias='isHidden')

class TabletOptions(BaseModel):
    full_width: bool | None = Field(None, alias='fullWidth')
    is_hidden: bool | None = Field(None, alias='isHidden')

class DesktopOptions(BaseModel):
    full_width: bool = Field(..., alias='fullWidth')

class Glimpse4(BaseModel):
    container_key: str = Field(..., alias='containerKey')
    container_type: str = Field(..., alias='containerType')
    container_style: str = Field(..., alias='containerStyle')
    vertical_position: int = Field(..., alias='verticalPosition')

class MetricsData4(BaseModel):
    glimpse: Glimpse4

class PreconnectLink(BaseModel):
    rel: str
    href: str
    cross_origin: str = Field(..., alias='crossOrigin')

class PriorityMetaTag(BaseModel):
    http_equiv: str | None = Field(None, alias='httpEquiv')
    content: str
    name: str | None = None

class MetaTag(BaseModel):
    item_prop: str | None = Field(None, alias='itemProp')
    content: str
    property: str | None = None
    name: str | None = None

class LinkTag(BaseModel):
    rel: str
    href: str

class EpisodeItem(BaseModel):
    field_type: str = Field(..., alias='@type')
    name: str
    episode_number: int = Field(..., alias='episodeNumber')

class ContainsSeasonItem(BaseModel):
    field_type: str = Field(..., alias='@type')
    name: str
    season_number: int = Field(..., alias='seasonNumber')
    episode: list[EpisodeItem]

class Item1(BaseModel):
    field_type: str = Field(..., alias='@type')
    field_id: str = Field(..., alias='@id')
    url: str
    name: str

class ItemListElementItem(BaseModel):
    field_type: str = Field(..., alias='@type')
    position: int
    item: Item1

class FieldGraphItem(BaseModel):
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
    field_context: str = Field(..., alias='@context')
    field_graph: list[FieldGraphItem] = Field(..., alias='@graph')

class DebugMetaTag(BaseModel):
    name: str
    content: str

class MainContentItem(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str | None = Field(None, alias='_id')
    background_image: BackgroundImage | None = Field(None, alias='backgroundImage')
    offers: Offers | None = None
    children: list[Child3] | None = None
    detail_icons: list[DetailIcon] | None = Field(None, alias='detailIcons')
    release_year: str | None = Field(None, alias='releaseYear')
    seasons_available: str | None = Field(None, alias='seasonsAvailable')
    genres: list[str] | None = None
    locale: str | None = None
    promotion: None = None
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

class Headline(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: str
    as_: str = Field(..., alias='as')
    class_name: str | None = Field(None, alias='className')

class Child15(BaseModel):
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
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')

class Child13(BaseModel):
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
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    title: str | None = None
    direction: str
    children: list[Child13]
    mobile_alignment: str | None = Field(None, alias='mobileAlignment')
    tablet_alignment: str | None = Field(None, alias='tabletAlignment')
    desktop_alignment: str | None = Field(None, alias='desktopAlignment')

class Block(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    children: list[Child12]

class Data15(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    title: str
    blocks: list[Block]
    light_mode: bool = Field(..., alias='lightMode')
    class_name: str = Field(..., alias='className')
    field_hash: str = Field(..., alias='_hash')
    field_created_at: AwareDatetime = Field(..., alias='_createdAt')

class Glimpse5(BaseModel):
    container_key: str = Field(..., alias='containerKey')
    container_type: str = Field(..., alias='containerType')
    vertical_position: int = Field(..., alias='verticalPosition')
    container_style: str = Field(..., alias='containerStyle')

class MetricsData5(BaseModel):
    glimpse: Glimpse5

class PostContentItem(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    data: Data15
    enable_cmp: bool = Field(..., alias='enableCMP')
    locale: str
    lang_selector_languages: None = Field(..., alias='langSelectorLanguages')
    region_groupings: None = Field(..., alias='regionGroupings')
    metrics_data: MetricsData5 = Field(..., alias='metricsData')

class Data16(BaseModel):
    class_name: str | None = Field(..., alias='className')

class Mark12(BaseModel):
    type: str
    data: Data16 | None = None

class Data17(BaseModel):
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
    type: str
    value: str | None = None
    marks: list[Mark12] | None = None
    content: list[None] | None = None
    data: Data17 | None = None

class ContentItem24(BaseModel):
    type: str
    content: list[ContentItem25]

class RichText12(BaseModel):
    type: str
    content: list[ContentItem24]

class DefaultImage12(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XsmallImage11(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class SmallImage11(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class MediumImage11(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class LargeImage11(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XlargeImage11(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class XxlargeImage11(BaseModel):
    source: str
    content_type: str = Field(..., alias='contentType')
    width: int
    height: int
    ripcut_id: str = Field(..., alias='ripcutId')
    image_id: str = Field(..., alias='imageId')

class Style5(BaseModel):
    color: str

class ModalContentItem1(BaseModel):
    field_type: str = Field(..., alias='_type')
    field_id: str = Field(..., alias='_id')
    rich_text: RichText12 | None = Field(None, alias='richText')
    alt: str | None = None
    default_image: DefaultImage12 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage11 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage11 | None = Field(None, alias='smallImage')
    medium_image: MediumImage11 | None = Field(None, alias='mediumImage')
    large_image: LargeImage11 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage11 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage11 | None = Field(None, alias='xxlargeImage')
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
    text_align: str = Field(..., alias='textAlign')

class Payload4(BaseModel):
    container_style: str = Field(..., alias='containerStyle')
    container_type: str = Field(..., alias='containerType')
    elements: list[None]
    elements_per_width: int = Field(..., alias='elementsPerWidth')
    horizontal_position: int = Field(..., alias='horizontalPosition')
    vertical_position: int = Field(..., alias='verticalPosition')
    container_key: str = Field(..., alias='containerKey')

class Glimpse6(BaseModel):
    event_urn: str = Field(..., alias='eventUrn')
    payload: Payload4

class MetricsData6(BaseModel):
    glimpse: Glimpse6

class Modal(BaseModel):
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
    field_id: str = Field(..., alias='_id')
    key: str | None = None
    url: str
    analytics_name: str

class CannonballLinkManager(BaseModel):
    field_id: str = Field(..., alias='_id')
    urls: list[Url]

class ImageCardModalConfig(BaseModel):
    signup_url: str = Field(..., alias='signupUrl')
    login_url: str = Field(..., alias='loginUrl')
    signup_text: str = Field(..., alias='signupText')
    login_text: str = Field(..., alias='loginText')
    modal_copy: str = Field(..., alias='modalCopy')

class Overrides(BaseModel):
    cannonball_link_manager: CannonballLinkManager = Field(..., alias='cannonballLinkManager')
    image_card_modal_config: ImageCardModalConfig = Field(..., alias='imageCardModalConfig')

class StitchDocument(BaseModel):
    head_content: list[None] = Field(..., alias='headContent')
    pre_content: list[list[PreContentItem]] = Field(..., alias='preContent')
    main_content: list[MainContentItem] = Field(..., alias='mainContent')
    post_content: list[PostContentItem] = Field(..., alias='postContent')
    modals: list[Modal]
    overrides: Overrides

class Glimpse7(BaseModel):
    page_info_block: str = Field(..., alias='pageInfoBlock')

class MetricsData7(BaseModel):
    glimpse: Glimpse7

class Signup(BaseModel):
    label: str
    url: str

class ToastCtaProps(BaseModel):
    signup: Signup

class PageContentRedisHostname(BaseModel):
    eu_west_1: str = Field(..., alias='eu-west-1')
    us_east_1: str = Field(..., alias='us-east-1')
    us_west_2: str = Field(..., alias='us-west-2')

class AppConfig(BaseModel):
    adobe_launch_script_url: str = Field(..., alias='adobeLaunchScriptUrl')
    help_center_url: str = Field(..., alias='helpCenterUrl')
    name: str
    page_content_redis_hostname: PageContentRedisHostname = Field(..., alias='pageContentRedisHostname')

class DictionaryVersions(BaseModel):
    accessibility: str
    application: str
    commerce: str
    decorations: str
    identity: str
    iscp: str
    media: str
    off_device: str = Field(..., alias='off-device')
    paywall: str
    pcon: str
    promo: str
    ratings: str
    sdk_errors: str = Field(..., alias='sdk-errors')
    seo: str
    subscriptions: str
    unified_commerce: str = Field(..., alias='unified-commerce')
    unified_commerce_onboarding: str = Field(..., alias='unified-commerce-onboarding')
    unified_offers: str = Field(..., alias='unified-offers')
    welch: str

class Commerce(BaseModel):
    account: str
    base: str
    hulu_activation: None
    incoming_activation_success: None
    manage_subscription_help: str
    refresh_cookies: None
    logo_navigation_home_logged_in: str
    logo_navigation_home_logged_out: str
    onboarding: str
    home: str
    unified_account: str
    welcome_back: str
    plan_select: str
    disney_account_details: None
    disney_plan_switch_ledger: str
    disney_plan_switch: str
    disney_plan_selector: str
    disney_signup_preview: str
    disney_upsell_interstitial: None
    espn_account_details: None
    espn_plan_switch_ledger: str
    espn_plan_switch: str
    espn_plan_selector: str
    espn_signup_preview: str
    hulu_account_details: None
    hulu_plan_selector: None
    hulu_plan_switch: str
    hulu_plan_switch_ledger: str
    hulu_signup_preview: str
    login: str
    login_with_redirect: None
    hoth: None
    secure: None
    student_verification: None = Field(..., alias='studentVerification')
    home_service: None
    account_api: None
    waf: None
    update_credentials: str
    root_domain: str
    yokozuna: None

class Activate(BaseModel):
    wbd_max: str
    espn: None
    hulu: str
    raptor_us: str
    crave_ca: str
    foxone_us: None
    mlb_us: None
    nfl_us: str
    tving_kr: str
    epicgames_us: None

class Activation(BaseModel):
    hulu: str

class Application1(BaseModel):
    name: str
    id: str
    version: str

class Sdk(BaseModel):
    client_id: str = Field(..., alias='clientId')
    client_api_key: str = Field(..., alias='clientApiKey')
    environment: str
    debug_enabled: bool = Field(..., alias='debugEnabled')
    application: Application1
    identity_client_id: str = Field(..., alias='identityClientId')

class GoogleRecaptcha(BaseModel):
    site_key: str = Field(..., alias='siteKey')

class Primary(BaseModel):
    port: int
    compression_level: int = Field(..., alias='compressionLevel')
    default_ttl_seconds: int = Field(..., alias='defaultTtlSeconds')
    type: str

class External(BaseModel):
    type: str

class Internal(BaseModel):
    type: str

class CacheClients(BaseModel):
    primary: Primary
    external: External
    internal: Internal

class ExploreApiConfig(BaseModel):
    base: str
    version: str
    page_version: str = Field(..., alias='pageVersion')

class Path(BaseModel):
    commerce: Commerce
    activate: Activate
    activation: Activation
    content: str
    dictionary_url: str = Field(..., alias='dictionaryUrl')
    dictionary_url_internal: str = Field(..., alias='dictionaryUrlInternal')
    hulu: str
    ripcut: str
    ripcut_raw: str = Field(..., alias='ripcutRaw')
    sdk: Sdk
    google_recaptcha: GoogleRecaptcha = Field(..., alias='googleRecaptcha')
    static_recommendations_assets: list[None] = Field(..., alias='staticRecommendationsAssets')
    switch_setup_timeout_seconds: int = Field(..., alias='switchSetupTimeoutSeconds')
    orchestration_url: str = Field(..., alias='orchestrationUrl')
    identity_provider_service: str = Field(..., alias='identityProviderService')
    cache_clients: CacheClients
    access_token: str = Field(..., alias='accessToken')
    explore_api_config: ExploreApiConfig = Field(..., alias='exploreApiConfig')
    orchestration_b2b_api_uri: str = Field(..., alias='orchestrationB2bApiUri')

class Billing(BaseModel):
    gift_card_number_mask: str = Field(..., alias='giftCardNumberMask')
    gift_card_number_min_length: int = Field(..., alias='giftCardNumberMinLength')

class Commerce1(BaseModel):
    billing: Billing
    cypher_variable_error_paths_to_crash: list[str] = Field(..., alias='cypherVariableErrorPathsToCrash')
    enabled_analytics_tooling: list[str] = Field(..., alias='enabledAnalyticsTooling')
    hardcoded_queries: list[None] = Field(..., alias='hardcodedQueries')
    url_param_host_allowlist: list[None] = Field(..., alias='urlParamHostAllowlist')
    payment_methods: None = Field(..., alias='paymentMethods')
    ravelin: None

class Adobe(BaseModel):
    cross_domains: list[str] = Field(..., alias='crossDomains')
    rsid: str
    rsidname: str
    server: str
    secure_server: str = Field(..., alias='secureServer')
    visitor_namespace: str = Field(..., alias='visitorNamespace')
    visitor: str
    audience_manager_server: str = Field(..., alias='audienceManagerServer')
    disable_third_party_cookies: bool = Field(..., alias='disableThirdPartyCookies')
    site: str
    web_app_name: str = Field(..., alias='webAppName')

class Tealium(BaseModel):
    url: str

class Analytics(BaseModel):
    adobe: Adobe
    partner: str
    tealium: Tealium

class IdentitySdk(BaseModel):
    client_id: str = Field(..., alias='clientId')
    enabled: bool
    environment: str
    rollout_percentage: int = Field(..., alias='rolloutPercentage')

class Script(BaseModel):
    stub_sdk: str = Field(..., alias='stubSDK')
    guuid: UUID

class CategoryPurposes(BaseModel):
    c0001: UUID = Field(..., alias='C0001')
    c0002: UUID = Field(..., alias='C0002')
    c0004: UUID = Field(..., alias='C0004')

class Api(BaseModel):
    url: str
    tokens: list[str]
    purposes: list[str]
    category_purposes: CategoryPurposes = Field(..., alias='categoryPurposes')

class CategoryPurposes1(BaseModel):
    field_1: UUID = Field(..., alias='1')
    field_2: UUID = Field(..., alias='2')
    field_4: UUID = Field(..., alias='4')

class UnifiedConsentApi(BaseModel):
    url: str
    tokens: list[str]
    purposes: list[str]
    category_purposes: CategoryPurposes1 = Field(..., alias='categoryPurposes')

class ConsentGroups(BaseModel):
    necessary: str
    performance_and_analytics: str = Field(..., alias='performanceAndAnalytics')
    functional: str
    targeted_advertising: str = Field(..., alias='targetedAdvertising')
    social_media: str = Field(..., alias='socialMedia')

class OneTrust(BaseModel):
    script: Script
    api: Api
    unified_consent_api: UnifiedConsentApi = Field(..., alias='unifiedConsentApi')
    consent_groups: ConsentGroups = Field(..., alias='consentGroups')

class ArAr(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class CsCz(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class DaDk(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class DeDe(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class ElGr(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class En(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class EnGb(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class Es419(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class EsEs(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class FiFi(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class FrCa(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class FrFr(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class HeIl(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class HuHu(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class HrHr(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class IdId(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class ItIt(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class JaJp(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class KoKr(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class MsMy(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class NlNl(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class NoNo(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class PlPl(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class PtBr(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class PtPt(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class RoRo(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class SkSk(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class SvSe(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class ThTh(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class TrTr(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class ZhHans(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class ZhHant(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class ZhHk(BaseModel):
    dict_: str = Field(..., alias='dict')
    hreflang: str

class SupportedLangsMap(BaseModel):
    ar_ar: ArAr = Field(..., alias='ar-ar')
    cs_cz: CsCz = Field(..., alias='cs-cz')
    da_dk: DaDk = Field(..., alias='da-dk')
    de_de: DeDe = Field(..., alias='de-de')
    el_gr: ElGr = Field(..., alias='el-gr')
    en: En
    en_gb: EnGb = Field(..., alias='en-gb')
    es_419: Es419 = Field(..., alias='es-419')
    es_es: EsEs = Field(..., alias='es-es')
    fi_fi: FiFi = Field(..., alias='fi-fi')
    fr_ca: FrCa = Field(..., alias='fr-ca')
    fr_fr: FrFr = Field(..., alias='fr-fr')
    he_il: HeIl = Field(..., alias='he-il')
    hu_hu: HuHu = Field(..., alias='hu-hu')
    hr_hr: HrHr = Field(..., alias='hr-hr')
    id_id: IdId = Field(..., alias='id-id')
    it_it: ItIt = Field(..., alias='it-it')
    ja_jp: JaJp = Field(..., alias='ja-jp')
    ko_kr: KoKr = Field(..., alias='ko-kr')
    ms_my: MsMy = Field(..., alias='ms-my')
    nl_nl: NlNl = Field(..., alias='nl-nl')
    no_no: NoNo = Field(..., alias='no-no')
    pl_pl: PlPl = Field(..., alias='pl-pl')
    pt_br: PtBr = Field(..., alias='pt-br')
    pt_pt: PtPt = Field(..., alias='pt-pt')
    ro_ro: RoRo = Field(..., alias='ro-ro')
    sk_sk: SkSk = Field(..., alias='sk-sk')
    sv_se: SvSe = Field(..., alias='sv-se')
    th_th: ThTh = Field(..., alias='th-th')
    tr_tr: TrTr = Field(..., alias='tr-tr')
    zh_hans: ZhHans = Field(..., alias='zh-hans')
    zh_hant: ZhHant = Field(..., alias='zh-hant')
    zh_hk: ZhHk = Field(..., alias='zh-hk')

class AuthZ(BaseModel):
    client_id: str = Field(..., alias='clientId')
    authorization_url: str = Field(..., alias='authorizationUrl')

class Convergence(BaseModel):
    auth_z: AuthZ = Field(..., alias='authZ')
    enabled: bool

class RemoteAppConfig(BaseModel):
    bolt_partner_id: None = Field(..., alias='boltPartnerId')
    commerce: Commerce1
    analytics: Analytics
    dictionary_tenant: str = Field(..., alias='dictionaryTenant')
    globalization_service_version: str = Field(..., alias='globalizationServiceVersion')
    identity_sdk: IdentitySdk = Field(..., alias='identitySDK')
    one_id: None = Field(..., alias='oneId')
    one_trust: OneTrust = Field(..., alias='oneTrust')
    supported_langs_map: SupportedLangsMap = Field(..., alias='supportedLangsMap')
    convergence: Convergence

class Af(BaseModel):
    group: str

class Nu(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class ChangePayment(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class Purchase(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class UnAuth(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class DefaultProduct(BaseModel):
    nu: Nu = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class SpecialOfferProduct(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class Commerce2(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Au(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce2
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')
    marketing: Marketing

class Bd(BaseModel):
    group: str

class Bn(BaseModel):
    group: str

class Bt(BaseModel):
    group: str

class Bu(BaseModel):
    group: str

class Commerce3(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing1(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cc(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce3
    feature_config: FeatureConfig = Field(..., alias='featureConfig')
    marketing: Marketing1

class Commerce4(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ck(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce4
    feature_config: FeatureConfig = Field(..., alias='featureConfig')
    marketing: Marketing1

class Cn(BaseModel):
    group: str

class Fj(BaseModel):
    group: str

class DefaultProduct1(BaseModel):
    nu: Nu = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce5(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct1 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig2(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing3(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Hk(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce5
    feature_config: FeatureConfig2 = Field(..., alias='featureConfig')
    marketing: Marketing3

class Hm(BaseModel):
    group: str

class Id(BaseModel):
    group: str
    marketing: Marketing3

class In(BaseModel):
    group: str

class DefaultProduct2(BaseModel):
    nu: Nu = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce6(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct2 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Jp(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce6
    feature_config: FeatureConfig2 = Field(..., alias='featureConfig')
    marketing: Marketing3

class Kh(BaseModel):
    group: str

class Ki(BaseModel):
    group: str

class DefaultProduct3(BaseModel):
    nu: Nu = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce7(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    card_options_popover_enabled: bool = Field(..., alias='cardOptionsPopoverEnabled')
    default_product: DefaultProduct3 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    minimum_age_to_subscribe: int = Field(..., alias='minimumAgeToSubscribe')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig4(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')
    enable_age_verification: bool = Field(..., alias='enableAgeVerification')
    enable_cmp: bool = Field(..., alias='enableCMP')

class Kr(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce7
    feature_config: FeatureConfig4 = Field(..., alias='featureConfig')
    marketing: Marketing3

class La(BaseModel):
    group: str

class Lk(BaseModel):
    group: str

class Mm(BaseModel):
    group: str

class Mo(BaseModel):
    group: str

class Mv(BaseModel):
    group: str

class My(BaseModel):
    group: str
    marketing: Marketing3

class Commerce8(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig5(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing8(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Nf(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce8
    feature_config: FeatureConfig5 = Field(..., alias='featureConfig')
    marketing: Marketing8

class Np(BaseModel):
    group: str

class Nr(BaseModel):
    group: str

class Commerce9(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Nu4(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce9
    feature_config: FeatureConfig5 = Field(..., alias='featureConfig')
    marketing: Marketing8

class Nu5(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class DefaultProduct4(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce10(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct4 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing10(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Nz(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce10
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')
    marketing: Marketing10

class Pg(BaseModel):
    group: str

class Ph(BaseModel):
    group: str
    marketing: Marketing10

class Pk(BaseModel):
    group: str

class Sb(BaseModel):
    group: str

class DefaultProduct5(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce11(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct5 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig7(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')

class Sg(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce11
    feature_config: FeatureConfig7 = Field(..., alias='featureConfig')
    marketing: Marketing10

class Th(BaseModel):
    group: str
    marketing: Marketing10

class Commerce12(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig8(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing14(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Tk(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce12
    feature_config: FeatureConfig8 = Field(..., alias='featureConfig')
    marketing: Marketing14

class Tl(BaseModel):
    group: str

class To(BaseModel):
    group: str

class Tp(BaseModel):
    group: str

class Tv(BaseModel):
    group: str

class DefaultProduct6(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce13(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct6 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_e_guid: bool = Field(..., alias='requiresEGuid')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig9(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing15(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Tw(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce13
    feature_config: FeatureConfig9 = Field(..., alias='featureConfig')
    marketing: Marketing15

class Vn(BaseModel):
    group: str

class Vu(BaseModel):
    group: str

class Ws(BaseModel):
    group: str

class DefaultProduct7(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce14(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct7 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig10(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Ad(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce14
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing15

class Ae(BaseModel):
    group: str
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing15

class Commerce15(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ai(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce15
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing15

class DefaultProduct8(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce16(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct8 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Al(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce16
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing15

class Am(BaseModel):
    group: str

class An(BaseModel):
    group: str

class Ao(BaseModel):
    group: str

class Portability(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class DefaultProduct9(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce17(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct9 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class At(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce17
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing15

class Commerce18(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Aw(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce18
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing15

class Commerce19(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing22(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ax(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce19
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing22

class DefaultProduct10(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce20(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct10 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing23(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ba(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce20
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing23

class DefaultProduct11(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce21(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct11 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Be(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce21
    feature_config: FeatureConfig10 = Field(..., alias='featureConfig')
    marketing: Marketing23

class Bf(BaseModel):
    group: str

class DefaultProduct12(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce22(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    local_price_enabled: bool = Field(..., alias='localPriceEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct12 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig19(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class Bg(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce22
    feature_config: FeatureConfig19 = Field(..., alias='featureConfig')
    marketing: Marketing23

class Bh(BaseModel):
    group: str
    marketing: Marketing23

class Bi(BaseModel):
    group: str

class Bj(BaseModel):
    group: str

class Commerce23(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class FeatureConfig20(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing27(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Bl(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce23
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing27

class Commerce24(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing28(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Bm(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce24
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing28

class Commerce25(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bq(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce25
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing28

class Bv(BaseModel):
    group: str
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')

class Bw(BaseModel):
    group: str

class Cd(BaseModel):
    group: str

class Cf(BaseModel):
    group: str

class Cq(BaseModel):
    group: str

class DefaultProduct13(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce26(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct13 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ch(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce26
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing28

class Ci(BaseModel):
    group: str

class Cm(BaseModel):
    group: str

class Cs(BaseModel):
    footer: list[str]
    group: str
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')

class Cv(BaseModel):
    group: str

class Commerce27(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cw(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce27
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing28

class Commerce28(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing32(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cx(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce28
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing32

class Cy(BaseModel):
    footer: list[str]
    group: str
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')

class DefaultProduct14(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce29(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct14 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing33(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cz(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce29
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing33

class DefaultProduct15(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class RegulatedCancelFlow(BaseModel):
    cancel_footer_nav_to_sub_details: bool = Field(..., alias='cancelFooterNavToSubDetails')
    hide_cancel_footer_when_unauth: bool = Field(..., alias='hideCancelFooterWhenUnauth')
    show_regulated_cancellation_flow: bool = Field(..., alias='showRegulatedCancellationFlow')

class Commerce30(BaseModel):
    annual_auto_downgrade: bool = Field(..., alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct15 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow = Field(..., alias='regulatedCancelFlow')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool = Field(..., alias='requiresAdditionalSADisclaimer')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class De(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce30
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing33

class Dj(BaseModel):
    group: str

class DefaultProduct16(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce31(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct16 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Dk(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce31
    feature_config: FeatureConfig20 = Field(..., alias='featureConfig')
    marketing: Marketing33

class Dz(BaseModel):
    group: str
    marketing: Marketing33

class DefaultProduct17(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce32(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct17 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig32(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class Ee(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce32
    feature_config: FeatureConfig32 = Field(..., alias='featureConfig')
    marketing: Marketing33

class FeatureConfig33(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Eg(BaseModel):
    group: str
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing33

class Eh(BaseModel):
    group: str

class Er(BaseModel):
    group: str

class DefaultProduct18(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce33(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct18 = Field(..., alias='defaultProduct')
    disable_province_dropdown: bool = Field(..., alias='disableProvinceDropdown')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Es(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce33
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing33

class Et(BaseModel):
    group: str

class DefaultProduct19(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce34(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct19 = Field(..., alias='defaultProduct')
    disable_province_dropdown: bool = Field(..., alias='disableProvinceDropdown')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Fi(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce34
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing33

class Commerce35(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Fk(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce35
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing33

class Commerce36(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing42(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Fo(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce36
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing42

class DefaultProduct20(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce37(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct20 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow = Field(..., alias='regulatedCancelFlow')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool = Field(..., alias='requiresAdditionalSADisclaimer')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing43(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Fr(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce37
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing43

class Fx(BaseModel):
    group: str

class Ga(BaseModel):
    group: str

class DefaultProduct21(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce38(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct21 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gb(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce38
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing43

class Commerce39(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing45(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Gf(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce39
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing45

class Commerce40(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Gg(BaseModel):
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce40
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing45

class Gh(BaseModel):
    group: str

class Commerce41(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Gi(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce41
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing45

class DefaultProduct22(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce42(BaseModel):
    default_product: DefaultProduct22 = Field(..., alias='defaultProduct')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing48(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Gl(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce42
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing48

class Gm(BaseModel):
    group: str

class Gn(BaseModel):
    group: str

class Commerce43(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing49(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Gp(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce43
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing49

class Gq(BaseModel):
    group: str

class DefaultProduct23(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce44(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct23 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing50(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Gr(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce44
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing50

class Commerce45(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gs(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce45
    feature_config: FeatureConfig33 = Field(..., alias='featureConfig')
    marketing: Marketing50

class Gw(BaseModel):
    group: str

class DefaultProduct24(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce46(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct24 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig47(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class Hr(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce46
    feature_config: FeatureConfig47 = Field(..., alias='featureConfig')
    marketing: Marketing50

class DefaultProduct25(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce47(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct25 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig48(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Hu(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce47
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing50

class DefaultProduct26(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce48(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct26 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ie(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce48
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing50

class Il(BaseModel):
    group: str
    marketing: Marketing50

class Commerce49(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing56(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Im(BaseModel):
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce49
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing56

class Commerce50(BaseModel):
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Io(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce50
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing56

class Marketing58(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Iq(BaseModel):
    group: str
    marketing: Marketing58

class Ir(BaseModel):
    group: str

class DefaultProduct27(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce51(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct27 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Is(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce51
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing58

class DefaultProduct28(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce52(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct28 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class It(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce52
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing58

class Commerce53(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing61(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Je(BaseModel):
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce53
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing61

class Marketing62(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Jo(BaseModel):
    group: str
    marketing: Marketing62

class Ke(BaseModel):
    group: str

class Km(BaseModel):
    group: str

class Kw(BaseModel):
    group: str
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing62

class Commerce54(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ky(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce54
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing62

class Lb(BaseModel):
    group: str
    marketing: Marketing62

class DefaultProduct29(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce55(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct29 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Li(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce55
    feature_config: FeatureConfig48 = Field(..., alias='featureConfig')
    marketing: Marketing62

class Lr(BaseModel):
    group: str

class Ls(BaseModel):
    group: str

class DefaultProduct30(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce56(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct30 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig58(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class Lt(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce56
    feature_config: FeatureConfig58 = Field(..., alias='featureConfig')
    marketing: Marketing62

class DefaultProduct31(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce57(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct31 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig59(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Lu(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce57
    feature_config: FeatureConfig59 = Field(..., alias='featureConfig')
    marketing: Marketing62

class DefaultProduct32(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce58(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct32 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig60(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class Lv(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce58
    feature_config: FeatureConfig60 = Field(..., alias='featureConfig')
    marketing: Marketing62

class Ly(BaseModel):
    group: str

class Ma(BaseModel):
    group: str
    marketing: Marketing62

class DefaultProduct33(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce59(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    default_product: DefaultProduct33 = Field(..., alias='defaultProduct')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig61(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing71(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mc(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce59
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing71

class Md(BaseModel):
    group: str

class DefaultProduct34(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce60(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct34 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing72(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Me(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce60
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing72

class Commerce61(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing73(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mf(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce61
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing73

class Mg(BaseModel):
    group: str

class Commerce62(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    sells_bundle: bool = Field(..., alias='sellsBundle')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing74(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mh(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce62
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing74

class DefaultProduct35(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce63(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct35 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mk(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce63
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing74

class Ml(BaseModel):
    group: str

class Commerce64(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing76(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mq(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce64
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing76

class Mr(BaseModel):
    group: str

class Commerce65(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing77(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ms(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce65
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing77

class DefaultProduct36(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce66(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct36 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mt(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce66
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing77

class DefaultProduct37(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce67(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct37 = Field(..., alias='defaultProduct')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing79(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mu(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce67
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing79

class Mw(BaseModel):
    group: str

class Mz(BaseModel):
    group: str

class Na(BaseModel):
    group: str

class Commerce68(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Nc(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce68
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing79

class Ne(BaseModel):
    group: str

class Ng(BaseModel):
    group: str

class DefaultProduct38(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class LocalPayment(BaseModel):
    bank_options: list[str] = Field(..., alias='bankOptions')
    client_key: str

class Commerce69(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct38 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    local_payment: LocalPayment = Field(..., alias='localPayment')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing81(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Nl(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce69
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing81

class DefaultProduct39(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce70(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct39 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class No(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce70
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing81

class Nt(BaseModel):
    group: str

class Om(BaseModel):
    group: str
    marketing: Marketing81

class Commerce71(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing84(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Pf(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce71
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing84

class DefaultProduct40(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce72(BaseModel):
    annual_auto_downgrade: bool = Field(..., alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct40 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing85(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Pl(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce72
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing85

class Commerce73(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing86(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Pm(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce73
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing86

class Commerce74(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Pn(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce74
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing86

class Marketing88(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ps(BaseModel):
    group: str
    marketing: Marketing88

class DefaultProduct41(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce75(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct41 = Field(..., alias='defaultProduct')
    disable_province_dropdown: bool = Field(..., alias='disableProvinceDropdown')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pt(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce75
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing88

class Qa(BaseModel):
    group: str
    marketing: Marketing88

class Commerce76(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing91(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Re(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce76
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing91

class DefaultProduct42(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce77(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct42 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing92(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ro(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce77
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing92

class DefaultProduct43(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce78(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct43 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Rs(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce78
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing92

class Rw(BaseModel):
    group: str

class Sa(BaseModel):
    group: str
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing92

class Sc(BaseModel):
    group: str

class DefaultProduct44(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce79(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct44 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Se(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce79
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing92

class Commerce80(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing96(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sh(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce80
    feature_config: FeatureConfig61 = Field(..., alias='featureConfig')
    marketing: Marketing96

class DefaultProduct45(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce81(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct45 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig84(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class Marketing97(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Si(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce81
    feature_config: FeatureConfig84 = Field(..., alias='featureConfig')
    marketing: Marketing97

class Commerce82(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class FeatureConfig85(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing98(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sj(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce82
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing98

class DefaultProduct46(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce83(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct46 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing99(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sk(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce83
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing99

class Sl(BaseModel):
    group: str

class DefaultProduct47(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce84(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct47 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing100(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sm(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce84
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing100

class Sn(BaseModel):
    group: str

class So(BaseModel):
    group: str

class Ss(BaseModel):
    group: str

class St(BaseModel):
    group: str

class Commerce85(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing101(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sx(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce85
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing101

class Sy(BaseModel):
    group: str

class Sz(BaseModel):
    group: str

class Commerce86(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tc(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce86
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing101

class Td(BaseModel):
    group: str

class Commerce87(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing103(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Tf(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce87
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing103

class Tg(BaseModel):
    group: str

class Marketing104(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Tn(BaseModel):
    group: str
    marketing: Marketing104

class DefaultProduct48(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce88(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct48 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tr(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce88
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing104

class Tz(BaseModel):
    group: str

class Ua(BaseModel):
    group: str

class Ug(BaseModel):
    group: str

class Marketing106(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Uk(BaseModel):
    group: str
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing106

class DefaultProduct49(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce89(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct49 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Va(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce89
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing106

class Commerce90(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing108(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Vg(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce90
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing108

class Commerce91(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Marketing109(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Wf(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce91
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing109

class Commerce92(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Xk(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce92
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')

class Ye(BaseModel):
    group: str

class Commerce93(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Yt(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce93
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing109

class Yu(BaseModel):
    group: str

class Marketing111(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Za(BaseModel):
    group: str
    marketing: Marketing111

class Zm(BaseModel):
    group: str

class Zr(BaseModel):
    group: str

class Zw(BaseModel):
    group: str

class DefaultProduct50(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce94(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct50 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ag(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce94
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing111

class CancelSubscriptionNavItemPromoted(BaseModel):
    cancel_subscription_nav_item_period: int = Field(..., alias='cancelSubscriptionNavItemPeriod')

class DefaultProduct51(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce95(BaseModel):
    cancel_subscription_nav_item_promoted: CancelSubscriptionNavItemPromoted = Field(..., alias='cancelSubscriptionNavItemPromoted')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct51 = Field(..., alias='defaultProduct')
    is_one_step_cancel_billing_country: bool = Field(..., alias='isOneStepCancelBillingCountry')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ar(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce95
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct52(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce96(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct52 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bb(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce96
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct53(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce97(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct53 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bo(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce97
    feature_config: FeatureConfig85 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct54(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce98(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct54 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    starz_play_supported_regions: bool = Field(..., alias='starzPlaySupportedRegions')

class FeatureConfig101(BaseModel):
    display_additional_ratings: bool = Field(..., alias='displayAdditionalRatings')
    display_rating_advisories: bool = Field(..., alias='displayRatingAdvisories')
    enable_cmp: bool = Field(..., alias='enableCMP')

class Br(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce98
    feature_config: FeatureConfig101 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct55(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce99(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct55 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig102(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Bs(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce99
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct56(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce100(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct56 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bz(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce100
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct57(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce101(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct57 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cl(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce101
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct58(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce102(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct58 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Co(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce102
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct59(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce103(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct59 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cr(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce103
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct60(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce104(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct60 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Dm(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce104
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct61(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce105(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct61 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Do(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce105
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct62(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce106(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct62 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ec(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce106
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct63(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce107(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct63 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gd(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce107
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct64(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce108(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct64 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gt(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce108
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct65(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce109(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct65 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gy(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce109
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct66(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce110(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct66 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Hn(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce110
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct67(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce111(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct67 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ht(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce111
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct68(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce112(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct68 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Jm(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce112
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct69(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce113(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct69 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Kn(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce113
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct70(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce114(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct70 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Lc(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce114
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct71(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce115(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct71 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    starz_play_supported_regions: bool = Field(..., alias='starzPlaySupportedRegions')

class Mx(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce115
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct72(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce116(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct72 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ni(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce116
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct73(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce117(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct73 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pa(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce117
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct74(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce118(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct74 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pe(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce118
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct75(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce119(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct75 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Py(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce119
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct76(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce120(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct76 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Sr(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce120
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct77(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce121(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct77 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Sv(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce121
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct78(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce122(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct78 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tt(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce122
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct79(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce123(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct79 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Uy(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce123
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct80(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce124(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct80 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Vc(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce124
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class DefaultProduct81(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce125(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct81 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ve(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce125
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing111

class Commerce126(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing144(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class As(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce126
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing144

class DefaultProduct82(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce127(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct82 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing145(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ca(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce127
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing145

class Commerce128(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing146(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Gu(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce128
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing146

class Commerce129(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mp(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce129
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing146

class Commerce130(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pr(BaseModel):
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce130
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing146

class Commerce131(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    sells_bundle: bool = Field(..., alias='sellsBundle')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Marketing149(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Um(BaseModel):
    footer: list[str]
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce131
    feature_config: FeatureConfig102 = Field(..., alias='featureConfig')
    marketing: Marketing149

class AdsTierDevices(BaseModel):
    comcastx1: bool
    cox: bool
    hisense: bool
    lg: bool
    ps: bool
    ps4: bool
    samsung: bool
    vizio: bool
    xbox: bool

class DefaultProduct83(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase
    un_auth: UnAuth = Field(..., alias='unAuth')

class DevicesThatSell2PBundle(BaseModel):
    comcast: bool
    comcastx1: bool
    cox: bool
    lg: bool
    samsung: bool
    ps4: bool
    ps: bool
    tivo_us: bool
    vizio: bool
    xbox: bool
    xglobal: bool

class DevicesThatSellBundle(BaseModel):
    comcast: bool
    comcastx1: bool
    cox: bool
    lg: bool
    ps: bool
    ps4: bool
    samsung: bool
    tivo_us: bool
    vizio: bool
    xbox: bool
    xglobal: bool

class Amazon(BaseModel):
    type: str
    url: str

class Cox(BaseModel):
    type: str
    url: str

class Hisense(BaseModel):
    type: str
    url: str

class Lg(BaseModel):
    type: str
    url: str

class Ps1(BaseModel):
    type: str
    url: str

class Ps4(BaseModel):
    type: str
    url: str

class Samsung(BaseModel):
    type: str
    url: str

class TivoUs(BaseModel):
    type: str
    url: str

class Tv1(BaseModel):
    type: str
    url: str

class Vizio(BaseModel):
    type: str
    url: str

class Xbox(BaseModel):
    type: str
    url: str

class Xglobal(BaseModel):
    type: str
    url: str

class LicensePlateFlowNavigation(BaseModel):
    amazon: Amazon = Field(..., alias='AMAZON')
    cox: Cox
    hisense: Hisense
    lg: Lg
    ps: Ps1
    ps4: Ps4
    samsung: Samsung
    tivo_us: TivoUs
    tv: Tv1
    vizio: Vizio
    xbox: Xbox
    xglobal: Xglobal

class NineMonth(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    price: float
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class OneYear(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    price: float
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class SixMonth(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    price: float
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class ThreeYear(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    price: float
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class TwoYear(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    price: float
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class Ft(BaseModel):
    nine_month: NineMonth = Field(..., alias='nineMonth')
    one_year: OneYear = Field(..., alias='oneYear')
    six_month: SixMonth = Field(..., alias='sixMonth')
    three_year: ThreeYear = Field(..., alias='threeYear')
    two_year: TwoYear = Field(..., alias='twoYear')

class Purchase84(BaseModel):
    nine_month: NineMonth = Field(..., alias='nineMonth')
    one_year: OneYear = Field(..., alias='oneYear')
    six_month: SixMonth = Field(..., alias='sixMonth')
    three_year: ThreeYear = Field(..., alias='threeYear')
    two_year: TwoYear = Field(..., alias='twoYear')

class Superbundle(BaseModel):
    nine_month: NineMonth = Field(..., alias='nineMonth')
    one_year: OneYear = Field(..., alias='oneYear')
    six_month: SixMonth = Field(..., alias='sixMonth')

class RewardsProducts(BaseModel):
    ft: Ft = Field(..., alias='FT')
    purchase: Purchase84
    superbundle: Superbundle

class Commerce132(BaseModel):
    ads_tier_devices: AdsTierDevices = Field(..., alias='adsTierDevices')
    ads_tier_enabled: bool = Field(..., alias='adsTierEnabled')
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct83 = Field(..., alias='defaultProduct')
    devices_that_sell2_p_bundle: DevicesThatSell2PBundle = Field(..., alias='devicesThatSell2PBundle')
    devices_that_sell_bundle: DevicesThatSellBundle = Field(..., alias='devicesThatSellBundle')
    enable_global_identity_unbranded_create_account: bool = Field(..., alias='enableGlobalIdentityUnbrandedCreateAccount')
    license_plate_flow_navigation: LicensePlateFlowNavigation = Field(..., alias='licensePlateFlowNavigation')
    one_step_cancel_billing_states: list[str] = Field(..., alias='oneStepCancelBillingStates')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_annual_opt_in_states: list[str] = Field(..., alias='requiresAnnualOptInStates')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    rewards_products: RewardsProducts = Field(..., alias='rewardsProducts')
    sells_bundle: bool = Field(..., alias='sellsBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig135(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    enable_identity_consent_sync: bool = Field(..., alias='enableIdentityConsentSync')

class Us(BaseModel):
    footer: list[str]
    group: str
    commerce: Commerce132
    feature_config: FeatureConfig135 = Field(..., alias='featureConfig')
    marketing: Marketing149

class Commerce133(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class FeatureConfig136(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Marketing151(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Vi(BaseModel):
    parent_country: str = Field(..., alias='parentCountry')
    group: str
    commerce: Commerce133
    feature_config: FeatureConfig136 = Field(..., alias='featureConfig')
    marketing: Marketing151

class Yz(BaseModel):
    group: str
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')

class Countries(BaseModel):
    af: Af = Field(..., alias='AF')
    au: Au = Field(..., alias='AU')
    bd: Bd = Field(..., alias='BD')
    bn: Bn = Field(..., alias='BN')
    bt: Bt = Field(..., alias='BT')
    bu: Bu = Field(..., alias='BU')
    cc: Cc = Field(..., alias='CC')
    ck: Ck = Field(..., alias='CK')
    cn: Cn = Field(..., alias='CN')
    fj: Fj = Field(..., alias='FJ')
    hk: Hk = Field(..., alias='HK')
    hm: Hm = Field(..., alias='HM')
    id: Id = Field(..., alias='ID')
    in_: In = Field(..., alias='IN')
    jp: Jp = Field(..., alias='JP')
    kh: Kh = Field(..., alias='KH')
    ki: Ki = Field(..., alias='KI')
    kr: Kr = Field(..., alias='KR')
    la: La = Field(..., alias='LA')
    lk: Lk = Field(..., alias='LK')
    mm: Mm = Field(..., alias='MM')
    mo: Mo = Field(..., alias='MO')
    mv: Mv = Field(..., alias='MV')
    my: My = Field(..., alias='MY')
    nf: Nf = Field(..., alias='NF')
    np: Np = Field(..., alias='NP')
    nr: Nr = Field(..., alias='NR')
    nu: Nu4 = Field(..., alias='NU')
    nz: Nz = Field(..., alias='NZ')
    pg: Pg = Field(..., alias='PG')
    ph: Ph = Field(..., alias='PH')
    pk: Pk = Field(..., alias='PK')
    sb: Sb = Field(..., alias='SB')
    sg: Sg = Field(..., alias='SG')
    th: Th = Field(..., alias='TH')
    tk: Tk = Field(..., alias='TK')
    tl: Tl = Field(..., alias='TL')
    to: To = Field(..., alias='TO')
    tp: Tp = Field(..., alias='TP')
    tv: Tv = Field(..., alias='TV')
    tw: Tw = Field(..., alias='TW')
    vn: Vn = Field(..., alias='VN')
    vu: Vu = Field(..., alias='VU')
    ws: Ws = Field(..., alias='WS')
    ad: Ad = Field(..., alias='AD')
    ae: Ae = Field(..., alias='AE')
    ai: Ai = Field(..., alias='AI')
    al: Al = Field(..., alias='AL')
    am: Am = Field(..., alias='AM')
    an: An = Field(..., alias='AN')
    ao: Ao = Field(..., alias='AO')
    at: At = Field(..., alias='AT')
    aw: Aw = Field(..., alias='AW')
    ax: Ax = Field(..., alias='AX')
    ba: Ba = Field(..., alias='BA')
    be: Be = Field(..., alias='BE')
    bf: Bf = Field(..., alias='BF')
    bg: Bg = Field(..., alias='BG')
    bh: Bh = Field(..., alias='BH')
    bi: Bi = Field(..., alias='BI')
    bj: Bj = Field(..., alias='BJ')
    bl: Bl = Field(..., alias='BL')
    bm: Bm = Field(..., alias='BM')
    bq: Bq = Field(..., alias='BQ')
    bv: Bv = Field(..., alias='BV')
    bw: Bw = Field(..., alias='BW')
    cd: Cd = Field(..., alias='CD')
    cf: Cf = Field(..., alias='CF')
    cq: Cq = Field(..., alias='CQ')
    ch: Ch = Field(..., alias='CH')
    ci: Ci = Field(..., alias='CI')
    cm: Cm = Field(..., alias='CM')
    cs: Cs = Field(..., alias='CS')
    cv: Cv = Field(..., alias='CV')
    cw: Cw = Field(..., alias='CW')
    cx: Cx = Field(..., alias='CX')
    cy: Cy = Field(..., alias='CY')
    cz: Cz = Field(..., alias='CZ')
    de: De = Field(..., alias='DE')
    dj: Dj = Field(..., alias='DJ')
    dk: Dk = Field(..., alias='DK')
    dz: Dz = Field(..., alias='DZ')
    ee: Ee = Field(..., alias='EE')
    eg: Eg = Field(..., alias='EG')
    eh: Eh = Field(..., alias='EH')
    er: Er = Field(..., alias='ER')
    es: Es = Field(..., alias='ES')
    et: Et = Field(..., alias='ET')
    fi: Fi = Field(..., alias='FI')
    fk: Fk = Field(..., alias='FK')
    fo: Fo = Field(..., alias='FO')
    fr: Fr = Field(..., alias='FR')
    fx: Fx = Field(..., alias='FX')
    ga: Ga = Field(..., alias='GA')
    gb: Gb = Field(..., alias='GB')
    gf: Gf = Field(..., alias='GF')
    gg: Gg = Field(..., alias='GG')
    gh: Gh = Field(..., alias='GH')
    gi: Gi = Field(..., alias='GI')
    gl: Gl = Field(..., alias='GL')
    gm: Gm = Field(..., alias='GM')
    gn: Gn = Field(..., alias='GN')
    gp: Gp = Field(..., alias='GP')
    gq: Gq = Field(..., alias='GQ')
    gr: Gr = Field(..., alias='GR')
    gs: Gs = Field(..., alias='GS')
    gw: Gw = Field(..., alias='GW')
    hr: Hr = Field(..., alias='HR')
    hu: Hu = Field(..., alias='HU')
    ie: Ie = Field(..., alias='IE')
    il: Il = Field(..., alias='IL')
    im: Im = Field(..., alias='IM')
    io: Io = Field(..., alias='IO')
    iq: Iq = Field(..., alias='IQ')
    ir: Ir = Field(..., alias='IR')
    is_: Is = Field(..., alias='IS')
    it: It = Field(..., alias='IT')
    je: Je = Field(..., alias='JE')
    jo: Jo = Field(..., alias='JO')
    ke: Ke = Field(..., alias='KE')
    km: Km = Field(..., alias='KM')
    kw: Kw = Field(..., alias='KW')
    ky: Ky = Field(..., alias='KY')
    lb: Lb = Field(..., alias='LB')
    li: Li = Field(..., alias='LI')
    lr: Lr = Field(..., alias='LR')
    ls: Ls = Field(..., alias='LS')
    lt: Lt = Field(..., alias='LT')
    lu: Lu = Field(..., alias='LU')
    lv: Lv = Field(..., alias='LV')
    ly: Ly = Field(..., alias='LY')
    ma: Ma = Field(..., alias='MA')
    mc: Mc = Field(..., alias='MC')
    md: Md = Field(..., alias='MD')
    me: Me = Field(..., alias='ME')
    mf: Mf = Field(..., alias='MF')
    mg: Mg = Field(..., alias='MG')
    mh: Mh = Field(..., alias='MH')
    mk: Mk = Field(..., alias='MK')
    ml: Ml = Field(..., alias='ML')
    mq: Mq = Field(..., alias='MQ')
    mr: Mr = Field(..., alias='MR')
    ms: Ms = Field(..., alias='MS')
    mt: Mt = Field(..., alias='MT')
    mu: Mu = Field(..., alias='MU')
    mw: Mw = Field(..., alias='MW')
    mz: Mz = Field(..., alias='MZ')
    na: Na = Field(..., alias='NA')
    nc: Nc = Field(..., alias='NC')
    ne: Ne = Field(..., alias='NE')
    ng: Ng = Field(..., alias='NG')
    nl: Nl = Field(..., alias='NL')
    no: No = Field(..., alias='NO')
    nt: Nt = Field(..., alias='NT')
    om: Om = Field(..., alias='OM')
    pf: Pf = Field(..., alias='PF')
    pl: Pl = Field(..., alias='PL')
    pm: Pm = Field(..., alias='PM')
    pn: Pn = Field(..., alias='PN')
    ps: Ps = Field(..., alias='PS')
    pt: Pt = Field(..., alias='PT')
    qa: Qa = Field(..., alias='QA')
    re: Re = Field(..., alias='RE')
    ro: Ro = Field(..., alias='RO')
    rs: Rs = Field(..., alias='RS')
    rw: Rw = Field(..., alias='RW')
    sa: Sa = Field(..., alias='SA')
    sc: Sc = Field(..., alias='SC')
    se: Se = Field(..., alias='SE')
    sh: Sh = Field(..., alias='SH')
    si: Si = Field(..., alias='SI')
    sj: Sj = Field(..., alias='SJ')
    sk: Sk = Field(..., alias='SK')
    sl: Sl = Field(..., alias='SL')
    sm: Sm = Field(..., alias='SM')
    sn: Sn = Field(..., alias='SN')
    so: So = Field(..., alias='SO')
    ss: Ss = Field(..., alias='SS')
    st: St = Field(..., alias='ST')
    sx: Sx = Field(..., alias='SX')
    sy: Sy = Field(..., alias='SY')
    sz: Sz = Field(..., alias='SZ')
    tc: Tc = Field(..., alias='TC')
    td: Td = Field(..., alias='TD')
    tf: Tf = Field(..., alias='TF')
    tg: Tg = Field(..., alias='TG')
    tn: Tn = Field(..., alias='TN')
    tr: Tr = Field(..., alias='TR')
    tz: Tz = Field(..., alias='TZ')
    ua: Ua = Field(..., alias='UA')
    ug: Ug = Field(..., alias='UG')
    uk: Uk = Field(..., alias='UK')
    va: Va = Field(..., alias='VA')
    vg: Vg = Field(..., alias='VG')
    wf: Wf = Field(..., alias='WF')
    xk: Xk = Field(..., alias='XK')
    ye: Ye = Field(..., alias='YE')
    yt: Yt = Field(..., alias='YT')
    yu: Yu = Field(..., alias='YU')
    za: Za = Field(..., alias='ZA')
    zm: Zm = Field(..., alias='ZM')
    zr: Zr = Field(..., alias='ZR')
    zw: Zw = Field(..., alias='ZW')
    ag: Ag = Field(..., alias='AG')
    ar: Ar = Field(..., alias='AR')
    bb: Bb = Field(..., alias='BB')
    bo: Bo = Field(..., alias='BO')
    br: Br = Field(..., alias='BR')
    bs: Bs = Field(..., alias='BS')
    bz: Bz = Field(..., alias='BZ')
    cl: Cl = Field(..., alias='CL')
    co: Co = Field(..., alias='CO')
    cr: Cr = Field(..., alias='CR')
    dm: Dm = Field(..., alias='DM')
    do: Do = Field(..., alias='DO')
    ec: Ec = Field(..., alias='EC')
    gd: Gd = Field(..., alias='GD')
    gt: Gt = Field(..., alias='GT')
    gy: Gy = Field(..., alias='GY')
    hn: Hn = Field(..., alias='HN')
    ht: Ht = Field(..., alias='HT')
    jm: Jm = Field(..., alias='JM')
    kn: Kn = Field(..., alias='KN')
    lc: Lc = Field(..., alias='LC')
    mx: Mx = Field(..., alias='MX')
    ni: Ni = Field(..., alias='NI')
    pa: Pa = Field(..., alias='PA')
    pe: Pe = Field(..., alias='PE')
    py: Py = Field(..., alias='PY')
    sr: Sr = Field(..., alias='SR')
    sv: Sv = Field(..., alias='SV')
    tt: Tt = Field(..., alias='TT')
    uy: Uy = Field(..., alias='UY')
    vc: Vc = Field(..., alias='VC')
    ve: Ve = Field(..., alias='VE')
    as_: As = Field(..., alias='AS')
    ca: Ca = Field(..., alias='CA')
    gu: Gu = Field(..., alias='GU')
    mp: Mp = Field(..., alias='MP')
    pr: Pr = Field(..., alias='PR')
    um: Um = Field(..., alias='UM')
    us: Us = Field(..., alias='US')
    vi: Vi = Field(..., alias='VI')
    yz: Yz = Field(..., alias='YZ')
    time_stamp: dict[str, Any] = Field(..., alias='timeStamp')

class UseWebPlaybackExperienceOverrides(BaseModel):
    live_linear_playlist_type: str = Field(..., alias='liveLinearPlaylistType')

class FeatureConfig137(BaseModel):
    activation_retry_enabled: bool = Field(..., alias='activationRetryEnabled')
    commerce_unified_activation_callback_provider_ids: list[str] = Field(..., alias='commerceUnifiedActivationCallbackProviderIds')
    commerce_unified_activation_success_enabled_provider_ids: list[str] = Field(..., alias='commerceUnifiedActivationSuccessEnabledProviderIds')
    disable_account_delete: bool = Field(..., alias='disableAccountDelete')
    disable_account_hold: bool = Field(..., alias='disableAccountHold')
    disable_activation: bool = Field(..., alias='disableActivation')
    disable_adobe_launch: bool = Field(..., alias='disableAdobeLaunch')
    disable_app_settings: bool = Field(..., alias='disableAppSettings')
    disable_bam_tech_sdk: bool = Field(..., alias='disableBAMTechSDK')
    disable_commerce_refactor: bool = Field(..., alias='disableCommerceRefactor')
    disable_content_overrides: bool = Field(..., alias='disableContentOverrides')
    disable_early_access_refactor: bool = Field(..., alias='disableEarlyAccessRefactor')
    disable_free_trial_fraud: bool = Field(..., alias='disableFreeTrialFraud')
    disable_hulu_redirect: bool = Field(..., alias='disableHuluRedirect')
    disable_nsb_legacy_hubs: bool = Field(..., alias='disableNsbLegacyHubs')
    disable_mega_bundle: bool = Field(..., alias='disableMegaBundle')
    disable_o_auth: bool = Field(..., alias='disableOAuth')
    disable_one_trust: bool = Field(..., alias='disableOneTrust')
    disable_overlay_ad_blurb: bool = Field(..., alias='disableOverlayAdBlurb')
    disable_payment_blockage: bool = Field(..., alias='disablePaymentBlockage')
    disable_paywall_fallback: bool = Field(..., alias='disablePaywallFallback')
    disable_pittsburgh: bool = Field(..., alias='disablePittsburgh')
    disable_restart_eligible: bool = Field(..., alias='disableRestartEligible')
    disable_tandem_flow: bool = Field(..., alias='disableTandemFlow')
    disable_unification: bool = Field(..., alias='disableUnification')
    disable_welch: bool = Field(..., alias='disableWelch')
    enable_account_price_change_messaging: bool = Field(..., alias='enableAccountPriceChangeMessaging')
    enable_amp_weapon_x: bool = Field(..., alias='enableAmpWeaponX')
    enable_partner_win_back: bool = Field(..., alias='enablePartnerWinBack')
    enable_analytics_validation: bool = Field(..., alias='enableAnalyticsValidation')
    enable_braintree_paypal: bool = Field(..., alias='enableBraintreePaypal')
    enable_braze: bool = Field(..., alias='enableBraze')
    enable_braze_logging: bool = Field(..., alias='enableBrazeLogging')
    enable_cancel_stop_gap: bool = Field(..., alias='enableCancelStopGap')
    enable_charter_activate_review_page: bool = Field(..., alias='enableCharterActivateReviewPage')
    enable_cnbl_footer: bool = Field(..., alias='enableCnblFooter')
    enable_nsb_cannonball: bool = Field(..., alias='enableNsbCannonball')
    enable_nsb_cannonball_hubs: bool = Field(..., alias='enableNsbCannonballHubs')
    enable_commerce_complete_account_info_route: bool = Field(..., alias='enableCommerceCompleteAccountInfoRoute')
    enable_commerce_membership_pause: bool = Field(..., alias='enableCommerceMembershipPause')
    enable_commerce_price_increase_consent: bool = Field(..., alias='enableCommercePriceIncreaseConsent')
    enable_commerce_tiara: bool = Field(..., alias='enableCommerceTiara')
    enable_commerce_unified_account_home: bool = Field(..., alias='enableCommerceUnifiedAccountHome')
    enable_commerce_unified_activation_route: bool = Field(..., alias='enableCommerceUnifiedActivationRoute')
    enable_commerce_unified_activation_success: bool = Field(..., alias='enableCommerceUnifiedActivationSuccess')
    enable_commerce_unified_billing_history: bool = Field(..., alias='enableCommerceUnifiedBillingHistory')
    enable_commerce_unified_callback_route: bool = Field(..., alias='enableCommerceUnifiedCallbackRoute')
    enable_commerce_unified_cancel_contract_route: bool = Field(..., alias='enableCommerceUnifiedCancelContractRoute')
    enable_commerce_unified_cancel_route: bool = Field(..., alias='enableCommerceUnifiedCancelRoute')
    enable_commerce_unified_cancel_landing_route: bool = Field(..., alias='enableCommerceUnifiedCancelLandingRoute')
    enable_commerce_unified_change_subscription: bool = Field(..., alias='enableCommerceUnifiedChangeSubscription')
    enable_commerce_unified_extra_member: bool = Field(..., alias='enableCommerceUnifiedExtraMember')
    enable_commerce_unified_extra_member_access_route: bool = Field(..., alias='enableCommerceUnifiedExtraMemberAccessRoute')
    enable_commerce_unified_outgoing_activation_route: bool = Field(..., alias='enableCommerceUnifiedOutgoingActivationRoute')
    enable_commerce_unified_plans: bool = Field(..., alias='enableCommerceUnifiedPlans')
    enable_commerce_unified_signup_flow: bool = Field(..., alias='enableCommerceUnifiedSignupFlow')
    enable_commerce_unified_redemption: bool = Field(..., alias='enableCommerceUnifiedRedemption')
    enable_commerce_unified_welcome_back: bool = Field(..., alias='enableCommerceUnifiedWelcomeBack')
    enable_commerce_v2_dob: bool = Field(..., alias='enableCommerceV2DOB')
    enable_dictionary_draft_state: bool = Field(..., alias='enableDictionaryDraftState')
    enable_dob_collection_legal_copy: bool = Field(..., alias='enableDOBCollectionLegalCopy')
    enable_explore_api_for_hubs: bool = Field(..., alias='enableExploreApiForHubs')
    enable_explore_nsb_redirect_to_browse: bool = Field(..., alias='enableExploreNsbRedirectToBrowse')
    enable_explore_page: bool = Field(..., alias='enableExplorePage')
    enable_explore_us: bool = Field(..., alias='enableExploreUs')
    enable_explore_api_for_nsb: bool = Field(..., alias='enableExploreApiForNsb')
    enable_flex_powered_activation_success_screen: bool = Field(..., alias='enableFlexPoweredActivationSuccessScreen')
    enable_gift_card: bool = Field(..., alias='enableGiftCard')
    enable_global_footer: bool = Field(..., alias='enableGlobalFooter')
    enable_global_identity_unbranded_create_account: bool = Field(..., alias='enableGlobalIdentityUnbrandedCreateAccount')
    enable_global_identity_unbranded_credentials_update: bool = Field(..., alias='enableGlobalIdentityUnbrandedCredentialsUpdate')
    enable_identity_consent_sync: bool = Field(..., alias='enableIdentityConsentSync')
    enable_identity_create_account_route: bool = Field(..., alias='enableIdentityCreateAccountRoute')
    enable_identity_magic_link_route: bool = Field(..., alias='enableIdentityMagicLinkRoute')
    enable_identity_manage_devices_route: bool = Field(..., alias='enableIdentityManageDevicesRoute')
    enable_identity_o_auth_review_terms_route: bool = Field(..., alias='enableIdentityOAuthReviewTermsRoute')
    enable_identity_one_id_authentication: bool = Field(..., alias='enableIdentityOneIdAuthentication')
    enable_identity_review_and_accept_route: bool = Field(..., alias='enableIdentityReviewAndAcceptRoute')
    enable_identity_unified_auth_flows: bool = Field(..., alias='enableIdentityUnifiedAuthFlows')
    enable_identity_unified_account_delete: bool = Field(..., alias='enableIdentityUnifiedAccountDelete')
    enable_identity_unified_license_plate_flow: bool = Field(..., alias='enableIdentityUnifiedLicensePlateFlow')
    enable_identity_verify_route: bool = Field(..., alias='enableIdentityVerifyRoute')
    enable_identity_unified_nielsen_route: bool = Field(..., alias='enableIdentityUnifiedNielsenRoute')
    enable_individual_date_replaces: bool = Field(..., alias='enableIndividualDateReplaces')
    enable_inline_wpnx_experimentation: bool = Field(..., alias='enableInlineWPNXExperimentation')
    enable_nsb_commerce_plans_cta: bool = Field(..., alias='enableNsbCommercePlansCta')
    enable_onboarding_existing_users: bool = Field(..., alias='enableOnboardingExistingUsers')
    enable_profiles_linking_route: bool = Field(..., alias='enableProfilesLinkingRoute')
    enable_profiles_loading_route: bool = Field(..., alias='enableProfilesLoadingRoute')
    enable_profiles_routes: bool = Field(..., alias='enableProfilesRoutes')
    enable_profiles_setup_route: bool = Field(..., alias='enableProfilesSetupRoute')
    enable_privacy_consent_package: bool = Field(..., alias='enablePrivacyConsentPackage')
    enable_regulated_cancellation: bool = Field(..., alias='enableRegulatedCancellation')
    enable_unauth_sub_id_cancellation: bool = Field(..., alias='enableUnauthSubIdCancellation')
    enable_redux_logging: bool = Field(..., alias='enableReduxLogging')
    enable_redux_dev_tools: bool = Field(..., alias='enableReduxDevTools')
    enable_restart_eligible_for_world: bool = Field(..., alias='enableRestartEligibleForWorld')
    enable_roku_rpm_cancel_switch: bool = Field(..., alias='enableRokuRPMCancelSwitch')
    enable_should_use_legacy_sash: bool = Field(..., alias='enableShouldUseLegacySASH')
    enable_sign_up_flow_add_ons_route: bool = Field(..., alias='enableSignUpFlowAddOnsRoute')
    enable_sign_up_flow_cadence_route: bool = Field(..., alias='enableSignUpFlowCadenceRoute')
    enable_tenant_specific_header: bool = Field(..., alias='enableTenantSpecificHeader')
    enable_update_credentials_route: bool = Field(..., alias='enableUpdateCredentialsRoute')
    env: str
    live_selection_modal_enabled: bool = Field(..., alias='liveSelectionModalEnabled')
    unified_billing_history_rollout: str = Field(..., alias='unifiedBillingHistoryRollout')
    use_web_playback_experience_overrides: UseWebPlaybackExperienceOverrides = Field(..., alias='useWebPlaybackExperienceOverrides')
    enable_license_plate_dynamic_routes: bool = Field(..., alias='enableLicensePlateDynamicRoutes')
    enable_taste_picking_route: bool = Field(..., alias='enableTastePickingRoute')
    enable_spaceball_explore: bool = Field(..., alias='enableSpaceballExplore')
    enable_spaceball_mlp: bool = Field(..., alias='enableSpaceballMlp')
    enable_spaceball_whats_on: bool = Field(..., alias='enableSpaceballWhatsOn')

class AppLangMap(BaseModel):
    ar_ae: str = Field(..., alias='ar-ae')
    ar_ar: str = Field(..., alias='ar-ar')
    ar_bh: str = Field(..., alias='ar-bh')
    ar_dz: str = Field(..., alias='ar-dz')
    ar_eg: str = Field(..., alias='ar-eg')
    ar_iq: str = Field(..., alias='ar-iq')
    ar_jo: str = Field(..., alias='ar-jo')
    ar_kw: str = Field(..., alias='ar-kw')
    ar_lb: str = Field(..., alias='ar-lb')
    ar_ma: str = Field(..., alias='ar-ma')
    ar_om: str = Field(..., alias='ar-om')
    ar_ps: str = Field(..., alias='ar-ps')
    ar_qa: str = Field(..., alias='ar-qa')
    ar_sa: str = Field(..., alias='ar-sa')
    ar_tn: str = Field(..., alias='ar-tn')
    bg_bg: str = Field(..., alias='bg-bg')
    cs_cz: str = Field(..., alias='cs-cz')
    da_dk: str = Field(..., alias='da-dk')
    da_fo: str = Field(..., alias='da-fo')
    da_gl: str = Field(..., alias='da-gl')
    de_at: str = Field(..., alias='de-at')
    de_ch: str = Field(..., alias='de-ch')
    de_de: str = Field(..., alias='de-de')
    de_li: str = Field(..., alias='de-li')
    de_lu: str = Field(..., alias='de-lu')
    el_gr: str = Field(..., alias='el-gr')
    en: str
    en_ad: str = Field(..., alias='en-ad')
    en_ae: str = Field(..., alias='en-ae')
    en_ag: str = Field(..., alias='en-ag')
    en_ai: str = Field(..., alias='en-ai')
    en_al: str = Field(..., alias='en-al')
    en_ar: str = Field(..., alias='en-ar')
    en_as: str = Field(..., alias='en-as')
    en_at: str = Field(..., alias='en-at')
    en_au: str = Field(..., alias='en-au')
    en_aw: str = Field(..., alias='en-aw')
    en_ax: str = Field(..., alias='en-ax')
    en_ba: str = Field(..., alias='en-ba')
    en_bb: str = Field(..., alias='en-bb')
    en_be: str = Field(..., alias='en-be')
    en_bg: str = Field(..., alias='en-bg')
    en_bh: str = Field(..., alias='en-bh')
    en_bm: str = Field(..., alias='en-bm')
    en_bo: str = Field(..., alias='en-bo')
    en_bq: str = Field(..., alias='en-bq')
    en_br: str = Field(..., alias='en-br')
    en_bs: str = Field(..., alias='en-bs')
    en_bz: str = Field(..., alias='en-bz')
    en_ca: str = Field(..., alias='en-ca')
    en_cc: str = Field(..., alias='en-cc')
    en_ch: str = Field(..., alias='en-ch')
    en_ck: str = Field(..., alias='en-ck')
    en_cl: str = Field(..., alias='en-cl')
    en_co: str = Field(..., alias='en-co')
    en_cr: str = Field(..., alias='en-cr')
    en_cw: str = Field(..., alias='en-cw')
    en_cx: str = Field(..., alias='en-cx')
    en_cz: str = Field(..., alias='en-cz')
    en_de: str = Field(..., alias='en-de')
    en_dk: str = Field(..., alias='en-dk')
    en_dm: str = Field(..., alias='en-dm')
    en_dz: str = Field(..., alias='en-dz')
    en_do: str = Field(..., alias='en-do')
    en_ec: str = Field(..., alias='en-ec')
    en_ee: str = Field(..., alias='en-ee')
    en_eg: str = Field(..., alias='en-eg')
    en_es: str = Field(..., alias='en-es')
    en_fi: str = Field(..., alias='en-fi')
    en_fk: str = Field(..., alias='en-fk')
    en_fo: str = Field(..., alias='en-fo')
    en_fr: str = Field(..., alias='en-fr')
    en_gb: str = Field(..., alias='en-gb')
    en_gd: str = Field(..., alias='en-gd')
    en_gi: str = Field(..., alias='en-gi')
    en_gl: str = Field(..., alias='en-gl')
    en_gr: str = Field(..., alias='en-gr')
    en_gs: str = Field(..., alias='en-gs')
    en_gt: str = Field(..., alias='en-gt')
    en_gu: str = Field(..., alias='en-gu')
    en_gy: str = Field(..., alias='en-gy')
    en_hk: str = Field(..., alias='en-hk')
    en_hn: str = Field(..., alias='en-hn')
    en_hr: str = Field(..., alias='en-hr')
    en_ht: str = Field(..., alias='en-ht')
    en_hu: str = Field(..., alias='en-hu')
    en_id: str = Field(..., alias='en-id')
    en_ie: str = Field(..., alias='en-ie')
    en_il: str = Field(..., alias='en-il')
    en_io: str = Field(..., alias='en-io')
    en_iq: str = Field(..., alias='en-iq')
    en_is: str = Field(..., alias='en-is')
    en_it: str = Field(..., alias='en-it')
    en_jm: str = Field(..., alias='en-jm')
    en_jo: str = Field(..., alias='en-jo')
    en_jp: str = Field(..., alias='en-jp')
    en_kn: str = Field(..., alias='en-kn')
    en_kr: str = Field(..., alias='en-kr')
    en_kw: str = Field(..., alias='en-kw')
    en_ky: str = Field(..., alias='en-ky')
    en_lb: str = Field(..., alias='en-lb')
    en_lc: str = Field(..., alias='en-lc')
    en_li: str = Field(..., alias='en-li')
    en_lt: str = Field(..., alias='en-lt')
    en_lu: str = Field(..., alias='en-lu')
    en_lv: str = Field(..., alias='en-lv')
    en_ma: str = Field(..., alias='en-ma')
    en_me: str = Field(..., alias='en-me')
    en_mh: str = Field(..., alias='en-mh')
    en_mk: str = Field(..., alias='en-mk')
    en_mp: str = Field(..., alias='en-mp')
    en_ms: str = Field(..., alias='en-ms')
    en_mt: str = Field(..., alias='en-mt')
    en_mx: str = Field(..., alias='en-mx')
    en_my: str = Field(..., alias='en-my')
    en_nf: str = Field(..., alias='en-nf')
    en_ni: str = Field(..., alias='en-ni')
    en_nl: str = Field(..., alias='en-nl')
    en_no: str = Field(..., alias='en-no')
    en_nu: str = Field(..., alias='en-nu')
    en_th: str = Field(..., alias='en-th')
    en_nz: str = Field(..., alias='en-nz')
    en_om: str = Field(..., alias='en-om')
    en_pa: str = Field(..., alias='en-pa')
    en_pe: str = Field(..., alias='en-pe')
    en_pf: str = Field(..., alias='en-pf')
    en_ph: str = Field(..., alias='en-ph')
    en_pl: str = Field(..., alias='en-pl')
    en_pm: str = Field(..., alias='en-pm')
    en_pn: str = Field(..., alias='en-pn')
    en_pr: str = Field(..., alias='en-pr')
    en_ps: str = Field(..., alias='en-ps')
    en_pt: str = Field(..., alias='en-pt')
    en_qa: str = Field(..., alias='en-qa')
    en_py: str = Field(..., alias='en-py')
    en_ro: str = Field(..., alias='en-ro')
    en_rs: str = Field(..., alias='en-rs')
    en_sa: str = Field(..., alias='en-sa')
    en_se: str = Field(..., alias='en-se')
    en_sh: str = Field(..., alias='en-sh')
    en_si: str = Field(..., alias='en-si')
    en_sj: str = Field(..., alias='en-sj')
    en_sk: str = Field(..., alias='en-sk')
    en_sm: str = Field(..., alias='en-sm')
    en_sr: str = Field(..., alias='en-sr')
    en_sv: str = Field(..., alias='en-sv')
    en_sx: str = Field(..., alias='en-sx')
    en_tc: str = Field(..., alias='en-tc')
    en_tf: str = Field(..., alias='en-tf')
    en_tk: str = Field(..., alias='en-tk')
    en_tn: str = Field(..., alias='en-tn')
    en_tr: str = Field(..., alias='en-tr')
    en_tt: str = Field(..., alias='en-tt')
    en_tw: str = Field(..., alias='en-tw')
    en_um: str = Field(..., alias='en-um')
    en_uy: str = Field(..., alias='en-uy')
    en_va: str = Field(..., alias='en-va')
    en_vc: str = Field(..., alias='en-vc')
    en_ve: str = Field(..., alias='en-ve')
    en_vg: str = Field(..., alias='en-vg')
    en_za: str = Field(..., alias='en-za')
    es_ad: str = Field(..., alias='es-ad')
    es_ar: str = Field(..., alias='es-ar')
    es_bo: str = Field(..., alias='es-bo')
    es_cl: str = Field(..., alias='es-cl')
    es_co: str = Field(..., alias='es-co')
    es_cr: str = Field(..., alias='es-cr')
    es_do: str = Field(..., alias='es-do')
    es_ec: str = Field(..., alias='es-ec')
    es_es: str = Field(..., alias='es-es')
    es_gt: str = Field(..., alias='es-gt')
    es_hn: str = Field(..., alias='es-hn')
    es_mx: str = Field(..., alias='es-mx')
    es_ni: str = Field(..., alias='es-ni')
    es_pa: str = Field(..., alias='es-pa')
    es_pe: str = Field(..., alias='es-pe')
    es_py: str = Field(..., alias='es-py')
    es_sv: str = Field(..., alias='es-sv')
    es_us: str = Field(..., alias='es-us')
    es_uy: str = Field(..., alias='es-uy')
    es_ve: str = Field(..., alias='es-ve')
    es_xl: str = Field(..., alias='es-xl')
    fi_ax: str = Field(..., alias='fi-ax')
    fi_fi: str = Field(..., alias='fi-fi')
    fr_ad: str = Field(..., alias='fr-ad')
    fr_be: str = Field(..., alias='fr-be')
    fr_bl: str = Field(..., alias='fr-bl')
    fr_ca: str = Field(..., alias='fr-ca')
    fr_ch: str = Field(..., alias='fr-ch')
    fr_fr: str = Field(..., alias='fr-fr')
    fr_gf: str = Field(..., alias='fr-gf')
    fr_gp: str = Field(..., alias='fr-gp')
    fr_ht: str = Field(..., alias='fr-ht')
    fr_lu: str = Field(..., alias='fr-lu')
    fr_mc: str = Field(..., alias='fr-mc')
    fr_mf: str = Field(..., alias='fr-mf')
    fr_mq: str = Field(..., alias='fr-mq')
    fr_mu: str = Field(..., alias='fr-mu')
    fr_nc: str = Field(..., alias='fr-nc')
    fr_pf: str = Field(..., alias='fr-pf')
    fr_pm: str = Field(..., alias='fr-pm')
    fr_re: str = Field(..., alias='fr-re')
    fr_sx: str = Field(..., alias='fr-sx')
    fr_tf: str = Field(..., alias='fr-tf')
    fr_wf: str = Field(..., alias='fr-wf')
    fr_yt: str = Field(..., alias='fr-yt')
    he_il: str = Field(..., alias='he-il')
    hr_ba: str = Field(..., alias='hr-ba')
    hr_hr: str = Field(..., alias='hr-hr')
    hu_hu: str = Field(..., alias='hu-hu')
    id_id: str = Field(..., alias='id-id')
    it_ch: str = Field(..., alias='it-ch')
    it_it: str = Field(..., alias='it-it')
    it_sm: str = Field(..., alias='it-sm')
    it_va: str = Field(..., alias='it-va')
    ja_jp: str = Field(..., alias='ja-jp')
    ko_kr: str = Field(..., alias='ko-kr')
    ms_my: str = Field(..., alias='ms-my')
    nb_no: str = Field(..., alias='nb-no')
    no_no: str = Field(..., alias='no-no')
    nb_sj: str = Field(..., alias='nb-sj')
    nl_aw: str = Field(..., alias='nl-aw')
    nl_be: str = Field(..., alias='nl-be')
    nl_bq: str = Field(..., alias='nl-bq')
    nl_cw: str = Field(..., alias='nl-cw')
    nl_nl: str = Field(..., alias='nl-nl')
    nl_sr: str = Field(..., alias='nl-sr')
    nl_sx: str = Field(..., alias='nl-sx')
    pl_pl: str = Field(..., alias='pl-pl')
    pt_br: str = Field(..., alias='pt-br')
    pt_pt: str = Field(..., alias='pt-pt')
    ro_ro: str = Field(..., alias='ro-ro')
    sk_sk: str = Field(..., alias='sk-sk')
    sv_ax: str = Field(..., alias='sv-ax')
    sv_fi: str = Field(..., alias='sv-fi')
    sv_se: str = Field(..., alias='sv-se')
    th_th: str = Field(..., alias='th-th')
    tr_tr: str = Field(..., alias='tr-tr')
    vi_vn: str = Field(..., alias='vi-vn')
    zh_hk: str = Field(..., alias='zh-hk')
    zh_sg: str = Field(..., alias='zh-sg')
    zh_tw: str = Field(..., alias='zh-tw')

class AnnualStandaloneHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class AnnualStandaloneToggle(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class AnnualStarPlus(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class BundleDefault(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class BundleNoah(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class BundleNoahHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class BundleSash(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class BundleSashHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class CancelSubscription(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class ComboPlus(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class CraveBundlePremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class CraveBundleStandardWithAds(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class DisneyHulu(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipAdsBundleAddOns(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipAdsBundleBilling(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipAdsBundleBillingOfferId(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipAdsBundleBillingOfferId2(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipAdsBundleBillingOfferId3(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipAdsBundleBillingOfferId4(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipBundlePremiumRetailWildcat(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipBundlePremiumWildcat(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipBundlePromoWildcat(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipBundleRetailWildcat(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipNoAdsBundleAddOns(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class FlagshipNoAdsBundleBilling(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class Login(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MaxAdsBundleAddOns(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MaxAdsBundleflagship(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MaxBundleBasic(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MaxBundlePremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MaxNoAdsBundleAddOns(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MaxNoAdsBundleflagship(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MonthlyStandalone(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MonthlyStandaloneHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MonthlyStandaloneNoah(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MonthlyStandaloneSash(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class MonthlyStandaloneToggle(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class PlanSelectCommercePlans(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class PlanSelectIdentitySignup(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class Signup1(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class TsnBundleStandardWithAds(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class TsnBundleStandardNoAds(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class TsnBundlePremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class TsnCraveBundleStandardWithAds(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class TsnCraveBundlePremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufAnnualStandalonePremiumCo(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufAnnualStandalonePremiumHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufAnnualStandalonePremiumToggle(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufAnnualStandaloneStandardCo(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufBundlePremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufBundlePremiumHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufBundleTrioBasic(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufBundleTrioBasicDefault(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufBundleTrioBasicHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDisneyAnnualStandardHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDisneyAnnualStandardToggle(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDisneyMonthlyBasic(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDisneyMonthlyPremiumToggle(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDisneyMonthlyStandardHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDisneyMonthlyStandardToggle(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDuoBasic(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufDuoPremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufLogin(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufMonthlyStandalone(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufMonthlyStandaloneBasic(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufMonthlyStandalonePremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufMonthlyStandalonePremiumHidden(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufMonthlyStandalonePremiumToggle(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class UsufSignup(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class VenuBundleBasic(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class VenuBundlePremium(BaseModel):
    url: str
    glimpse_name: str = Field(..., alias='glimpseName')

class CannonballLinkManager1(BaseModel):
    annual_standalone_hidden: AnnualStandaloneHidden = Field(..., alias='annualStandaloneHidden')
    annual_standalone_toggle: AnnualStandaloneToggle = Field(..., alias='annualStandaloneToggle')
    annual_star_plus: AnnualStarPlus = Field(..., alias='annualStarPlus')
    bundle_default: BundleDefault = Field(..., alias='bundleDefault')
    bundle_noah: BundleNoah = Field(..., alias='bundleNoah')
    bundle_noah_hidden: BundleNoahHidden = Field(..., alias='bundleNoahHidden')
    bundle_sash: BundleSash = Field(..., alias='bundleSash')
    bundle_sash_hidden: BundleSashHidden = Field(..., alias='bundleSashHidden')
    cancel_subscription: CancelSubscription = Field(..., alias='cancelSubscription')
    combo_plus: ComboPlus = Field(..., alias='comboPlus')
    crave_bundle_premium: CraveBundlePremium = Field(..., alias='craveBundlePremium')
    crave_bundle_standard_with_ads: CraveBundleStandardWithAds = Field(..., alias='craveBundleStandardWithAds')
    disney_hulu: DisneyHulu = Field(..., alias='disneyHulu')
    flagship_ads_bundle_add_ons: FlagshipAdsBundleAddOns = Field(..., alias='flagshipAdsBundleAddOns')
    flagship_ads_bundle_billing: FlagshipAdsBundleBilling = Field(..., alias='flagshipAdsBundleBilling')
    flagship_ads_bundle_billing_offer_id: FlagshipAdsBundleBillingOfferId = Field(..., alias='flagshipAdsBundleBillingOfferId')
    flagship_ads_bundle_billing_offer_id2: FlagshipAdsBundleBillingOfferId2 = Field(..., alias='flagshipAdsBundleBillingOfferId2')
    flagship_ads_bundle_billing_offer_id3: FlagshipAdsBundleBillingOfferId3 = Field(..., alias='flagshipAdsBundleBillingOfferId3')
    flagship_ads_bundle_billing_offer_id4: FlagshipAdsBundleBillingOfferId4 = Field(..., alias='flagshipAdsBundleBillingOfferId4')
    flagship_bundle_premium_retail_wildcat: FlagshipBundlePremiumRetailWildcat = Field(..., alias='flagshipBundlePremiumRetailWildcat')
    flagship_bundle_premium_wildcat: FlagshipBundlePremiumWildcat = Field(..., alias='flagshipBundlePremiumWildcat')
    flagship_bundle_promo_wildcat: FlagshipBundlePromoWildcat = Field(..., alias='flagshipBundlePromoWildcat')
    flagship_bundle_retail_wildcat: FlagshipBundleRetailWildcat = Field(..., alias='flagshipBundleRetailWildcat')
    flagship_no_ads_bundle_add_ons: FlagshipNoAdsBundleAddOns = Field(..., alias='flagshipNoAdsBundleAddOns')
    flagship_no_ads_bundle_billing: FlagshipNoAdsBundleBilling = Field(..., alias='flagshipNoAdsBundleBilling')
    login: Login
    max_ads_bundle_add_ons: MaxAdsBundleAddOns = Field(..., alias='maxAdsBundleAddOns')
    max_ads_bundleflagship: MaxAdsBundleflagship = Field(..., alias='maxAdsBundleflagship')
    max_bundle_basic: MaxBundleBasic = Field(..., alias='maxBundleBasic')
    max_bundle_premium: MaxBundlePremium = Field(..., alias='maxBundlePremium')
    max_no_ads_bundle_add_ons: MaxNoAdsBundleAddOns = Field(..., alias='maxNoAdsBundleAddOns')
    max_no_ads_bundleflagship: MaxNoAdsBundleflagship = Field(..., alias='maxNoAdsBundleflagship')
    monthly_standalone: MonthlyStandalone = Field(..., alias='monthlyStandalone')
    monthly_standalone_hidden: MonthlyStandaloneHidden = Field(..., alias='monthlyStandaloneHidden')
    monthly_standalone_noah: MonthlyStandaloneNoah = Field(..., alias='monthlyStandaloneNoah')
    monthly_standalone_sash: MonthlyStandaloneSash = Field(..., alias='monthlyStandaloneSash')
    monthly_standalone_toggle: MonthlyStandaloneToggle = Field(..., alias='monthlyStandaloneToggle')
    plan_select_commerce_plans: PlanSelectCommercePlans = Field(..., alias='planSelectCommercePlans')
    plan_select_identity_signup: PlanSelectIdentitySignup = Field(..., alias='planSelectIdentitySignup')
    signup: Signup1
    tsn_bundle_standard_with_ads: TsnBundleStandardWithAds = Field(..., alias='tsnBundleStandardWithAds')
    tsn_bundle_standard_no_ads: TsnBundleStandardNoAds = Field(..., alias='tsnBundleStandardNoAds')
    tsn_bundle_premium: TsnBundlePremium = Field(..., alias='tsnBundlePremium')
    tsn_crave_bundle_standard_with_ads: TsnCraveBundleStandardWithAds = Field(..., alias='tsnCraveBundleStandardWithAds')
    tsn_crave_bundle_premium: TsnCraveBundlePremium = Field(..., alias='tsnCraveBundlePremium')
    usuf_annual_standalone_premium_co: UsufAnnualStandalonePremiumCo = Field(..., alias='usufAnnualStandalonePremiumCO')
    usuf_annual_standalone_premium_hidden: UsufAnnualStandalonePremiumHidden = Field(..., alias='usufAnnualStandalonePremiumHidden')
    usuf_annual_standalone_premium_toggle: UsufAnnualStandalonePremiumToggle = Field(..., alias='usufAnnualStandalonePremiumToggle')
    usuf_annual_standalone_standard_co: UsufAnnualStandaloneStandardCo = Field(..., alias='usufAnnualStandaloneStandardCO')
    usuf_bundle_premium: UsufBundlePremium = Field(..., alias='usufBundlePremium')
    usuf_bundle_premium_hidden: UsufBundlePremiumHidden = Field(..., alias='usufBundlePremiumHidden')
    usuf_bundle_trio_basic: UsufBundleTrioBasic = Field(..., alias='usufBundleTrioBasic')
    usuf_bundle_trio_basic_default: UsufBundleTrioBasicDefault = Field(..., alias='usufBundleTrioBasicDefault')
    usuf_bundle_trio_basic_hidden: UsufBundleTrioBasicHidden = Field(..., alias='usufBundleTrioBasicHidden')
    usuf_disney_annual_standard_hidden: UsufDisneyAnnualStandardHidden = Field(..., alias='usufDisneyAnnualStandardHidden')
    usuf_disney_annual_standard_toggle: UsufDisneyAnnualStandardToggle = Field(..., alias='usufDisneyAnnualStandardToggle')
    usuf_disney_monthly_basic: UsufDisneyMonthlyBasic = Field(..., alias='usufDisneyMonthlyBasic')
    usuf_disney_monthly_premium_toggle: UsufDisneyMonthlyPremiumToggle = Field(..., alias='usufDisneyMonthlyPremiumToggle')
    usuf_disney_monthly_standard_hidden: UsufDisneyMonthlyStandardHidden = Field(..., alias='usufDisneyMonthlyStandardHidden')
    usuf_disney_monthly_standard_toggle: UsufDisneyMonthlyStandardToggle = Field(..., alias='usufDisneyMonthlyStandardToggle')
    usuf_duo_basic: UsufDuoBasic = Field(..., alias='usufDuoBasic')
    usuf_duo_premium: UsufDuoPremium = Field(..., alias='usufDuoPremium')
    usuf_login: UsufLogin = Field(..., alias='usufLogin')
    usuf_monthly_standalone: UsufMonthlyStandalone = Field(..., alias='usufMonthlyStandalone')
    usuf_monthly_standalone_basic: UsufMonthlyStandaloneBasic = Field(..., alias='usufMonthlyStandaloneBasic')
    usuf_monthly_standalone_premium: UsufMonthlyStandalonePremium = Field(..., alias='usufMonthlyStandalonePremium')
    usuf_monthly_standalone_premium_hidden: UsufMonthlyStandalonePremiumHidden = Field(..., alias='usufMonthlyStandalonePremiumHidden')
    usuf_monthly_standalone_premium_toggle: UsufMonthlyStandalonePremiumToggle = Field(..., alias='usufMonthlyStandalonePremiumToggle')
    usuf_signup: UsufSignup = Field(..., alias='usufSignup')
    venu_bundle_basic: VenuBundleBasic = Field(..., alias='venuBundleBasic')
    venu_bundle_premium: VenuBundlePremium = Field(..., alias='venuBundlePremium')

class Paths(BaseModel):
    stage: str
    stage_preview: str = Field(..., alias='stagePreview')
    prod: str
    preview: str

class Lps(BaseModel):
    environment: str
    organization: str
    space: str
    available_environments: list[str] = Field(..., alias='availableEnvironments')

class Explore(BaseModel):
    environment: str
    organization: str
    space: str
    available_environments: list[str] = Field(..., alias='availableEnvironments')

class ExploreFamily(BaseModel):
    environment: str
    organization: str
    space: str
    available_environments: list[str] = Field(..., alias='availableEnvironments')

class Instances(BaseModel):
    lps: Lps
    explore: Explore
    explore_family: ExploreFamily = Field(..., alias='exploreFamily')

class Cannonball(BaseModel):
    cdn_manifest_domain: str = Field(..., alias='cdnManifestDomain')
    preview_manifest_domain: str = Field(..., alias='previewManifestDomain')
    environment: str
    organization: str
    space: str
    paths: Paths
    instances: Instances

class Paths1(BaseModel):
    stage: str
    prod: str
    preview: str
    stage_preview: str = Field(..., alias='stagePreview')

class Explore1(BaseModel):
    organization: str
    space: str
    environment: str
    available_environments: list[str] = Field(..., alias='availableEnvironments')

class Global(BaseModel):
    organization: str
    space: str
    environment: str
    available_environments: list[str] = Field(..., alias='availableEnvironments')

class Instances1(BaseModel):
    explore: Explore1
    global_: Global = Field(..., alias='global')
    lps: Lps
    explore_family: ExploreFamily = Field(..., alias='exploreFamily')

class Spaceball(BaseModel):
    paths: Paths1
    instances: Instances1

class Af1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing152(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Purchase85(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class DefaultProduct84(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce134(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct84 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Au1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing152
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')
    commerce: Commerce134

class Bd1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Bn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Bt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Bu1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing153(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig138(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Commerce135(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cc1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing153
    feature_config: FeatureConfig138 = Field(..., alias='featureConfig')
    commerce: Commerce135

class Commerce136(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ck1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing153
    feature_config: FeatureConfig138 = Field(..., alias='featureConfig')
    commerce: Commerce136

class Cn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Fj1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing155(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig140(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct85(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce137(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct85 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Hk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing155
    feature_config: FeatureConfig140 = Field(..., alias='featureConfig')
    commerce: Commerce137

class Hm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Id1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing155

class In1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct86(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce138(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct86 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Jp1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing155
    feature_config: FeatureConfig140 = Field(..., alias='featureConfig')
    commerce: Commerce138

class Kh1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ki1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig142(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')
    enable_age_verification: bool = Field(..., alias='enableAgeVerification')
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct87(BaseModel):
    nu: Nu5 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce139(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    card_options_popover_enabled: bool = Field(..., alias='cardOptionsPopoverEnabled')
    default_product: DefaultProduct87 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    minimum_age_to_subscribe: int = Field(..., alias='minimumAgeToSubscribe')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Kr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing155
    feature_config: FeatureConfig142 = Field(..., alias='featureConfig')
    commerce: Commerce139

class La1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Lk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mo1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mv1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class My1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing155

class Marketing160(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig143(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Commerce140(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Nf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing160
    feature_config: FeatureConfig143 = Field(..., alias='featureConfig')
    commerce: Commerce140

class Np1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Nr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce141(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Nu89(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing160
    feature_config: FeatureConfig143 = Field(..., alias='featureConfig')
    commerce: Commerce141

class Marketing162(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Nu90(BaseModel):
    campaign_code: str = Field(..., alias='campaignCode')
    sku_list: list[str] = Field(..., alias='skuList')
    voucher_code: str = Field(..., alias='voucherCode')

class DefaultProduct88(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce142(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct88 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Nz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing162
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')
    commerce: Commerce142

class Pg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ph1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing162

class Pk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sb1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig145(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')

class DefaultProduct89(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce143(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct89 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Sg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing162
    feature_config: FeatureConfig145 = Field(..., alias='featureConfig')
    commerce: Commerce143

class Th1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing162

class Marketing166(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig146(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Commerce144(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing166
    feature_config: FeatureConfig146 = Field(..., alias='featureConfig')
    commerce: Commerce144

class Tl1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class To1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Tp1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Tv2(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing167(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig147(BaseModel):
    display_rights_reserved_year: bool = Field(..., alias='displayRightsReservedYear')
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct90(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce145(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct90 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_e_guid: bool = Field(..., alias='requiresEGuid')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing167
    feature_config: FeatureConfig147 = Field(..., alias='featureConfig')
    commerce: Commerce145

class Vn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Vu1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ws1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig148(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct91(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce146(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct91 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ad1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing167
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce146

class Ae1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing167
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')

class Commerce147(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ai1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing167
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce147

class DefaultProduct92(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce148(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct92 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Al1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing167
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce148

class Am1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class An1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ao1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct93(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce149(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct93 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class At1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing167
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce149

class Commerce150(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Aw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing167
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce150

class Marketing174(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce151(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ax1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing174
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce151

class Marketing175(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct94(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce152(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct94 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ba1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing175
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce152

class DefaultProduct95(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce153(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct95 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Be1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing175
    feature_config: FeatureConfig148 = Field(..., alias='featureConfig')
    commerce: Commerce153

class Bf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig157(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class DefaultProduct96(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce154(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    local_price_enabled: bool = Field(..., alias='localPriceEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct96 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing175
    feature_config: FeatureConfig157 = Field(..., alias='featureConfig')
    commerce: Commerce154

class Bh1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing175

class Bi1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Bj1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing179(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig158(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Commerce155(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Bl1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing179
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce155

class Marketing180(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce156(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing180
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce156

class Commerce157(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bq1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing180
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce157

class Bv1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')

class Bw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cd1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cq1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct97(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce158(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct97 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ch1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing180
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce158

class Ci1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Cs1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')

class Cv1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce159(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing180
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce159

class Marketing184(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce160(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cx1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing184
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce160

class Cy1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')

class Marketing185(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct98(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce161(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct98 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing185
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce161

class DefaultProduct99(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce162(BaseModel):
    annual_auto_downgrade: bool = Field(..., alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct99 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow = Field(..., alias='regulatedCancelFlow')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool = Field(..., alias='requiresAdditionalSADisclaimer')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class De1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing185
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce162

class Dj1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct100(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce163(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct100 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Dk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing185
    feature_config: FeatureConfig158 = Field(..., alias='featureConfig')
    commerce: Commerce163

class Dz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing185

class FeatureConfig170(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class DefaultProduct101(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce164(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct101 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ee1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing185
    feature_config: FeatureConfig170 = Field(..., alias='featureConfig')
    commerce: Commerce164

class FeatureConfig171(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Eg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing185
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')

class Eh1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Er1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct102(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce165(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct102 = Field(..., alias='defaultProduct')
    disable_province_dropdown: bool = Field(..., alias='disableProvinceDropdown')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Es1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing185
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce165

class Et1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct103(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce166(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct103 = Field(..., alias='defaultProduct')
    disable_province_dropdown: bool = Field(..., alias='disableProvinceDropdown')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Fi1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing185
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce166

class Commerce167(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Fk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing185
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce167

class Marketing194(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce168(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Fo1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing194
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce168

class Marketing195(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct104(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce169(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct104 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow = Field(..., alias='regulatedCancelFlow')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool = Field(..., alias='requiresAdditionalSADisclaimer')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Fr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing195
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce169

class Fx1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ga1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct105(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce170(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct105 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gb1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing195
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce170

class Marketing197(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce171(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Gf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing197
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce171

class Commerce172(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Gg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing197
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce172

class Gh1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce173(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Gi1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing197
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce173

class Marketing200(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct106(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce174(BaseModel):
    default_product: DefaultProduct106 = Field(..., alias='defaultProduct')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Gl1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing200
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce174

class Gm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Gn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing201(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce175(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Gp1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing201
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce175

class Gq1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing202(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct107(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce176(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct107 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing202
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce176

class Commerce177(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gs1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing202
    feature_config: FeatureConfig171 = Field(..., alias='featureConfig')
    commerce: Commerce177

class Gw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig185(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class DefaultProduct108(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce178(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct108 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Hr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing202
    feature_config: FeatureConfig185 = Field(..., alias='featureConfig')
    commerce: Commerce178

class FeatureConfig186(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct109(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce179(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct109 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Hu1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing202
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce179

class DefaultProduct110(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce180(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct110 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ie1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing202
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce180

class Il1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing202

class Marketing208(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce181(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Im1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing208
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce181

class Commerce182(BaseModel):
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Io1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing208
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce182

class Marketing210(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Iq1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing210

class Ir1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct111(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce183(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct111 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Is1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing210
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce183

class DefaultProduct112(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce184(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct112 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class It1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing210
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce184

class Marketing213(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce185(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Je1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing213
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce185

class Marketing214(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Jo1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing214

class Ke1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Km1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Kw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing214
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')

class Commerce186(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ky1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing214
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce186

class Lb1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing214

class DefaultProduct113(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce187(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct113 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Li1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing214
    feature_config: FeatureConfig186 = Field(..., alias='featureConfig')
    commerce: Commerce187

class Lr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ls1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig196(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class DefaultProduct114(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce188(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct114 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Lt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing214
    feature_config: FeatureConfig196 = Field(..., alias='featureConfig')
    commerce: Commerce188

class FeatureConfig197(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct115(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce189(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct115 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Lu1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing214
    feature_config: FeatureConfig197 = Field(..., alias='featureConfig')
    commerce: Commerce189

class FeatureConfig198(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class DefaultProduct116(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce190(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct116 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Lv1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing214
    feature_config: FeatureConfig198 = Field(..., alias='featureConfig')
    commerce: Commerce190

class Ly1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ma1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing214

class Marketing223(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig199(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct117(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce191(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    default_product: DefaultProduct117 = Field(..., alias='defaultProduct')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mc1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing223
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce191

class Md1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing224(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct118(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce192(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct118 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Me1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing224
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce192

class Marketing225(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce193(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Mf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing225
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce193

class Mg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing226(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce194(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    sells_bundle: bool = Field(..., alias='sellsBundle')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mh1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing226
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce194

class DefaultProduct119(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce195(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct119 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing226
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce195

class Ml1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing228(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce196(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Mq1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing228
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce196

class Mr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing229(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce197(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ms1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing229
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce197

class DefaultProduct120(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce198(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct120 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing229
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce198

class Marketing231(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct121(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce199(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct121 = Field(..., alias='defaultProduct')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Mu1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing231
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce199

class Mw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Mz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Na1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce200(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Nc1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing231
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce200

class Ne1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ng1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing233(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct122(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce201(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct122 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    local_payment: LocalPayment = Field(..., alias='localPayment')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Nl1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing233
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce201

class DefaultProduct123(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce202(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct123 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class No1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing233
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce202

class Nt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Om1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing233

class Marketing236(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce203(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Pf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing236
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce203

class Marketing237(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct124(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce204(BaseModel):
    annual_auto_downgrade: bool = Field(..., alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct124 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pl1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing237
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce204

class Marketing238(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce205(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Pm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing238
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce205

class Commerce206(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Pn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing238
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce206

class Marketing240(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ps2(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing240

class DefaultProduct125(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce207(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct125 = Field(..., alias='defaultProduct')
    disable_province_dropdown: bool = Field(..., alias='disableProvinceDropdown')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing240
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce207

class Qa1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing240

class Marketing243(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce208(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Re1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing243
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce208

class Marketing244(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct126(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce209(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct126 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ro1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing244
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce209

class DefaultProduct127(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce210(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct127 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Rs1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing244
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce210

class Rw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sa1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing244
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')

class Sc1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct128(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce211(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct128 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Se1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing244
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce211

class Marketing248(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce212(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Sh1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing248
    feature_config: FeatureConfig199 = Field(..., alias='featureConfig')
    commerce: Commerce212

class Marketing249(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig222(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    cmp_enable_browser_lang: bool = Field(..., alias='cmpEnableBrowserLang')

class DefaultProduct129(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce213(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct129 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Si1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing249
    feature_config: FeatureConfig222 = Field(..., alias='featureConfig')
    commerce: Commerce213

class Marketing250(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig223(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Commerce214(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Sj1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing250
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce214

class Marketing251(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct130(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    portability: Portability
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce215(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct130 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Sk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing251
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce215

class Sl1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing252(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct131(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce216(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct131 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Sm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing252
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce216

class Sn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class So1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ss1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class St1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing253(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce217(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Sx1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing253
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce217

class Sy1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Sz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce218(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tc1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing253
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce218

class Td1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing255(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce219(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Tf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing255
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce219

class Tg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing256(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Tn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing256

class DefaultProduct132(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce220(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct132 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing256
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce220

class Tz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ua1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Ug1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing258(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Uk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing258
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')

class DefaultProduct133(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce221(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct133 = Field(..., alias='defaultProduct')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Va1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing258
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce221

class Marketing260(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce222(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Vg1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing260
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce222

class Marketing261(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce223(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Wf1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing261
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce223

class Commerce224(BaseModel):
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Xk1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')
    commerce: Commerce224

class Ye1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce225(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show3_ds_flow: bool = Field(..., alias='show3DSFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool = Field(..., alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')

class Yt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing261
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce225

class Yu1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Marketing263(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Za1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing263

class Zm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Zr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Zw1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct134(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce226(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct134 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ag1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce226

class DefaultProduct135(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce227(BaseModel):
    cancel_subscription_nav_item_promoted: CancelSubscriptionNavItemPromoted = Field(..., alias='cancelSubscriptionNavItemPromoted')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct135 = Field(..., alias='defaultProduct')
    is_one_step_cancel_billing_country: bool = Field(..., alias='isOneStepCancelBillingCountry')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_active_review: bool = Field(..., alias='requiresActiveReview')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ar1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce227

class DefaultProduct136(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce228(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct136 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bb1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce228

class DefaultProduct137(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce229(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct137 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bo1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig223 = Field(..., alias='featureConfig')
    commerce: Commerce229

class FeatureConfig239(BaseModel):
    display_additional_ratings: bool = Field(..., alias='displayAdditionalRatings')
    display_rating_advisories: bool = Field(..., alias='displayRatingAdvisories')
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct138(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce230(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct138 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    starz_play_supported_regions: bool = Field(..., alias='starzPlaySupportedRegions')

class Br1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig239 = Field(..., alias='featureConfig')
    commerce: Commerce230

class FeatureConfig240(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class DefaultProduct139(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce231(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct139 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bs1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce231

class DefaultProduct140(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce232(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct140 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Bz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce232

class DefaultProduct141(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce233(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct141 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cl1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce233

class DefaultProduct142(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce234(BaseModel):
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct142 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Co1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce234

class DefaultProduct143(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce235(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct143 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Cr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce235

class DefaultProduct144(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce236(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct144 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Dm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce236

class DefaultProduct145(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce237(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct145 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Do1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce237

class DefaultProduct146(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce238(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct146 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ec1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce238

class DefaultProduct147(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce239(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct147 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gd1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce239

class DefaultProduct148(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce240(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct148 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce240

class DefaultProduct149(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce241(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct149 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gy1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce241

class DefaultProduct150(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce242(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct150 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Hn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce242

class DefaultProduct151(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce243(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct151 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ht1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce243

class DefaultProduct152(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce244(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct152 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Jm1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce244

class DefaultProduct153(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce245(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct153 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Kn1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce245

class DefaultProduct154(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce246(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct154 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Lc1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce246

class DefaultProduct155(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce247(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct155 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')
    starz_play_supported_regions: bool = Field(..., alias='starzPlaySupportedRegions')

class Mx1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce247

class DefaultProduct156(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce248(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct156 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ni1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce248

class DefaultProduct157(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce249(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct157 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pa1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce249

class DefaultProduct158(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce250(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct158 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pe1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce250

class DefaultProduct159(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce251(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct159 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Py1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce251

class DefaultProduct160(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce252(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct160 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Sr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce252

class DefaultProduct161(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce253(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct161 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Sv1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce253

class DefaultProduct162(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce254(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct162 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Tt1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce254

class DefaultProduct163(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce255(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct163 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Uy1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce255

class DefaultProduct164(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce256(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct164 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Vc1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce256

class DefaultProduct165(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce257(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct165 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_forced_subscriber_agreement: bool = Field(..., alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool = Field(..., alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool = Field(..., alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool = Field(..., alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ve1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing263
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce257

class Marketing296(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce258(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class As1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing296
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce258

class Marketing297(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class DefaultProduct166(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Commerce259(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct166 = Field(..., alias='defaultProduct')
    license_plate_sign_up_url: str = Field(..., alias='licensePlateSignUpURL')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    promotional_offers: dict[str, Any] = Field(..., alias='promotionalOffers')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool = Field(..., alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Ca1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing297
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce259

class Marketing298(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce260(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Gu1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing298
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce260

class Commerce261(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Mp1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing298
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce261

class Commerce262(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Pr1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing298
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce262

class Marketing301(BaseModel):
    name: str
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')

class Commerce263(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    sells_bundle: bool = Field(..., alias='sellsBundle')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Um1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing301
    feature_config: FeatureConfig240 = Field(..., alias='featureConfig')
    commerce: Commerce263

class FeatureConfig273(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')
    enable_identity_consent_sync: bool = Field(..., alias='enableIdentityConsentSync')

class DefaultProduct167(BaseModel):
    nu: Nu90 = Field(..., alias='NU')
    change_payment: ChangePayment = Field(..., alias='changePayment')
    purchase: Purchase85
    un_auth: UnAuth = Field(..., alias='unAuth')

class Ps3(BaseModel):
    type: str
    url: str

class Tv3(BaseModel):
    type: str
    url: str

class LicensePlateFlowNavigation1(BaseModel):
    amazon: Amazon = Field(..., alias='AMAZON')
    cox: Cox
    hisense: Hisense
    lg: Lg
    ps: Ps3
    ps4: Ps4
    samsung: Samsung
    tivo_us: TivoUs
    tv: Tv3
    vizio: Vizio
    xbox: Xbox
    xglobal: Xglobal

class Ft1(BaseModel):
    nine_month: NineMonth = Field(..., alias='nineMonth')
    one_year: OneYear = Field(..., alias='oneYear')
    six_month: SixMonth = Field(..., alias='sixMonth')
    three_year: ThreeYear = Field(..., alias='threeYear')
    two_year: TwoYear = Field(..., alias='twoYear')

class Purchase169(BaseModel):
    nine_month: NineMonth = Field(..., alias='nineMonth')
    one_year: OneYear = Field(..., alias='oneYear')
    six_month: SixMonth = Field(..., alias='sixMonth')
    three_year: ThreeYear = Field(..., alias='threeYear')
    two_year: TwoYear = Field(..., alias='twoYear')

class Superbundle1(BaseModel):
    nine_month: NineMonth = Field(..., alias='nineMonth')
    one_year: OneYear = Field(..., alias='oneYear')
    six_month: SixMonth = Field(..., alias='sixMonth')

class RewardsProducts1(BaseModel):
    ft: Ft1 = Field(..., alias='FT')
    purchase: Purchase169
    superbundle: Superbundle1

class Commerce264(BaseModel):
    ads_tier_devices: AdsTierDevices = Field(..., alias='adsTierDevices')
    ads_tier_enabled: bool = Field(..., alias='adsTierEnabled')
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    card_options: list[str] = Field(..., alias='cardOptions')
    default_product: DefaultProduct167 = Field(..., alias='defaultProduct')
    devices_that_sell2_p_bundle: DevicesThatSell2PBundle = Field(..., alias='devicesThatSell2PBundle')
    devices_that_sell_bundle: DevicesThatSellBundle = Field(..., alias='devicesThatSellBundle')
    enable_global_identity_unbranded_create_account: bool = Field(..., alias='enableGlobalIdentityUnbrandedCreateAccount')
    license_plate_flow_navigation: LicensePlateFlowNavigation1 = Field(..., alias='licensePlateFlowNavigation')
    one_step_cancel_billing_states: list[str] = Field(..., alias='oneStepCancelBillingStates')
    payment_methods: list[str] = Field(..., alias='paymentMethods')
    paypal_client_id: str = Field(..., alias='paypalClientId')
    requires_annual_opt_in_states: list[str] = Field(..., alias='requiresAnnualOptInStates')
    restart_eligible_enabled: bool = Field(..., alias='restartEligibleEnabled')
    rewards_products: RewardsProducts1 = Field(..., alias='rewardsProducts')
    sells_bundle: bool = Field(..., alias='sellsBundle')
    show_commerce_flex_account_offer: bool = Field(..., alias='showCommerceFlexAccountOffer')
    show_commerce_unified_cancel_flow: bool = Field(..., alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Us1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    footer: list[str]
    marketing: Marketing301
    feature_config: FeatureConfig273 = Field(..., alias='featureConfig')
    commerce: Commerce264

class Marketing303(BaseModel):
    name: str
    lang: str
    enable_parent_country_languages: bool = Field(..., alias='enableParentCountryLanguages')
    region_languages: list[str] = Field(..., alias='regionLanguages')

class FeatureConfig274(BaseModel):
    enable_cmp: bool = Field(..., alias='enableCMP')

class Commerce265(BaseModel):
    braintree_paypal_enabled: bool = Field(..., alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool = Field(..., alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool = Field(..., alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool = Field(..., alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool = Field(..., alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct = Field(..., alias='specialOfferProduct')

class Vi1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    parent_country: str = Field(..., alias='parentCountry')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    marketing: Marketing303
    feature_config: FeatureConfig274 = Field(..., alias='featureConfig')
    commerce: Commerce265

class Yz1(BaseModel):
    is_eu: bool = Field(..., alias='isEU')
    name: str
    group: str
    has_launched: bool = Field(..., alias='hasLaunched')
    lang: str
    region_languages: list[str] = Field(..., alias='regionLanguages')
    feature_config: dict[str, Any] = Field(..., alias='featureConfig')

class CountriesConfig(BaseModel):
    af: Af1 = Field(..., alias='AF')
    au: Au1 = Field(..., alias='AU')
    bd: Bd1 = Field(..., alias='BD')
    bn: Bn1 = Field(..., alias='BN')
    bt: Bt1 = Field(..., alias='BT')
    bu: Bu1 = Field(..., alias='BU')
    cc: Cc1 = Field(..., alias='CC')
    ck: Ck1 = Field(..., alias='CK')
    cn: Cn1 = Field(..., alias='CN')
    fj: Fj1 = Field(..., alias='FJ')
    hk: Hk1 = Field(..., alias='HK')
    hm: Hm1 = Field(..., alias='HM')
    id: Id1 = Field(..., alias='ID')
    in_: In1 = Field(..., alias='IN')
    jp: Jp1 = Field(..., alias='JP')
    kh: Kh1 = Field(..., alias='KH')
    ki: Ki1 = Field(..., alias='KI')
    kr: Kr1 = Field(..., alias='KR')
    la: La1 = Field(..., alias='LA')
    lk: Lk1 = Field(..., alias='LK')
    mm: Mm1 = Field(..., alias='MM')
    mo: Mo1 = Field(..., alias='MO')
    mv: Mv1 = Field(..., alias='MV')
    my: My1 = Field(..., alias='MY')
    nf: Nf1 = Field(..., alias='NF')
    np: Np1 = Field(..., alias='NP')
    nr: Nr1 = Field(..., alias='NR')
    nu: Nu89 = Field(..., alias='NU')
    nz: Nz1 = Field(..., alias='NZ')
    pg: Pg1 = Field(..., alias='PG')
    ph: Ph1 = Field(..., alias='PH')
    pk: Pk1 = Field(..., alias='PK')
    sb: Sb1 = Field(..., alias='SB')
    sg: Sg1 = Field(..., alias='SG')
    th: Th1 = Field(..., alias='TH')
    tk: Tk1 = Field(..., alias='TK')
    tl: Tl1 = Field(..., alias='TL')
    to: To1 = Field(..., alias='TO')
    tp: Tp1 = Field(..., alias='TP')
    tv: Tv2 = Field(..., alias='TV')
    tw: Tw1 = Field(..., alias='TW')
    vn: Vn1 = Field(..., alias='VN')
    vu: Vu1 = Field(..., alias='VU')
    ws: Ws1 = Field(..., alias='WS')
    ad: Ad1 = Field(..., alias='AD')
    ae: Ae1 = Field(..., alias='AE')
    ai: Ai1 = Field(..., alias='AI')
    al: Al1 = Field(..., alias='AL')
    am: Am1 = Field(..., alias='AM')
    an: An1 = Field(..., alias='AN')
    ao: Ao1 = Field(..., alias='AO')
    at: At1 = Field(..., alias='AT')
    aw: Aw1 = Field(..., alias='AW')
    ax: Ax1 = Field(..., alias='AX')
    ba: Ba1 = Field(..., alias='BA')
    be: Be1 = Field(..., alias='BE')
    bf: Bf1 = Field(..., alias='BF')
    bg: Bg1 = Field(..., alias='BG')
    bh: Bh1 = Field(..., alias='BH')
    bi: Bi1 = Field(..., alias='BI')
    bj: Bj1 = Field(..., alias='BJ')
    bl: Bl1 = Field(..., alias='BL')
    bm: Bm1 = Field(..., alias='BM')
    bq: Bq1 = Field(..., alias='BQ')
    bv: Bv1 = Field(..., alias='BV')
    bw: Bw1 = Field(..., alias='BW')
    cd: Cd1 = Field(..., alias='CD')
    cf: Cf1 = Field(..., alias='CF')
    cq: Cq1 = Field(..., alias='CQ')
    ch: Ch1 = Field(..., alias='CH')
    ci: Ci1 = Field(..., alias='CI')
    cm: Cm1 = Field(..., alias='CM')
    cs: Cs1 = Field(..., alias='CS')
    cv: Cv1 = Field(..., alias='CV')
    cw: Cw1 = Field(..., alias='CW')
    cx: Cx1 = Field(..., alias='CX')
    cy: Cy1 = Field(..., alias='CY')
    cz: Cz1 = Field(..., alias='CZ')
    de: De1 = Field(..., alias='DE')
    dj: Dj1 = Field(..., alias='DJ')
    dk: Dk1 = Field(..., alias='DK')
    dz: Dz1 = Field(..., alias='DZ')
    ee: Ee1 = Field(..., alias='EE')
    eg: Eg1 = Field(..., alias='EG')
    eh: Eh1 = Field(..., alias='EH')
    er: Er1 = Field(..., alias='ER')
    es: Es1 = Field(..., alias='ES')
    et: Et1 = Field(..., alias='ET')
    fi: Fi1 = Field(..., alias='FI')
    fk: Fk1 = Field(..., alias='FK')
    fo: Fo1 = Field(..., alias='FO')
    fr: Fr1 = Field(..., alias='FR')
    fx: Fx1 = Field(..., alias='FX')
    ga: Ga1 = Field(..., alias='GA')
    gb: Gb1 = Field(..., alias='GB')
    gf: Gf1 = Field(..., alias='GF')
    gg: Gg1 = Field(..., alias='GG')
    gh: Gh1 = Field(..., alias='GH')
    gi: Gi1 = Field(..., alias='GI')
    gl: Gl1 = Field(..., alias='GL')
    gm: Gm1 = Field(..., alias='GM')
    gn: Gn1 = Field(..., alias='GN')
    gp: Gp1 = Field(..., alias='GP')
    gq: Gq1 = Field(..., alias='GQ')
    gr: Gr1 = Field(..., alias='GR')
    gs: Gs1 = Field(..., alias='GS')
    gw: Gw1 = Field(..., alias='GW')
    hr: Hr1 = Field(..., alias='HR')
    hu: Hu1 = Field(..., alias='HU')
    ie: Ie1 = Field(..., alias='IE')
    il: Il1 = Field(..., alias='IL')
    im: Im1 = Field(..., alias='IM')
    io: Io1 = Field(..., alias='IO')
    iq: Iq1 = Field(..., alias='IQ')
    ir: Ir1 = Field(..., alias='IR')
    is_: Is1 = Field(..., alias='IS')
    it: It1 = Field(..., alias='IT')
    je: Je1 = Field(..., alias='JE')
    jo: Jo1 = Field(..., alias='JO')
    ke: Ke1 = Field(..., alias='KE')
    km: Km1 = Field(..., alias='KM')
    kw: Kw1 = Field(..., alias='KW')
    ky: Ky1 = Field(..., alias='KY')
    lb: Lb1 = Field(..., alias='LB')
    li: Li1 = Field(..., alias='LI')
    lr: Lr1 = Field(..., alias='LR')
    ls: Ls1 = Field(..., alias='LS')
    lt: Lt1 = Field(..., alias='LT')
    lu: Lu1 = Field(..., alias='LU')
    lv: Lv1 = Field(..., alias='LV')
    ly: Ly1 = Field(..., alias='LY')
    ma: Ma1 = Field(..., alias='MA')
    mc: Mc1 = Field(..., alias='MC')
    md: Md1 = Field(..., alias='MD')
    me: Me1 = Field(..., alias='ME')
    mf: Mf1 = Field(..., alias='MF')
    mg: Mg1 = Field(..., alias='MG')
    mh: Mh1 = Field(..., alias='MH')
    mk: Mk1 = Field(..., alias='MK')
    ml: Ml1 = Field(..., alias='ML')
    mq: Mq1 = Field(..., alias='MQ')
    mr: Mr1 = Field(..., alias='MR')
    ms: Ms1 = Field(..., alias='MS')
    mt: Mt1 = Field(..., alias='MT')
    mu: Mu1 = Field(..., alias='MU')
    mw: Mw1 = Field(..., alias='MW')
    mz: Mz1 = Field(..., alias='MZ')
    na: Na1 = Field(..., alias='NA')
    nc: Nc1 = Field(..., alias='NC')
    ne: Ne1 = Field(..., alias='NE')
    ng: Ng1 = Field(..., alias='NG')
    nl: Nl1 = Field(..., alias='NL')
    no: No1 = Field(..., alias='NO')
    nt: Nt1 = Field(..., alias='NT')
    om: Om1 = Field(..., alias='OM')
    pf: Pf1 = Field(..., alias='PF')
    pl: Pl1 = Field(..., alias='PL')
    pm: Pm1 = Field(..., alias='PM')
    pn: Pn1 = Field(..., alias='PN')
    ps: Ps2 = Field(..., alias='PS')
    pt: Pt1 = Field(..., alias='PT')
    qa: Qa1 = Field(..., alias='QA')
    re: Re1 = Field(..., alias='RE')
    ro: Ro1 = Field(..., alias='RO')
    rs: Rs1 = Field(..., alias='RS')
    rw: Rw1 = Field(..., alias='RW')
    sa: Sa1 = Field(..., alias='SA')
    sc: Sc1 = Field(..., alias='SC')
    se: Se1 = Field(..., alias='SE')
    sh: Sh1 = Field(..., alias='SH')
    si: Si1 = Field(..., alias='SI')
    sj: Sj1 = Field(..., alias='SJ')
    sk: Sk1 = Field(..., alias='SK')
    sl: Sl1 = Field(..., alias='SL')
    sm: Sm1 = Field(..., alias='SM')
    sn: Sn1 = Field(..., alias='SN')
    so: So1 = Field(..., alias='SO')
    ss: Ss1 = Field(..., alias='SS')
    st: St1 = Field(..., alias='ST')
    sx: Sx1 = Field(..., alias='SX')
    sy: Sy1 = Field(..., alias='SY')
    sz: Sz1 = Field(..., alias='SZ')
    tc: Tc1 = Field(..., alias='TC')
    td: Td1 = Field(..., alias='TD')
    tf: Tf1 = Field(..., alias='TF')
    tg: Tg1 = Field(..., alias='TG')
    tn: Tn1 = Field(..., alias='TN')
    tr: Tr1 = Field(..., alias='TR')
    tz: Tz1 = Field(..., alias='TZ')
    ua: Ua1 = Field(..., alias='UA')
    ug: Ug1 = Field(..., alias='UG')
    uk: Uk1 = Field(..., alias='UK')
    va: Va1 = Field(..., alias='VA')
    vg: Vg1 = Field(..., alias='VG')
    wf: Wf1 = Field(..., alias='WF')
    xk: Xk1 = Field(..., alias='XK')
    ye: Ye1 = Field(..., alias='YE')
    yt: Yt1 = Field(..., alias='YT')
    yu: Yu1 = Field(..., alias='YU')
    za: Za1 = Field(..., alias='ZA')
    zm: Zm1 = Field(..., alias='ZM')
    zr: Zr1 = Field(..., alias='ZR')
    zw: Zw1 = Field(..., alias='ZW')
    ag: Ag1 = Field(..., alias='AG')
    ar: Ar1 = Field(..., alias='AR')
    bb: Bb1 = Field(..., alias='BB')
    bo: Bo1 = Field(..., alias='BO')
    br: Br1 = Field(..., alias='BR')
    bs: Bs1 = Field(..., alias='BS')
    bz: Bz1 = Field(..., alias='BZ')
    cl: Cl1 = Field(..., alias='CL')
    co: Co1 = Field(..., alias='CO')
    cr: Cr1 = Field(..., alias='CR')
    dm: Dm1 = Field(..., alias='DM')
    do: Do1 = Field(..., alias='DO')
    ec: Ec1 = Field(..., alias='EC')
    gd: Gd1 = Field(..., alias='GD')
    gt: Gt1 = Field(..., alias='GT')
    gy: Gy1 = Field(..., alias='GY')
    hn: Hn1 = Field(..., alias='HN')
    ht: Ht1 = Field(..., alias='HT')
    jm: Jm1 = Field(..., alias='JM')
    kn: Kn1 = Field(..., alias='KN')
    lc: Lc1 = Field(..., alias='LC')
    mx: Mx1 = Field(..., alias='MX')
    ni: Ni1 = Field(..., alias='NI')
    pa: Pa1 = Field(..., alias='PA')
    pe: Pe1 = Field(..., alias='PE')
    py: Py1 = Field(..., alias='PY')
    sr: Sr1 = Field(..., alias='SR')
    sv: Sv1 = Field(..., alias='SV')
    tt: Tt1 = Field(..., alias='TT')
    uy: Uy1 = Field(..., alias='UY')
    vc: Vc1 = Field(..., alias='VC')
    ve: Ve1 = Field(..., alias='VE')
    as_: As1 = Field(..., alias='AS')
    ca: Ca1 = Field(..., alias='CA')
    gu: Gu1 = Field(..., alias='GU')
    mp: Mp1 = Field(..., alias='MP')
    pr: Pr1 = Field(..., alias='PR')
    um: Um1 = Field(..., alias='UM')
    us: Us1 = Field(..., alias='US')
    vi: Vi1 = Field(..., alias='VI')
    yz: Yz1 = Field(..., alias='YZ')
    time_stamp: str = Field(..., alias='timeStamp')

class LangDisplayNames(BaseModel):
    ar: str
    bg: str
    cs: str
    da: str
    de: str
    el: str
    en: str
    es: str
    fi: str
    fr: str
    he: str
    hr: str
    hu: str
    id: str
    it: str
    ja: str
    ko: str
    ms: str
    nl: str
    nb: str
    pl: str
    pt: str
    ro: str
    sk: str
    sv: str
    th: str
    tr: str
    vi: str
    zh: str

class RemoteConfig(BaseModel):
    app_config: AppConfig = Field(..., alias='appConfig')
    dictionary_versions: DictionaryVersions = Field(..., alias='dictionaryVersions')
    path: Path
    remote_app_config: RemoteAppConfig = Field(..., alias='remoteAppConfig')
    version: str
    countries: Countries
    feature_config: FeatureConfig137 = Field(..., alias='featureConfig')
    app_lang_map: AppLangMap = Field(..., alias='appLangMap')
    cannonball_link_manager: CannonballLinkManager1 = Field(..., alias='cannonballLinkManager')
    cannonball: Cannonball
    spaceball: Spaceball
    archive_date: str = Field(..., alias='archiveDate')
    countries_config: CountriesConfig = Field(..., alias='countriesConfig')
    lang_display_names: LangDisplayNames = Field(..., alias='langDisplayNames')

class CannonballInstance(BaseModel):
    instance: str
    available_environments: list[str] = Field(..., alias='availableEnvironments')
    current_environment: str = Field(..., alias='currentEnvironment')

class Debug(BaseModel):
    cannonball_edit_url: str = Field(..., alias='cannonballEditUrl')
    entity_id: str = Field(..., alias='entityId')
    cannonball_instances: list[CannonballInstance] = Field(..., alias='cannonballInstances')
    common_available_environments: list[str] = Field(..., alias='commonAvailableEnvironments')

class PageProps(BaseModel):
    available_locales: list[str] = Field(..., alias='availableLocales')
    dictionary: Dictionary
    feature_flags: FeatureFlags = Field(..., alias='featureFlags')
    identity_sdk_config: IdentitySdkConfig = Field(..., alias='identitySDKConfig')
    stitch_document: StitchDocument = Field(..., alias='stitchDocument')
    page_id: str = Field(..., alias='pageId')
    metrics_data: MetricsData7 = Field(..., alias='metricsData')
    language: str
    region: str
    toast_cta_props: ToastCtaProps = Field(..., alias='toastCtaProps')
    remote_config: RemoteConfig = Field(..., alias='remoteConfig')
    pathname: str
    location: str
    disable_redirect: bool = Field(..., alias='disableRedirect')
    has_content: bool = Field(..., alias='hasContent')
    rtl_supported_locales: list[str] = Field(..., alias='rtlSupportedLocales')
    debug: Debug

class Props(BaseModel):
    page_props: PageProps = Field(..., alias='pageProps')
    field__n_ssp: bool = Field(..., alias='__N_SSP')

class Query(BaseModel):
    season: UUID | None = None
    slug: str

class PinnedPlatformOptions(BaseModel):
    pinned_platform_name: str = Field(..., alias='pinnedPlatformName')
    pinned_platform_version: str = Field(..., alias='pinnedPlatformVersion')

class RuntimeConfig(BaseModel):
    pinned_platform_options: PinnedPlatformOptions = Field(..., alias='pinnedPlatformOptions')
    git_commit: str = Field(..., alias='gitCommit')
    is_debug_tooling_enabled: bool = Field(..., alias='isDebugToolingEnabled')
    datadog_rum_env: str = Field(..., alias='datadogRUMEnv')
    datadog_rum_build_id: str = Field(..., alias='datadogRUMBuildId')
    datadog_service_name: str = Field(..., alias='datadogServiceName')
    remote_dictionaries_to_load: str = Field(..., alias='remoteDictionariesToLoad')

class EntityModel(BaseModel):
    props: Props
    page: str
    query: Query
    build_id: str = Field(..., alias='buildId')
    asset_prefix: str = Field(..., alias='assetPrefix')
    runtime_config: RuntimeConfig = Field(..., alias='runtimeConfig')
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
