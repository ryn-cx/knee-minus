from typing import Self
from pydantic import ModelWrapValidatorHandler, PrivateAttr, model_validator
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field
from typing import Any
from uuid import UUID

class Application(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    age_gate_denied_heading: str | None = None
    age_gate_denied_body: str | None = None
    age_gate_prompt_body: str | None = None
    age_gate_prompt_error: str | None = None
    article_back_to_top: str | None = None
    article_byline: str | None = None
    article_copy_link: str | None = None
    article_copy_to_clipboard_error: str | None = None
    article_copy_to_clipboard_success: str | None = None
    article_email_link: str | None = None
    article_revised: str | None = None
    article_share_link: str | None = None
    article_tags: str | None = None
    btn_choose_plan: str | None = None
    btn_login: str | None = None
    btn_ok_continue: str | None = None
    filter_and_sort_filters_label: str | None = None
    filter_and_sort_no_results: str | None = None
    filter_and_sort_no_results_sub: str | None = None
    filter_and_sort_reset: str | None = None
    filter_and_sort_sort_by: str | None = None
    d23countdownclock_days: str | None = None
    d23countdownclock_hours: str | None = None
    d23countdownclock_minutes: str | None = None
    d23countdownclock_seconds: str | None = None
    next_episode_episode_subtitle: str | None = None
    pagination_next: str | None = None
    pagination_previous: str | None = None
    pagination_show_all: str | None = None
    runtime_hours: str | None = None
    runtime_minutes: str | None = None
    search_placeholder: str | None = None
    unauthdetail_modal_copy: str | None = None
    unauthdetail_signupcta: str | None = None
    unauthdetail_you_may_also_like: str | None = None

class Accessibility(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    badge_label_event_live_tts: str | None = None
    btn_banner_web_close_tts: str | None = None
    btn_flip_card_close: str | None = None
    btn_flip_card_open: str | None = None
    btn_go_to_item_tts: str | None = None
    btn_live_modal_web_close_tts: str | None = None
    btn_nav_toggle_tts: str | None = None
    comp_chart_cell_feature_included_tts: str | None = None
    comp_chart_cell_feature_not_included_tts: str | None = None
    comp_chart_compare_plan_tts: str | None = None
    filter_and_sort_reset: str | None = None
    formerror_zipcode_invalid: str | None = None
    formerror_zipcode_required: str | None = None
    formlabel_submit: str | None = None
    formlabel_zipcode: str | None = None
    gallery_navigation_tts: str | None = None
    hero_gallery_tts: str | None = None
    index_number_generic: str | None = None
    pagination_next_tts: str | None = None
    pause: str | None = None
    plan_builder_reset_message: str | None = None
    play: str | None = None
    select_option_tts: str | None = None
    dropdown_season_label: str | None = None
    select_add_on_custom: str | None = None
    select_add_on: str | None = None
    skiptocontent_tts: str | None = None
    toast_close: str | None = None
    video_controls_pause: str | None = None
    video_controls_play: str | None = None

class Ratings(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    image_rating_kijkwijzer_12: str | None = None
    image_rating_kijkwijzer_16: str | None = None
    image_rating_kijkwijzer_6: str | None = None
    image_rating_kijkwijzer_9: str | None = None
    image_rating_kijkwijzer_al: str | None = None
    image_rating_mpaa_g: str | None = None
    image_rating_mpaa_nc_17: str | None = Field(None, alias='image_rating_mpaa_nc-17')
    image_rating_mpaa_pg: str | None = None
    image_rating_mpaa_pg_13: str | None = Field(None, alias='image_rating_mpaa_pg-13')
    image_rating_mpaa_r: str | None = None
    image_rating_ncs_g: str | None = None
    image_rating_ncs_m: str | None = None
    image_rating_ncs_ma15: str | None = None
    image_rating_ncs_pg: str | None = None
    image_rating_oflc_g: str | None = None
    image_rating_oflc_m: str | None = None
    image_rating_oflc_pg: str | None = None
    image_rating_oflc_r15: str | None = None
    image_rating_oflc_r16: str | None = None
    image_rating_oflc_rp13: str | None = None
    image_rating_oflc_rp16: str | None = None
    image_rating_tvpg_tv_14: str | None = Field(None, alias='image_rating_tvpg_tv-14')
    image_rating_tvpg_tv_g: str | None = Field(None, alias='image_rating_tvpg_tv-g')
    image_rating_tvpg_tv_ma: str | None = Field(None, alias='image_rating_tvpg_tv-ma')
    image_rating_tvpg_tv_pg: str | None = Field(None, alias='image_rating_tvpg_tv-pg')
    image_rating_tvpg_tv_y: str | None = Field(None, alias='image_rating_tvpg_tv-y')
    image_rating_tvpg_tv_y7: str | None = Field(None, alias='image_rating_tvpg_tv-y7')

class UnifiedCommerceOnboarding(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    next_landing_button1: str | None = None
    next_landing_button2: str | None = None
    next_landing_header: str | None = None
    next_landing_subhead: str | None = None

class Seo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    description_collection_brand: str | None = None
    title_collection_brand: str | None = None
    title_details_event: str | None = None
    title_details_movie: str | None = None
    title_details_series: str | None = None

class Dictionary(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    application: Application | None = None
    accessibility: Accessibility | None = None
    ratings: Ratings | None = None
    unified_commerce_onboarding: UnifiedCommerceOnboarding | None = Field(None, alias='unified-commerce-onboarding')
    seo: Seo | None = None

class FeatureFlags(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    block_datadog_rum: bool | None = Field(None, alias='blockDatadogRum')
    enable_identity_sdkv5: bool | None = Field(None, alias='enableIdentitySDKV5')
    enable_always_reload_on_consent_change: bool | None = Field(None, alias='enableAlwaysReloadOnConsentChange')

class IdentitySdkConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_id: str | None = Field(None, alias='clientId')
    enabled: bool | None = None
    environment: str | None = None
    rollout_percentage: int | None = Field(None, alias='rolloutPercentage')
    script_url: str | None = Field(None, alias='scriptUrl')
    flag: str | None = None
    enable_identity_sdkv5: bool | None = Field(None, alias='enableIdentitySDKV5')

class DefaultImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage(BaseModel):
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

class Child(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alt: str | None = None
    default_image: DefaultImage | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage | None = Field(None, alias='xsmallImage')
    small_image: SmallImage | None = Field(None, alias='smallImage')
    medium_image: MediumImage | None = Field(None, alias='mediumImage')
    large_image: LargeImage | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage | None = Field(None, alias='xxlargeImage')
    max_widths: MaxWidths | None = Field(None, alias='maxWidths')

class LeftItem(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    action_key: str | None = Field(None, alias='actionKey')
    children: list[Child] | None = None
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

class DefaultImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage1(BaseModel):
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
    default_image: DefaultImage1 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage1 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage1 | None = Field(None, alias='smallImage')
    medium_image: MediumImage1 | None = Field(None, alias='mediumImage')
    large_image: LargeImage1 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage1 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage1 | None = Field(None, alias='xxlargeImage')

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

class DefaultImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

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

class Child2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
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
    model_config = ConfigDict(extra='ignore', defer_build=True)
    desktop: int | None = None
    tablet: int | None = None
    mobile: int | None = None

class Child1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    alignments: Alignments | None = None
    footer: list[FooterItem] | None = None
    children: list[Child2] | None = None
    col_size: ColSize | None = Field(None, alias='colSize')
    gap: str | None = None
    grid_item_index: int | None = Field(None, alias='gridItemIndex')

class Offers(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    field_type: str | None = Field(None, alias='_type')
    alignment: str | None = None
    children: list[Child1] | None = None
    col_size: ColSize | None = Field(None, alias='colSize')
    gap: str | None = None

class DefaultImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage3(BaseModel):
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
    default_image: DefaultImage3 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage3 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage3 | None = Field(None, alias='smallImage')
    medium_image: MediumImage3 | None = Field(None, alias='mediumImage')
    large_image: LargeImage3 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage3 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage3 | None = Field(None, alias='xxlargeImage')
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

class Child7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText1 | None = Field(None, alias='richText')

class Child6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child7] | None = None
    size: str | None = None

class Footer(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    field_type: str | None = Field(None, alias='_type')
    children: list[Child6] | None = None
    text_alignment: str | None = Field(None, alias='textAlignment')

class DefaultImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage4(BaseModel):
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

class Child8(BaseModel):
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
    children: list[Child8] | None = None
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

class Child10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    rich_text: RichText5 | None = Field(None, alias='richText')

class Child9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child10] | None = None
    size: str | None = None

class Footer1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_id: str | None = Field(None, alias='_id')
    field_type: str | None = Field(None, alias='_type')
    children: list[Child9] | None = None
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

class Child11(BaseModel):
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
    children: list[Child11] | None = None
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

class Child5(BaseModel):
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

class Child4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: UUID | str | None = Field(None, alias='_id', union_mode='left_to_right')
    children: list[Child5] | None = None
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

class Child3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_type: str | None = Field(None, alias='_type')
    field_id: str | None = Field(None, alias='_id')
    children: list[Child4] | None = None
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
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage5(BaseModel):
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
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    transform: str | None = None
    max: list[int] | None = None
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage6(BaseModel):
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
    default_image: DefaultImage6 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage6 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage6 | None = Field(None, alias='smallImage')
    medium_image: MediumImage6 | None = Field(None, alias='mediumImage')
    large_image: LargeImage6 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage6 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage6 | None = Field(None, alias='xxlargeImage')

class DefaultImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage7(BaseModel):
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
    default_image: DefaultImage7 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage7 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage7 | None = Field(None, alias='smallImage')
    medium_image: MediumImage7 | None = Field(None, alias='mediumImage')
    large_image: LargeImage7 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage7 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage7 | None = Field(None, alias='xxlargeImage')

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

class DefaultImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage8(BaseModel):
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
    default_image: DefaultImage8 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage8 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage8 | None = Field(None, alias='smallImage')
    medium_image: MediumImage8 | None = Field(None, alias='mediumImage')
    large_image: LargeImage8 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage8 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage8 | None = Field(None, alias='xxlargeImage')
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

class DefaultImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XsmallImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage9(BaseModel):
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

class DefaultImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XsmallImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class SmallImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class MediumImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class LargeImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XlargeImage10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    ripcut_id: UUID | None = Field(None, alias='ripcutId')
    image_id: UUID | None = Field(None, alias='imageId')

class XxlargeImage10(BaseModel):
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
    default_image: DefaultImage10 | None = Field(None, alias='defaultImage')
    xsmall_image: XsmallImage10 | None = Field(None, alias='xsmallImage')
    small_image: SmallImage10 | None = Field(None, alias='smallImage')
    medium_image: MediumImage10 | None = Field(None, alias='mediumImage')
    large_image: LargeImage10 | None = Field(None, alias='largeImage')
    xlarge_image: XlargeImage10 | None = Field(None, alias='xlargeImage')
    xxlarge_image: XxlargeImage10 | None = Field(None, alias='xxlargeImage')
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
    children: Any | list[Child3] | None = None
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

class XsmallImage11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class SmallImage11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class MediumImage11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class LargeImage11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XlargeImage11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    source: str | None = None
    content_type: str | None = Field(None, alias='contentType')
    width: int | None = None
    height: int | None = None
    ripcut_id: str | None = Field(None, alias='ripcutId')
    image_id: str | None = Field(None, alias='imageId')

class XxlargeImage11(BaseModel):
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
    head_content: list[Any] | None = Field(None, alias='headContent')
    pre_content: list[list[PreContentItem]] | None = Field(None, alias='preContent')
    main_content: list[MainContentItem] | None = Field(None, alias='mainContent')
    post_content: list[PostContentItem] | None = Field(None, alias='postContent')
    modals: list[Modal] | None = None
    overrides: Overrides | None = None

class Glimpse7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_info_block: str | None = Field(None, alias='pageInfoBlock')

class MetricsData7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    glimpse: Glimpse7 | None = None

class Signup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    label: str | None = None
    url: str | None = None

class ToastCtaProps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    signup: Signup | None = None

class PageContentRedisHostname(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    eu_west_1: str | None = Field(None, alias='eu-west-1')
    us_east_1: str | None = Field(None, alias='us-east-1')
    us_west_2: str | None = Field(None, alias='us-west-2')

class AppConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    adobe_launch_script_url: str | None = Field(None, alias='adobeLaunchScriptUrl')
    help_center_url: str | None = Field(None, alias='helpCenterUrl')
    name: str | None = None
    page_content_redis_hostname: PageContentRedisHostname | None = Field(None, alias='pageContentRedisHostname')

class DictionaryVersions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    accessibility: str | None = None
    application: str | None = None
    commerce: str | None = None
    decorations: str | None = None
    identity: str | None = None
    iscp: str | None = None
    media: str | None = None
    off_device: str | None = Field(None, alias='off-device')
    paywall: str | None = None
    pcon: str | None = None
    promo: str | None = None
    ratings: str | None = None
    sdk_errors: str | None = Field(None, alias='sdk-errors')
    seo: str | None = None
    subscriptions: str | None = None
    unified_commerce: str | None = Field(None, alias='unified-commerce')
    unified_commerce_onboarding: str | None = Field(None, alias='unified-commerce-onboarding')
    unified_offers: str | None = Field(None, alias='unified-offers')
    welch: str | None = None

class Commerce(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    account: str | None = None
    base: str | None = None
    hulu_activation: Any | None = None
    incoming_activation_success: Any | None = None
    manage_subscription_help: str | None = None
    refresh_cookies: Any | None = None
    logo_navigation_home_logged_in: str | None = None
    logo_navigation_home_logged_out: str | None = None
    onboarding: str | None = None
    home: str | None = None
    unified_account: str | None = None
    welcome_back: str | None = None
    plan_select: str | None = None
    disney_account_details: Any | None = None
    disney_plan_switch_ledger: str | None = None
    disney_plan_switch: str | None = None
    disney_plan_selector: str | None = None
    disney_signup_preview: str | None = None
    disney_upsell_interstitial: Any | None = None
    espn_account_details: Any | None = None
    espn_plan_switch_ledger: str | None = None
    espn_plan_switch: str | None = None
    espn_plan_selector: str | None = None
    espn_signup_preview: str | None = None
    hulu_account_details: Any | None = None
    hulu_plan_selector: Any | None = None
    hulu_plan_switch: str | None = None
    hulu_plan_switch_ledger: str | None = None
    hulu_signup_preview: str | None = None
    login: str | None = None
    login_with_redirect: Any | None = None
    hoth: Any | None = None
    secure: Any | None = None
    student_verification: Any | None = Field(None, alias='studentVerification')
    home_service: Any | None = None
    account_api: Any | None = None
    waf: Any | None = None
    update_credentials: str | None = None
    root_domain: str | None = None
    yokozuna: Any | None = None

class Activate(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    wbd_max: str | None = None
    espn: Any | None = None
    hulu: str | None = None
    raptor_us: str | None = None
    crave_ca: str | None = None
    foxone_us: Any | None = None
    mlb_us: Any | None = None
    nfl_us: str | None = None
    tving_kr: str | None = None
    epicgames_us: Any | None = None

class Activation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    hulu: str | None = None

class Application1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    id: str | None = None
    version: str | None = None

class Sdk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_id: str | None = Field(None, alias='clientId')
    client_api_key: str | None = Field(None, alias='clientApiKey')
    environment: str | None = None
    debug_enabled: bool | None = Field(None, alias='debugEnabled')
    application: Application1 | None = None
    identity_client_id: str | None = Field(None, alias='identityClientId')

class GoogleRecaptcha(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    site_key: str | None = Field(None, alias='siteKey')

class Primary(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    port: int | None = None
    compression_level: int | None = Field(None, alias='compressionLevel')
    default_ttl_seconds: int | None = Field(None, alias='defaultTtlSeconds')
    type: str | None = None

class External(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None

class Internal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None

class CacheClients(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    primary: Primary | None = None
    external: External | None = None
    internal: Internal | None = None

class ExploreApiConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    base: str | None = None
    version: str | None = None
    page_version: str | None = Field(None, alias='pageVersion')

class Path(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    commerce: Commerce | None = None
    activate: Activate | None = None
    activation: Activation | None = None
    content: str | None = None
    dictionary_url: str | None = Field(None, alias='dictionaryUrl')
    dictionary_url_internal: str | None = Field(None, alias='dictionaryUrlInternal')
    hulu: str | None = None
    ripcut: str | None = None
    ripcut_raw: str | None = Field(None, alias='ripcutRaw')
    sdk: Sdk | None = None
    google_recaptcha: GoogleRecaptcha | None = Field(None, alias='googleRecaptcha')
    static_recommendations_assets: list[Any] | None = Field(None, alias='staticRecommendationsAssets')
    switch_setup_timeout_seconds: int | None = Field(None, alias='switchSetupTimeoutSeconds')
    orchestration_url: str | None = Field(None, alias='orchestrationUrl')
    identity_provider_service: str | None = Field(None, alias='identityProviderService')
    cache_clients: CacheClients | None = None
    access_token: str | None = Field(None, alias='accessToken')
    explore_api_config: ExploreApiConfig | None = Field(None, alias='exploreApiConfig')
    orchestration_b2b_api_uri: str | None = Field(None, alias='orchestrationB2bApiUri')

class Billing(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    gift_card_number_mask: str | None = Field(None, alias='giftCardNumberMask')
    gift_card_number_min_length: int | None = Field(None, alias='giftCardNumberMinLength')

class Commerce1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    billing: Billing | None = None
    cypher_variable_error_paths_to_crash: list[str] | None = Field(None, alias='cypherVariableErrorPathsToCrash')
    enabled_analytics_tooling: list[str] | None = Field(None, alias='enabledAnalyticsTooling')
    hardcoded_queries: list[Any] | None = Field(None, alias='hardcodedQueries')
    url_param_host_allowlist: list[Any] | None = Field(None, alias='urlParamHostAllowlist')
    payment_methods: Any | None = Field(None, alias='paymentMethods')
    ravelin: Any | None = None

class Adobe(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cross_domains: list[str] | None = Field(None, alias='crossDomains')
    rsid: str | None = None
    rsidname: str | None = None
    server: str | None = None
    secure_server: str | None = Field(None, alias='secureServer')
    visitor_namespace: str | None = Field(None, alias='visitorNamespace')
    visitor: str | None = None
    audience_manager_server: str | None = Field(None, alias='audienceManagerServer')
    disable_third_party_cookies: bool | None = Field(None, alias='disableThirdPartyCookies')
    site: str | None = None
    web_app_name: str | None = Field(None, alias='webAppName')

class Tealium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None

class Analytics(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    adobe: Adobe | None = None
    partner: str | None = None
    tealium: Tealium | None = None

class IdentitySdk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_id: str | None = Field(None, alias='clientId')
    enabled: bool | None = None
    environment: str | None = None
    rollout_percentage: int | None = Field(None, alias='rolloutPercentage')

class Script(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    stub_sdk: str | None = Field(None, alias='stubSDK')
    guuid: UUID | None = None

class CategoryPurposes(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    c0001: UUID | None = Field(None, alias='C0001')
    c0002: UUID | None = Field(None, alias='C0002')
    c0004: UUID | None = Field(None, alias='C0004')

class Api(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    tokens: list[str] | None = None
    purposes: list[str] | None = None
    category_purposes: CategoryPurposes | None = Field(None, alias='categoryPurposes')

class CategoryPurposes1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    field_1: UUID | None = Field(None, alias='1')
    field_2: UUID | None = Field(None, alias='2')
    field_4: UUID | None = Field(None, alias='4')

class UnifiedConsentApi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    tokens: list[str] | None = None
    purposes: list[str] | None = None
    category_purposes: CategoryPurposes1 | None = Field(None, alias='categoryPurposes')

class ConsentGroups(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    necessary: str | None = None
    performance_and_analytics: str | None = Field(None, alias='performanceAndAnalytics')
    functional: str | None = None
    targeted_advertising: str | None = Field(None, alias='targetedAdvertising')
    social_media: str | None = Field(None, alias='socialMedia')

class OneTrust(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    script: Script | None = None
    api: Api | None = None
    unified_consent_api: UnifiedConsentApi | None = Field(None, alias='unifiedConsentApi')
    consent_groups: ConsentGroups | None = Field(None, alias='consentGroups')

class ArAr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class CsCz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class DaDk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class DeDe(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class ElGr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class En(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class EnGb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class Es419(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class EsEs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class FiFi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class FrCa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class FrFr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class HeIl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class HuHu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class HrHr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class IdId(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class ItIt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class JaJp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class KoKr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class MsMy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class NlNl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class NoNo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class PlPl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class PtBr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class PtPt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class RoRo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class SkSk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class SvSe(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class ThTh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class TrTr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class ZhHans(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class ZhHant(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class ZhHk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    dict_: str | None = Field(None, alias='dict')
    hreflang: str | None = None

class SupportedLangsMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ar_ar: ArAr | None = Field(None, alias='ar-ar')
    cs_cz: CsCz | None = Field(None, alias='cs-cz')
    da_dk: DaDk | None = Field(None, alias='da-dk')
    de_de: DeDe | None = Field(None, alias='de-de')
    el_gr: ElGr | None = Field(None, alias='el-gr')
    en: En | None = None
    en_gb: EnGb | None = Field(None, alias='en-gb')
    es_419: Es419 | None = Field(None, alias='es-419')
    es_es: EsEs | None = Field(None, alias='es-es')
    fi_fi: FiFi | None = Field(None, alias='fi-fi')
    fr_ca: FrCa | None = Field(None, alias='fr-ca')
    fr_fr: FrFr | None = Field(None, alias='fr-fr')
    he_il: HeIl | None = Field(None, alias='he-il')
    hu_hu: HuHu | None = Field(None, alias='hu-hu')
    hr_hr: HrHr | None = Field(None, alias='hr-hr')
    id_id: IdId | None = Field(None, alias='id-id')
    it_it: ItIt | None = Field(None, alias='it-it')
    ja_jp: JaJp | None = Field(None, alias='ja-jp')
    ko_kr: KoKr | None = Field(None, alias='ko-kr')
    ms_my: MsMy | None = Field(None, alias='ms-my')
    nl_nl: NlNl | None = Field(None, alias='nl-nl')
    no_no: NoNo | None = Field(None, alias='no-no')
    pl_pl: PlPl | None = Field(None, alias='pl-pl')
    pt_br: PtBr | None = Field(None, alias='pt-br')
    pt_pt: PtPt | None = Field(None, alias='pt-pt')
    ro_ro: RoRo | None = Field(None, alias='ro-ro')
    sk_sk: SkSk | None = Field(None, alias='sk-sk')
    sv_se: SvSe | None = Field(None, alias='sv-se')
    th_th: ThTh | None = Field(None, alias='th-th')
    tr_tr: TrTr | None = Field(None, alias='tr-tr')
    zh_hans: ZhHans | None = Field(None, alias='zh-hans')
    zh_hant: ZhHant | None = Field(None, alias='zh-hant')
    zh_hk: ZhHk | None = Field(None, alias='zh-hk')

class AuthZ(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    client_id: str | None = Field(None, alias='clientId')
    authorization_url: str | None = Field(None, alias='authorizationUrl')

class Convergence(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    auth_z: AuthZ | None = Field(None, alias='authZ')
    enabled: bool | None = None

class RemoteAppConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bolt_partner_id: Any | None = Field(None, alias='boltPartnerId')
    commerce: Commerce1 | None = None
    analytics: Analytics | None = None
    dictionary_tenant: str | None = Field(None, alias='dictionaryTenant')
    globalization_service_version: str | None = Field(None, alias='globalizationServiceVersion')
    identity_sdk: IdentitySdk | None = Field(None, alias='identitySDK')
    one_id: Any | None = Field(None, alias='oneId')
    one_trust: OneTrust | None = Field(None, alias='oneTrust')
    supported_langs_map: SupportedLangsMap | None = Field(None, alias='supportedLangsMap')
    convergence: Convergence | None = None

class Af(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Nu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class ChangePayment(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class Purchase(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class UnAuth(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class DefaultProduct(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class SpecialOfferProduct(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class Commerce2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Au(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce2 | None = None
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')
    marketing: Marketing | None = None

class Bd(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Bn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Bt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Bu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce3 | None = None
    feature_config: FeatureConfig | None = Field(None, alias='featureConfig')
    marketing: Marketing1 | None = None

class Commerce4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ck(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce4 | None = None
    feature_config: FeatureConfig | None = Field(None, alias='featureConfig')
    marketing: Marketing1 | None = None

class Cn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Fj(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct1 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Hk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce5 | None = None
    feature_config: FeatureConfig2 | None = Field(None, alias='featureConfig')
    marketing: Marketing3 | None = None

class Hm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Id(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing3 | None = None

class In(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct2 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Jp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce6 | None = None
    feature_config: FeatureConfig2 | None = Field(None, alias='featureConfig')
    marketing: Marketing3 | None = None

class Kh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ki(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    card_options_popover_enabled: bool | None = Field(None, alias='cardOptionsPopoverEnabled')
    default_product: DefaultProduct3 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    minimum_age_to_subscribe: int | None = Field(None, alias='minimumAgeToSubscribe')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')
    enable_age_verification: bool | None = Field(None, alias='enableAgeVerification')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Kr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce7 | None = None
    feature_config: FeatureConfig4 | None = Field(None, alias='featureConfig')
    marketing: Marketing3 | None = None

class La(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Lk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Mm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Mo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Mv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class My(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing3 | None = None

class Commerce8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Nf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce8 | None = None
    feature_config: FeatureConfig5 | None = Field(None, alias='featureConfig')
    marketing: Marketing8 | None = None

class Np(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Nr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Nu4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce9 | None = None
    feature_config: FeatureConfig5 | None = Field(None, alias='featureConfig')
    marketing: Marketing8 | None = None

class Nu5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class DefaultProduct4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct4 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Nz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce10 | None = None
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')
    marketing: Marketing10 | None = None

class Pg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ph(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing10 | None = None

class Pk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Sb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct5(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct5 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')

class Sg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce11 | None = None
    feature_config: FeatureConfig7 | None = Field(None, alias='featureConfig')
    marketing: Marketing10 | None = None

class Th(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing10 | None = None

class Commerce12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Tk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce12 | None = None
    feature_config: FeatureConfig8 | None = Field(None, alias='featureConfig')
    marketing: Marketing14 | None = None

class Tl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class To(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Tp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Tv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct6(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct6 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_e_guid: bool | None = Field(None, alias='requiresEGuid')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Tw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce13 | None = None
    feature_config: FeatureConfig9 | None = Field(None, alias='featureConfig')
    marketing: Marketing15 | None = None

class Vn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Vu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ws(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct7(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct7 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Ad(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce14 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing15 | None = None

class Ae(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing15 | None = None

class Commerce15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ai(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce15 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing15 | None = None

class DefaultProduct8(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct8 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Al(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce16 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing15 | None = None

class Am(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class An(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ao(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Portability(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class DefaultProduct9(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct9 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class At(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce17 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing15 | None = None

class Commerce18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Aw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce18 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing15 | None = None

class Commerce19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ax(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce19 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing22 | None = None

class DefaultProduct10(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct10 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ba(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce20 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing23 | None = None

class DefaultProduct11(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct11 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Be(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce21 | None = None
    feature_config: FeatureConfig10 | None = Field(None, alias='featureConfig')
    marketing: Marketing23 | None = None

class Bf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct12(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    local_price_enabled: bool | None = Field(None, alias='localPriceEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct12 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class Bg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce22 | None = None
    feature_config: FeatureConfig19 | None = Field(None, alias='featureConfig')
    marketing: Marketing23 | None = None

class Bh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing23 | None = None

class Bi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Bj(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class FeatureConfig20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Bl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce23 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing27 | None = None

class Commerce24(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Bm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce24 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing28 | None = None

class Commerce25(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce25 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing28 | None = None

class Bv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')

class Bw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Cd(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Cf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Cq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct13(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct13 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ch(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce26 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing28 | None = None

class Ci(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Cm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Cs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')

class Cv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce27 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing28 | None = None

class Commerce28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cx(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce28 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing32 | None = None

class Cy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')

class DefaultProduct14(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce29(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct14 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce29 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class DefaultProduct15(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class RegulatedCancelFlow(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cancel_footer_nav_to_sub_details: bool | None = Field(None, alias='cancelFooterNavToSubDetails')
    hide_cancel_footer_when_unauth: bool | None = Field(None, alias='hideCancelFooterWhenUnauth')
    show_regulated_cancellation_flow: bool | None = Field(None, alias='showRegulatedCancellationFlow')

class Commerce30(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    annual_auto_downgrade: bool | None = Field(None, alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct15 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow | None = Field(None, alias='regulatedCancelFlow')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool | None = Field(None, alias='requiresAdditionalSADisclaimer')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class De(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce30 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class Dj(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct16(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce31(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct16 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Dk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce31 | None = None
    feature_config: FeatureConfig20 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class Dz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing33 | None = None

class DefaultProduct17(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct17 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class Ee(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce32 | None = None
    feature_config: FeatureConfig32 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class FeatureConfig33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Eg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class Eh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Er(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct18(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct18 | None = Field(None, alias='defaultProduct')
    disable_province_dropdown: bool | None = Field(None, alias='disableProvinceDropdown')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Es(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce33 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class Et(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct19(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct19 | None = Field(None, alias='defaultProduct')
    disable_province_dropdown: bool | None = Field(None, alias='disableProvinceDropdown')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Fi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce34 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class Commerce35(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Fk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce35 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing33 | None = None

class Commerce36(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing42(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Fo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce36 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing42 | None = None

class DefaultProduct20(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce37(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct20 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow | None = Field(None, alias='regulatedCancelFlow')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool | None = Field(None, alias='requiresAdditionalSADisclaimer')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing43(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Fr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce37 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing43 | None = None

class Fx(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ga(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct21(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce38(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct21 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce38 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing43 | None = None

class Commerce39(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing45(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Gf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce39 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing45 | None = None

class Commerce40(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Gg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce40 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing45 | None = None

class Gh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce41(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Gi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce41 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing45 | None = None

class DefaultProduct22(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce42(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default_product: DefaultProduct22 | None = Field(None, alias='defaultProduct')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing48(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Gl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce42 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing48 | None = None

class Gm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Gn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce43(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing49(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Gp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce43 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing49 | None = None

class Gq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct23(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce44(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct23 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing50(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Gr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce44 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing50 | None = None

class Commerce45(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce45 | None = None
    feature_config: FeatureConfig33 | None = Field(None, alias='featureConfig')
    marketing: Marketing50 | None = None

class Gw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct24(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce46(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct24 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig47(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class Hr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce46 | None = None
    feature_config: FeatureConfig47 | None = Field(None, alias='featureConfig')
    marketing: Marketing50 | None = None

class DefaultProduct25(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce47(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct25 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig48(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Hu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce47 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing50 | None = None

class DefaultProduct26(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce48(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct26 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ie(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce48 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing50 | None = None

class Il(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing50 | None = None

class Commerce49(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing56(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Im(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce49 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing56 | None = None

class Commerce50(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Io(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce50 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing56 | None = None

class Marketing58(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Iq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing58 | None = None

class Ir(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct27(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce51(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct27 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Is(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce51 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing58 | None = None

class DefaultProduct28(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce52(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct28 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class It(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce52 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing58 | None = None

class Commerce53(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing61(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Je(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce53 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing61 | None = None

class Marketing62(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Jo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing62 | None = None

class Ke(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Km(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Kw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing62 | None = None

class Commerce54(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ky(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce54 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing62 | None = None

class Lb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing62 | None = None

class DefaultProduct29(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce55(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct29 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Li(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce55 | None = None
    feature_config: FeatureConfig48 | None = Field(None, alias='featureConfig')
    marketing: Marketing62 | None = None

class Lr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ls(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct30(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce56(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct30 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig58(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class Lt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce56 | None = None
    feature_config: FeatureConfig58 | None = Field(None, alias='featureConfig')
    marketing: Marketing62 | None = None

class DefaultProduct31(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce57(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct31 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig59(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Lu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce57 | None = None
    feature_config: FeatureConfig59 | None = Field(None, alias='featureConfig')
    marketing: Marketing62 | None = None

class DefaultProduct32(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce58(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct32 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig60(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class Lv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce58 | None = None
    feature_config: FeatureConfig60 | None = Field(None, alias='featureConfig')
    marketing: Marketing62 | None = None

class Ly(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ma(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing62 | None = None

class DefaultProduct33(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce59(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    default_product: DefaultProduct33 | None = Field(None, alias='defaultProduct')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig61(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing71(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce59 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing71 | None = None

class Md(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct34(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce60(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct34 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing72(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Me(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce60 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing72 | None = None

class Commerce61(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing73(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce61 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing73 | None = None

class Mg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce62(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    sells_bundle: bool | None = Field(None, alias='sellsBundle')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing74(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce62 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing74 | None = None

class DefaultProduct35(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce63(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct35 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce63 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing74 | None = None

class Ml(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce64(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing76(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mq(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce64 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing76 | None = None

class Mr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce65(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing77(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ms(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce65 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing77 | None = None

class DefaultProduct36(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce66(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct36 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce66 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing77 | None = None

class DefaultProduct37(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce67(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct37 | None = Field(None, alias='defaultProduct')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing79(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce67 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing79 | None = None

class Mw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Mz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Na(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce68(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Nc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce68 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing79 | None = None

class Ne(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ng(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct38(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class LocalPayment(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    bank_options: list[str] | None = Field(None, alias='bankOptions')
    client_key: str | None = None

class Commerce69(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct38 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    local_payment: LocalPayment | None = Field(None, alias='localPayment')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing81(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Nl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce69 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing81 | None = None

class DefaultProduct39(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce70(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct39 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class No(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce70 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing81 | None = None

class Nt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Om(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing81 | None = None

class Commerce71(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing84(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Pf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce71 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing84 | None = None

class DefaultProduct40(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce72(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    annual_auto_downgrade: bool | None = Field(None, alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct40 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing85(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Pl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce72 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing85 | None = None

class Commerce73(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing86(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Pm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce73 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing86 | None = None

class Commerce74(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Pn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce74 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing86 | None = None

class Marketing88(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing88 | None = None

class DefaultProduct41(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce75(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct41 | None = Field(None, alias='defaultProduct')
    disable_province_dropdown: bool | None = Field(None, alias='disableProvinceDropdown')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce75 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing88 | None = None

class Qa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing88 | None = None

class Commerce76(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing91(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Re(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce76 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing91 | None = None

class DefaultProduct42(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce77(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct42 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing92(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ro(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce77 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing92 | None = None

class DefaultProduct43(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce78(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct43 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Rs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce78 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing92 | None = None

class Rw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Sa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing92 | None = None

class Sc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct44(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce79(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct44 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Se(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce79 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing92 | None = None

class Commerce80(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing96(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sh(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce80 | None = None
    feature_config: FeatureConfig61 | None = Field(None, alias='featureConfig')
    marketing: Marketing96 | None = None

class DefaultProduct45(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce81(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct45 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig84(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class Marketing97(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Si(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce81 | None = None
    feature_config: FeatureConfig84 | None = Field(None, alias='featureConfig')
    marketing: Marketing97 | None = None

class Commerce82(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class FeatureConfig85(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing98(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sj(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce82 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing98 | None = None

class DefaultProduct46(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce83(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct46 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing99(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce83 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing99 | None = None

class Sl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct47(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce84(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct47 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce84 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing100 | None = None

class Sn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class So(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ss(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class St(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce85(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing101(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sx(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce85 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing101 | None = None

class Sy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Sz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce86(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce86 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing101 | None = None

class Td(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce87(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing103(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Tf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce87 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing103 | None = None

class Tg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Marketing104(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Tn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing104 | None = None

class DefaultProduct48(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce88(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct48 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce88 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing104 | None = None

class Tz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ua(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Ug(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Marketing106(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Uk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing106 | None = None

class DefaultProduct49(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce89(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct49 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Va(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce89 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing106 | None = None

class Commerce90(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing108(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Vg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce90 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing108 | None = None

class Commerce91(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Marketing109(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Wf(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce91 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing109 | None = None

class Commerce92(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Xk(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce92 | None = None
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')

class Ye(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Commerce93(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Yt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce93 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing109 | None = None

class Yu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Marketing111(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Za(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    marketing: Marketing111 | None = None

class Zm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Zr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class Zw(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None

class DefaultProduct50(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce94(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct50 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ag(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce94 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class CancelSubscriptionNavItemPromoted(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cancel_subscription_nav_item_period: int | None = Field(None, alias='cancelSubscriptionNavItemPeriod')

class DefaultProduct51(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce95(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cancel_subscription_nav_item_promoted: CancelSubscriptionNavItemPromoted | None = Field(None, alias='cancelSubscriptionNavItemPromoted')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct51 | None = Field(None, alias='defaultProduct')
    is_one_step_cancel_billing_country: bool | None = Field(None, alias='isOneStepCancelBillingCountry')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ar(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce95 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct52(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce96(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct52 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bb(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce96 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct53(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce97(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct53 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce97 | None = None
    feature_config: FeatureConfig85 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct54(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce98(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct54 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    starz_play_supported_regions: bool | None = Field(None, alias='starzPlaySupportedRegions')

class FeatureConfig101(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_additional_ratings: bool | None = Field(None, alias='displayAdditionalRatings')
    display_rating_advisories: bool | None = Field(None, alias='displayRatingAdvisories')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Br(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce98 | None = None
    feature_config: FeatureConfig101 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct55(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce99(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct55 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig102(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Bs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce99 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct56(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct56 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce100 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct57(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce101(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct57 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cl(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce101 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct58(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce102(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct58 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Co(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce102 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct59(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce103(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct59 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce103 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct60(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce104(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct60 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Dm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce104 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct61(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce105(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct61 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Do(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce105 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct62(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce106(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct62 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ec(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce106 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct63(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce107(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct63 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gd(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce107 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct64(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce108(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct64 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce108 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct65(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce109(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct65 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce109 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct66(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce110(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct66 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Hn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce110 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct67(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce111(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct67 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ht(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce111 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct68(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce112(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct68 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Jm(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce112 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct69(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce113(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct69 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Kn(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce113 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct70(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce114(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct70 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Lc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce114 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct71(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce115(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct71 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    starz_play_supported_regions: bool | None = Field(None, alias='starzPlaySupportedRegions')

class Mx(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce115 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct72(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce116(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct72 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ni(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce116 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct73(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce117(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct73 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pa(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce117 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct74(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce118(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct74 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pe(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce118 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct75(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce119(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct75 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Py(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce119 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct76(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce120(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct76 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Sr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce120 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct77(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce121(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct77 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Sv(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce121 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct78(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce122(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct78 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tt(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce122 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct79(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce123(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct79 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Uy(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce123 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct80(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce124(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct80 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Vc(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce124 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class DefaultProduct81(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce125(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct81 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ve(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce125 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing111 | None = None

class Commerce126(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing144(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class As(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce126 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing144 | None = None

class DefaultProduct82(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce127(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct82 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing145(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ca(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce127 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing145 | None = None

class Commerce128(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing146(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Gu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce128 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing146 | None = None

class Commerce129(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mp(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce129 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing146 | None = None

class Commerce130(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pr(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce130 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing146 | None = None

class Commerce131(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    sells_bundle: bool | None = Field(None, alias='sellsBundle')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Marketing149(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Um(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce131 | None = None
    feature_config: FeatureConfig102 | None = Field(None, alias='featureConfig')
    marketing: Marketing149 | None = None

class AdsTierDevices(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    comcastx1: bool | None = None
    cox: bool | None = None
    hisense: bool | None = None
    lg: bool | None = None
    ps: bool | None = None
    ps4: bool | None = None
    samsung: bool | None = None
    vizio: bool | None = None
    xbox: bool | None = None

class DefaultProduct83(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class DevicesThatSell2PBundle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    comcast: bool | None = None
    comcastx1: bool | None = None
    cox: bool | None = None
    lg: bool | None = None
    samsung: bool | None = None
    ps4: bool | None = None
    ps: bool | None = None
    tivo_us: bool | None = None
    vizio: bool | None = None
    xbox: bool | None = None
    xglobal: bool | None = None

class DevicesThatSellBundle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    comcast: bool | None = None
    comcastx1: bool | None = None
    cox: bool | None = None
    lg: bool | None = None
    ps: bool | None = None
    ps4: bool | None = None
    samsung: bool | None = None
    tivo_us: bool | None = None
    vizio: bool | None = None
    xbox: bool | None = None
    xglobal: bool | None = None

class Amazon(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Cox(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Hisense(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Lg(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Ps1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Ps4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Samsung(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class TivoUs(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Tv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Vizio(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Xbox(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Xglobal(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class LicensePlateFlowNavigation(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    amazon: Amazon | None = Field(None, alias='AMAZON')
    cox: Cox | None = None
    hisense: Hisense | None = None
    lg: Lg | None = None
    ps: Ps1 | None = None
    ps4: Ps4 | None = None
    samsung: Samsung | None = None
    tivo_us: TivoUs | None = None
    tv: Tv1 | None = None
    vizio: Vizio | None = None
    xbox: Xbox | None = None
    xglobal: Xglobal | None = None

class NineMonth(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    price: float | None = None
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class OneYear(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    price: float | None = None
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class SixMonth(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    price: float | None = None
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class ThreeYear(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    price: float | None = None
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class TwoYear(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    price: float | None = None
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class Ft(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nine_month: NineMonth | None = Field(None, alias='nineMonth')
    one_year: OneYear | None = Field(None, alias='oneYear')
    six_month: SixMonth | None = Field(None, alias='sixMonth')
    three_year: ThreeYear | None = Field(None, alias='threeYear')
    two_year: TwoYear | None = Field(None, alias='twoYear')

class Purchase84(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nine_month: NineMonth | None = Field(None, alias='nineMonth')
    one_year: OneYear | None = Field(None, alias='oneYear')
    six_month: SixMonth | None = Field(None, alias='sixMonth')
    three_year: ThreeYear | None = Field(None, alias='threeYear')
    two_year: TwoYear | None = Field(None, alias='twoYear')

class Superbundle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nine_month: NineMonth | None = Field(None, alias='nineMonth')
    one_year: OneYear | None = Field(None, alias='oneYear')
    six_month: SixMonth | None = Field(None, alias='sixMonth')

class RewardsProducts(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ft: Ft | None = Field(None, alias='FT')
    purchase: Purchase84 | None = None
    superbundle: Superbundle | None = None

class Commerce132(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ads_tier_devices: AdsTierDevices | None = Field(None, alias='adsTierDevices')
    ads_tier_enabled: bool | None = Field(None, alias='adsTierEnabled')
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct83 | None = Field(None, alias='defaultProduct')
    devices_that_sell2_p_bundle: DevicesThatSell2PBundle | None = Field(None, alias='devicesThatSell2PBundle')
    devices_that_sell_bundle: DevicesThatSellBundle | None = Field(None, alias='devicesThatSellBundle')
    enable_global_identity_unbranded_create_account: bool | None = Field(None, alias='enableGlobalIdentityUnbrandedCreateAccount')
    license_plate_flow_navigation: LicensePlateFlowNavigation | None = Field(None, alias='licensePlateFlowNavigation')
    one_step_cancel_billing_states: list[str] | None = Field(None, alias='oneStepCancelBillingStates')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_annual_opt_in_states: list[str] | None = Field(None, alias='requiresAnnualOptInStates')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    rewards_products: RewardsProducts | None = Field(None, alias='rewardsProducts')
    sells_bundle: bool | None = Field(None, alias='sellsBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig135(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    enable_identity_consent_sync: bool | None = Field(None, alias='enableIdentityConsentSync')

class Us(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    footer: list[str] | None = None
    group: str | None = None
    commerce: Commerce132 | None = None
    feature_config: FeatureConfig135 | None = Field(None, alias='featureConfig')
    marketing: Marketing149 | None = None

class Commerce133(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class FeatureConfig136(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Marketing151(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Vi(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    parent_country: str | None = Field(None, alias='parentCountry')
    group: str | None = None
    commerce: Commerce133 | None = None
    feature_config: FeatureConfig136 | None = Field(None, alias='featureConfig')
    marketing: Marketing151 | None = None

class Yz(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    group: str | None = None
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')

class Countries(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    af: Af | None = Field(None, alias='AF')
    au: Au | None = Field(None, alias='AU')
    bd: Bd | None = Field(None, alias='BD')
    bn: Bn | None = Field(None, alias='BN')
    bt: Bt | None = Field(None, alias='BT')
    bu: Bu | None = Field(None, alias='BU')
    cc: Cc | None = Field(None, alias='CC')
    ck: Ck | None = Field(None, alias='CK')
    cn: Cn | None = Field(None, alias='CN')
    fj: Fj | None = Field(None, alias='FJ')
    hk: Hk | None = Field(None, alias='HK')
    hm: Hm | None = Field(None, alias='HM')
    id: Id | None = Field(None, alias='ID')
    in_: In | None = Field(None, alias='IN')
    jp: Jp | None = Field(None, alias='JP')
    kh: Kh | None = Field(None, alias='KH')
    ki: Ki | None = Field(None, alias='KI')
    kr: Kr | None = Field(None, alias='KR')
    la: La | None = Field(None, alias='LA')
    lk: Lk | None = Field(None, alias='LK')
    mm: Mm | None = Field(None, alias='MM')
    mo: Mo | None = Field(None, alias='MO')
    mv: Mv | None = Field(None, alias='MV')
    my: My | None = Field(None, alias='MY')
    nf: Nf | None = Field(None, alias='NF')
    np: Np | None = Field(None, alias='NP')
    nr: Nr | None = Field(None, alias='NR')
    nu: Nu4 | None = Field(None, alias='NU')
    nz: Nz | None = Field(None, alias='NZ')
    pg: Pg | None = Field(None, alias='PG')
    ph: Ph | None = Field(None, alias='PH')
    pk: Pk | None = Field(None, alias='PK')
    sb: Sb | None = Field(None, alias='SB')
    sg: Sg | None = Field(None, alias='SG')
    th: Th | None = Field(None, alias='TH')
    tk: Tk | None = Field(None, alias='TK')
    tl: Tl | None = Field(None, alias='TL')
    to: To | None = Field(None, alias='TO')
    tp: Tp | None = Field(None, alias='TP')
    tv: Tv | None = Field(None, alias='TV')
    tw: Tw | None = Field(None, alias='TW')
    vn: Vn | None = Field(None, alias='VN')
    vu: Vu | None = Field(None, alias='VU')
    ws: Ws | None = Field(None, alias='WS')
    ad: Ad | None = Field(None, alias='AD')
    ae: Ae | None = Field(None, alias='AE')
    ai: Ai | None = Field(None, alias='AI')
    al: Al | None = Field(None, alias='AL')
    am: Am | None = Field(None, alias='AM')
    an: An | None = Field(None, alias='AN')
    ao: Ao | None = Field(None, alias='AO')
    at: At | None = Field(None, alias='AT')
    aw: Aw | None = Field(None, alias='AW')
    ax: Ax | None = Field(None, alias='AX')
    ba: Ba | None = Field(None, alias='BA')
    be: Be | None = Field(None, alias='BE')
    bf: Bf | None = Field(None, alias='BF')
    bg: Bg | None = Field(None, alias='BG')
    bh: Bh | None = Field(None, alias='BH')
    bi: Bi | None = Field(None, alias='BI')
    bj: Bj | None = Field(None, alias='BJ')
    bl: Bl | None = Field(None, alias='BL')
    bm: Bm | None = Field(None, alias='BM')
    bq: Bq | None = Field(None, alias='BQ')
    bv: Bv | None = Field(None, alias='BV')
    bw: Bw | None = Field(None, alias='BW')
    cd: Cd | None = Field(None, alias='CD')
    cf: Cf | None = Field(None, alias='CF')
    cq: Cq | None = Field(None, alias='CQ')
    ch: Ch | None = Field(None, alias='CH')
    ci: Ci | None = Field(None, alias='CI')
    cm: Cm | None = Field(None, alias='CM')
    cs: Cs | None = Field(None, alias='CS')
    cv: Cv | None = Field(None, alias='CV')
    cw: Cw | None = Field(None, alias='CW')
    cx: Cx | None = Field(None, alias='CX')
    cy: Cy | None = Field(None, alias='CY')
    cz: Cz | None = Field(None, alias='CZ')
    de: De | None = Field(None, alias='DE')
    dj: Dj | None = Field(None, alias='DJ')
    dk: Dk | None = Field(None, alias='DK')
    dz: Dz | None = Field(None, alias='DZ')
    ee: Ee | None = Field(None, alias='EE')
    eg: Eg | None = Field(None, alias='EG')
    eh: Eh | None = Field(None, alias='EH')
    er: Er | None = Field(None, alias='ER')
    es: Es | None = Field(None, alias='ES')
    et: Et | None = Field(None, alias='ET')
    fi: Fi | None = Field(None, alias='FI')
    fk: Fk | None = Field(None, alias='FK')
    fo: Fo | None = Field(None, alias='FO')
    fr: Fr | None = Field(None, alias='FR')
    fx: Fx | None = Field(None, alias='FX')
    ga: Ga | None = Field(None, alias='GA')
    gb: Gb | None = Field(None, alias='GB')
    gf: Gf | None = Field(None, alias='GF')
    gg: Gg | None = Field(None, alias='GG')
    gh: Gh | None = Field(None, alias='GH')
    gi: Gi | None = Field(None, alias='GI')
    gl: Gl | None = Field(None, alias='GL')
    gm: Gm | None = Field(None, alias='GM')
    gn: Gn | None = Field(None, alias='GN')
    gp: Gp | None = Field(None, alias='GP')
    gq: Gq | None = Field(None, alias='GQ')
    gr: Gr | None = Field(None, alias='GR')
    gs: Gs | None = Field(None, alias='GS')
    gw: Gw | None = Field(None, alias='GW')
    hr: Hr | None = Field(None, alias='HR')
    hu: Hu | None = Field(None, alias='HU')
    ie: Ie | None = Field(None, alias='IE')
    il: Il | None = Field(None, alias='IL')
    im: Im | None = Field(None, alias='IM')
    io: Io | None = Field(None, alias='IO')
    iq: Iq | None = Field(None, alias='IQ')
    ir: Ir | None = Field(None, alias='IR')
    is_: Is | None = Field(None, alias='IS')
    it: It | None = Field(None, alias='IT')
    je: Je | None = Field(None, alias='JE')
    jo: Jo | None = Field(None, alias='JO')
    ke: Ke | None = Field(None, alias='KE')
    km: Km | None = Field(None, alias='KM')
    kw: Kw | None = Field(None, alias='KW')
    ky: Ky | None = Field(None, alias='KY')
    lb: Lb | None = Field(None, alias='LB')
    li: Li | None = Field(None, alias='LI')
    lr: Lr | None = Field(None, alias='LR')
    ls: Ls | None = Field(None, alias='LS')
    lt: Lt | None = Field(None, alias='LT')
    lu: Lu | None = Field(None, alias='LU')
    lv: Lv | None = Field(None, alias='LV')
    ly: Ly | None = Field(None, alias='LY')
    ma: Ma | None = Field(None, alias='MA')
    mc: Mc | None = Field(None, alias='MC')
    md: Md | None = Field(None, alias='MD')
    me: Me | None = Field(None, alias='ME')
    mf: Mf | None = Field(None, alias='MF')
    mg: Mg | None = Field(None, alias='MG')
    mh: Mh | None = Field(None, alias='MH')
    mk: Mk | None = Field(None, alias='MK')
    ml: Ml | None = Field(None, alias='ML')
    mq: Mq | None = Field(None, alias='MQ')
    mr: Mr | None = Field(None, alias='MR')
    ms: Ms | None = Field(None, alias='MS')
    mt: Mt | None = Field(None, alias='MT')
    mu: Mu | None = Field(None, alias='MU')
    mw: Mw | None = Field(None, alias='MW')
    mz: Mz | None = Field(None, alias='MZ')
    na: Na | None = Field(None, alias='NA')
    nc: Nc | None = Field(None, alias='NC')
    ne: Ne | None = Field(None, alias='NE')
    ng: Ng | None = Field(None, alias='NG')
    nl: Nl | None = Field(None, alias='NL')
    no: No | None = Field(None, alias='NO')
    nt: Nt | None = Field(None, alias='NT')
    om: Om | None = Field(None, alias='OM')
    pf: Pf | None = Field(None, alias='PF')
    pl: Pl | None = Field(None, alias='PL')
    pm: Pm | None = Field(None, alias='PM')
    pn: Pn | None = Field(None, alias='PN')
    ps: Ps | None = Field(None, alias='PS')
    pt: Pt | None = Field(None, alias='PT')
    qa: Qa | None = Field(None, alias='QA')
    re: Re | None = Field(None, alias='RE')
    ro: Ro | None = Field(None, alias='RO')
    rs: Rs | None = Field(None, alias='RS')
    rw: Rw | None = Field(None, alias='RW')
    sa: Sa | None = Field(None, alias='SA')
    sc: Sc | None = Field(None, alias='SC')
    se: Se | None = Field(None, alias='SE')
    sh: Sh | None = Field(None, alias='SH')
    si: Si | None = Field(None, alias='SI')
    sj: Sj | None = Field(None, alias='SJ')
    sk: Sk | None = Field(None, alias='SK')
    sl: Sl | None = Field(None, alias='SL')
    sm: Sm | None = Field(None, alias='SM')
    sn: Sn | None = Field(None, alias='SN')
    so: So | None = Field(None, alias='SO')
    ss: Ss | None = Field(None, alias='SS')
    st: St | None = Field(None, alias='ST')
    sx: Sx | None = Field(None, alias='SX')
    sy: Sy | None = Field(None, alias='SY')
    sz: Sz | None = Field(None, alias='SZ')
    tc: Tc | None = Field(None, alias='TC')
    td: Td | None = Field(None, alias='TD')
    tf: Tf | None = Field(None, alias='TF')
    tg: Tg | None = Field(None, alias='TG')
    tn: Tn | None = Field(None, alias='TN')
    tr: Tr | None = Field(None, alias='TR')
    tz: Tz | None = Field(None, alias='TZ')
    ua: Ua | None = Field(None, alias='UA')
    ug: Ug | None = Field(None, alias='UG')
    uk: Uk | None = Field(None, alias='UK')
    va: Va | None = Field(None, alias='VA')
    vg: Vg | None = Field(None, alias='VG')
    wf: Wf | None = Field(None, alias='WF')
    xk: Xk | None = Field(None, alias='XK')
    ye: Ye | None = Field(None, alias='YE')
    yt: Yt | None = Field(None, alias='YT')
    yu: Yu | None = Field(None, alias='YU')
    za: Za | None = Field(None, alias='ZA')
    zm: Zm | None = Field(None, alias='ZM')
    zr: Zr | None = Field(None, alias='ZR')
    zw: Zw | None = Field(None, alias='ZW')
    ag: Ag | None = Field(None, alias='AG')
    ar: Ar | None = Field(None, alias='AR')
    bb: Bb | None = Field(None, alias='BB')
    bo: Bo | None = Field(None, alias='BO')
    br: Br | None = Field(None, alias='BR')
    bs: Bs | None = Field(None, alias='BS')
    bz: Bz | None = Field(None, alias='BZ')
    cl: Cl | None = Field(None, alias='CL')
    co: Co | None = Field(None, alias='CO')
    cr: Cr | None = Field(None, alias='CR')
    dm: Dm | None = Field(None, alias='DM')
    do: Do | None = Field(None, alias='DO')
    ec: Ec | None = Field(None, alias='EC')
    gd: Gd | None = Field(None, alias='GD')
    gt: Gt | None = Field(None, alias='GT')
    gy: Gy | None = Field(None, alias='GY')
    hn: Hn | None = Field(None, alias='HN')
    ht: Ht | None = Field(None, alias='HT')
    jm: Jm | None = Field(None, alias='JM')
    kn: Kn | None = Field(None, alias='KN')
    lc: Lc | None = Field(None, alias='LC')
    mx: Mx | None = Field(None, alias='MX')
    ni: Ni | None = Field(None, alias='NI')
    pa: Pa | None = Field(None, alias='PA')
    pe: Pe | None = Field(None, alias='PE')
    py: Py | None = Field(None, alias='PY')
    sr: Sr | None = Field(None, alias='SR')
    sv: Sv | None = Field(None, alias='SV')
    tt: Tt | None = Field(None, alias='TT')
    uy: Uy | None = Field(None, alias='UY')
    vc: Vc | None = Field(None, alias='VC')
    ve: Ve | None = Field(None, alias='VE')
    as_: As | None = Field(None, alias='AS')
    ca: Ca | None = Field(None, alias='CA')
    gu: Gu | None = Field(None, alias='GU')
    mp: Mp | None = Field(None, alias='MP')
    pr: Pr | None = Field(None, alias='PR')
    um: Um | None = Field(None, alias='UM')
    us: Us | None = Field(None, alias='US')
    vi: Vi | None = Field(None, alias='VI')
    yz: Yz | None = Field(None, alias='YZ')
    time_stamp: dict[str, Any] | None = Field(None, alias='timeStamp')

class UseWebPlaybackExperienceOverrides(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    live_linear_playlist_type: str | None = Field(None, alias='liveLinearPlaylistType')

class FeatureConfig137(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    activation_retry_enabled: bool | None = Field(None, alias='activationRetryEnabled')
    commerce_unified_activation_callback_provider_ids: list[str] | None = Field(None, alias='commerceUnifiedActivationCallbackProviderIds')
    commerce_unified_activation_success_enabled_provider_ids: list[str] | None = Field(None, alias='commerceUnifiedActivationSuccessEnabledProviderIds')
    disable_account_delete: bool | None = Field(None, alias='disableAccountDelete')
    disable_account_hold: bool | None = Field(None, alias='disableAccountHold')
    disable_activation: bool | None = Field(None, alias='disableActivation')
    disable_adobe_launch: bool | None = Field(None, alias='disableAdobeLaunch')
    disable_app_settings: bool | None = Field(None, alias='disableAppSettings')
    disable_bam_tech_sdk: bool | None = Field(None, alias='disableBAMTechSDK')
    disable_commerce_refactor: bool | None = Field(None, alias='disableCommerceRefactor')
    disable_content_overrides: bool | None = Field(None, alias='disableContentOverrides')
    disable_early_access_refactor: bool | None = Field(None, alias='disableEarlyAccessRefactor')
    disable_free_trial_fraud: bool | None = Field(None, alias='disableFreeTrialFraud')
    disable_hulu_redirect: bool | None = Field(None, alias='disableHuluRedirect')
    disable_nsb_legacy_hubs: bool | None = Field(None, alias='disableNsbLegacyHubs')
    disable_mega_bundle: bool | None = Field(None, alias='disableMegaBundle')
    disable_o_auth: bool | None = Field(None, alias='disableOAuth')
    disable_one_trust: bool | None = Field(None, alias='disableOneTrust')
    disable_overlay_ad_blurb: bool | None = Field(None, alias='disableOverlayAdBlurb')
    disable_payment_blockage: bool | None = Field(None, alias='disablePaymentBlockage')
    disable_paywall_fallback: bool | None = Field(None, alias='disablePaywallFallback')
    disable_pittsburgh: bool | None = Field(None, alias='disablePittsburgh')
    disable_restart_eligible: bool | None = Field(None, alias='disableRestartEligible')
    disable_tandem_flow: bool | None = Field(None, alias='disableTandemFlow')
    disable_unification: bool | None = Field(None, alias='disableUnification')
    disable_welch: bool | None = Field(None, alias='disableWelch')
    enable_account_price_change_messaging: bool | None = Field(None, alias='enableAccountPriceChangeMessaging')
    enable_amp_weapon_x: bool | None = Field(None, alias='enableAmpWeaponX')
    enable_partner_win_back: bool | None = Field(None, alias='enablePartnerWinBack')
    enable_analytics_validation: bool | None = Field(None, alias='enableAnalyticsValidation')
    enable_braintree_paypal: bool | None = Field(None, alias='enableBraintreePaypal')
    enable_braze: bool | None = Field(None, alias='enableBraze')
    enable_braze_logging: bool | None = Field(None, alias='enableBrazeLogging')
    enable_cancel_stop_gap: bool | None = Field(None, alias='enableCancelStopGap')
    enable_charter_activate_review_page: bool | None = Field(None, alias='enableCharterActivateReviewPage')
    enable_cnbl_footer: bool | None = Field(None, alias='enableCnblFooter')
    enable_nsb_cannonball: bool | None = Field(None, alias='enableNsbCannonball')
    enable_nsb_cannonball_hubs: bool | None = Field(None, alias='enableNsbCannonballHubs')
    enable_commerce_complete_account_info_route: bool | None = Field(None, alias='enableCommerceCompleteAccountInfoRoute')
    enable_commerce_membership_pause: bool | None = Field(None, alias='enableCommerceMembershipPause')
    enable_commerce_price_increase_consent: bool | None = Field(None, alias='enableCommercePriceIncreaseConsent')
    enable_commerce_tiara: bool | None = Field(None, alias='enableCommerceTiara')
    enable_commerce_unified_account_home: bool | None = Field(None, alias='enableCommerceUnifiedAccountHome')
    enable_commerce_unified_activation_route: bool | None = Field(None, alias='enableCommerceUnifiedActivationRoute')
    enable_commerce_unified_activation_success: bool | None = Field(None, alias='enableCommerceUnifiedActivationSuccess')
    enable_commerce_unified_billing_history: bool | None = Field(None, alias='enableCommerceUnifiedBillingHistory')
    enable_commerce_unified_callback_route: bool | None = Field(None, alias='enableCommerceUnifiedCallbackRoute')
    enable_commerce_unified_cancel_contract_route: bool | None = Field(None, alias='enableCommerceUnifiedCancelContractRoute')
    enable_commerce_unified_cancel_route: bool | None = Field(None, alias='enableCommerceUnifiedCancelRoute')
    enable_commerce_unified_cancel_landing_route: bool | None = Field(None, alias='enableCommerceUnifiedCancelLandingRoute')
    enable_commerce_unified_change_subscription: bool | None = Field(None, alias='enableCommerceUnifiedChangeSubscription')
    enable_commerce_unified_extra_member: bool | None = Field(None, alias='enableCommerceUnifiedExtraMember')
    enable_commerce_unified_extra_member_access_route: bool | None = Field(None, alias='enableCommerceUnifiedExtraMemberAccessRoute')
    enable_commerce_unified_outgoing_activation_route: bool | None = Field(None, alias='enableCommerceUnifiedOutgoingActivationRoute')
    enable_commerce_unified_plans: bool | None = Field(None, alias='enableCommerceUnifiedPlans')
    enable_commerce_unified_signup_flow: bool | None = Field(None, alias='enableCommerceUnifiedSignupFlow')
    enable_commerce_unified_redemption: bool | None = Field(None, alias='enableCommerceUnifiedRedemption')
    enable_commerce_unified_welcome_back: bool | None = Field(None, alias='enableCommerceUnifiedWelcomeBack')
    enable_commerce_v2_dob: bool | None = Field(None, alias='enableCommerceV2DOB')
    enable_dictionary_draft_state: bool | None = Field(None, alias='enableDictionaryDraftState')
    enable_dob_collection_legal_copy: bool | None = Field(None, alias='enableDOBCollectionLegalCopy')
    enable_explore_api_for_hubs: bool | None = Field(None, alias='enableExploreApiForHubs')
    enable_explore_nsb_redirect_to_browse: bool | None = Field(None, alias='enableExploreNsbRedirectToBrowse')
    enable_explore_page: bool | None = Field(None, alias='enableExplorePage')
    enable_explore_us: bool | None = Field(None, alias='enableExploreUs')
    enable_explore_api_for_nsb: bool | None = Field(None, alias='enableExploreApiForNsb')
    enable_flex_powered_activation_success_screen: bool | None = Field(None, alias='enableFlexPoweredActivationSuccessScreen')
    enable_gift_card: bool | None = Field(None, alias='enableGiftCard')
    enable_global_footer: bool | None = Field(None, alias='enableGlobalFooter')
    enable_global_identity_unbranded_create_account: bool | None = Field(None, alias='enableGlobalIdentityUnbrandedCreateAccount')
    enable_global_identity_unbranded_credentials_update: bool | None = Field(None, alias='enableGlobalIdentityUnbrandedCredentialsUpdate')
    enable_identity_consent_sync: bool | None = Field(None, alias='enableIdentityConsentSync')
    enable_identity_create_account_route: bool | None = Field(None, alias='enableIdentityCreateAccountRoute')
    enable_identity_magic_link_route: bool | None = Field(None, alias='enableIdentityMagicLinkRoute')
    enable_identity_manage_devices_route: bool | None = Field(None, alias='enableIdentityManageDevicesRoute')
    enable_identity_o_auth_review_terms_route: bool | None = Field(None, alias='enableIdentityOAuthReviewTermsRoute')
    enable_identity_one_id_authentication: bool | None = Field(None, alias='enableIdentityOneIdAuthentication')
    enable_identity_review_and_accept_route: bool | None = Field(None, alias='enableIdentityReviewAndAcceptRoute')
    enable_identity_unified_auth_flows: bool | None = Field(None, alias='enableIdentityUnifiedAuthFlows')
    enable_identity_unified_account_delete: bool | None = Field(None, alias='enableIdentityUnifiedAccountDelete')
    enable_identity_unified_license_plate_flow: bool | None = Field(None, alias='enableIdentityUnifiedLicensePlateFlow')
    enable_identity_verify_route: bool | None = Field(None, alias='enableIdentityVerifyRoute')
    enable_identity_unified_nielsen_route: bool | None = Field(None, alias='enableIdentityUnifiedNielsenRoute')
    enable_individual_date_replaces: bool | None = Field(None, alias='enableIndividualDateReplaces')
    enable_inline_wpnx_experimentation: bool | None = Field(None, alias='enableInlineWPNXExperimentation')
    enable_nsb_commerce_plans_cta: bool | None = Field(None, alias='enableNsbCommercePlansCta')
    enable_onboarding_existing_users: bool | None = Field(None, alias='enableOnboardingExistingUsers')
    enable_profiles_linking_route: bool | None = Field(None, alias='enableProfilesLinkingRoute')
    enable_profiles_loading_route: bool | None = Field(None, alias='enableProfilesLoadingRoute')
    enable_profiles_routes: bool | None = Field(None, alias='enableProfilesRoutes')
    enable_profiles_setup_route: bool | None = Field(None, alias='enableProfilesSetupRoute')
    enable_privacy_consent_package: bool | None = Field(None, alias='enablePrivacyConsentPackage')
    enable_regulated_cancellation: bool | None = Field(None, alias='enableRegulatedCancellation')
    enable_unauth_sub_id_cancellation: bool | None = Field(None, alias='enableUnauthSubIdCancellation')
    enable_redux_logging: bool | None = Field(None, alias='enableReduxLogging')
    enable_redux_dev_tools: bool | None = Field(None, alias='enableReduxDevTools')
    enable_restart_eligible_for_world: bool | None = Field(None, alias='enableRestartEligibleForWorld')
    enable_roku_rpm_cancel_switch: bool | None = Field(None, alias='enableRokuRPMCancelSwitch')
    enable_should_use_legacy_sash: bool | None = Field(None, alias='enableShouldUseLegacySASH')
    enable_sign_up_flow_add_ons_route: bool | None = Field(None, alias='enableSignUpFlowAddOnsRoute')
    enable_sign_up_flow_cadence_route: bool | None = Field(None, alias='enableSignUpFlowCadenceRoute')
    enable_tenant_specific_header: bool | None = Field(None, alias='enableTenantSpecificHeader')
    enable_update_credentials_route: bool | None = Field(None, alias='enableUpdateCredentialsRoute')
    env: str | None = None
    live_selection_modal_enabled: bool | None = Field(None, alias='liveSelectionModalEnabled')
    unified_billing_history_rollout: str | None = Field(None, alias='unifiedBillingHistoryRollout')
    use_web_playback_experience_overrides: UseWebPlaybackExperienceOverrides | None = Field(None, alias='useWebPlaybackExperienceOverrides')
    enable_license_plate_dynamic_routes: bool | None = Field(None, alias='enableLicensePlateDynamicRoutes')
    enable_taste_picking_route: bool | None = Field(None, alias='enableTastePickingRoute')
    enable_spaceball_explore: bool | None = Field(None, alias='enableSpaceballExplore')
    enable_spaceball_mlp: bool | None = Field(None, alias='enableSpaceballMlp')
    enable_spaceball_whats_on: bool | None = Field(None, alias='enableSpaceballWhatsOn')

class AppLangMap(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ar_ae: str | None = Field(None, alias='ar-ae')
    ar_ar: str | None = Field(None, alias='ar-ar')
    ar_bh: str | None = Field(None, alias='ar-bh')
    ar_dz: str | None = Field(None, alias='ar-dz')
    ar_eg: str | None = Field(None, alias='ar-eg')
    ar_iq: str | None = Field(None, alias='ar-iq')
    ar_jo: str | None = Field(None, alias='ar-jo')
    ar_kw: str | None = Field(None, alias='ar-kw')
    ar_lb: str | None = Field(None, alias='ar-lb')
    ar_ma: str | None = Field(None, alias='ar-ma')
    ar_om: str | None = Field(None, alias='ar-om')
    ar_ps: str | None = Field(None, alias='ar-ps')
    ar_qa: str | None = Field(None, alias='ar-qa')
    ar_sa: str | None = Field(None, alias='ar-sa')
    ar_tn: str | None = Field(None, alias='ar-tn')
    bg_bg: str | None = Field(None, alias='bg-bg')
    cs_cz: str | None = Field(None, alias='cs-cz')
    da_dk: str | None = Field(None, alias='da-dk')
    da_fo: str | None = Field(None, alias='da-fo')
    da_gl: str | None = Field(None, alias='da-gl')
    de_at: str | None = Field(None, alias='de-at')
    de_ch: str | None = Field(None, alias='de-ch')
    de_de: str | None = Field(None, alias='de-de')
    de_li: str | None = Field(None, alias='de-li')
    de_lu: str | None = Field(None, alias='de-lu')
    el_gr: str | None = Field(None, alias='el-gr')
    en: str | None = None
    en_ad: str | None = Field(None, alias='en-ad')
    en_ae: str | None = Field(None, alias='en-ae')
    en_ag: str | None = Field(None, alias='en-ag')
    en_ai: str | None = Field(None, alias='en-ai')
    en_al: str | None = Field(None, alias='en-al')
    en_ar: str | None = Field(None, alias='en-ar')
    en_as: str | None = Field(None, alias='en-as')
    en_at: str | None = Field(None, alias='en-at')
    en_au: str | None = Field(None, alias='en-au')
    en_aw: str | None = Field(None, alias='en-aw')
    en_ax: str | None = Field(None, alias='en-ax')
    en_ba: str | None = Field(None, alias='en-ba')
    en_bb: str | None = Field(None, alias='en-bb')
    en_be: str | None = Field(None, alias='en-be')
    en_bg: str | None = Field(None, alias='en-bg')
    en_bh: str | None = Field(None, alias='en-bh')
    en_bm: str | None = Field(None, alias='en-bm')
    en_bo: str | None = Field(None, alias='en-bo')
    en_bq: str | None = Field(None, alias='en-bq')
    en_br: str | None = Field(None, alias='en-br')
    en_bs: str | None = Field(None, alias='en-bs')
    en_bz: str | None = Field(None, alias='en-bz')
    en_ca: str | None = Field(None, alias='en-ca')
    en_cc: str | None = Field(None, alias='en-cc')
    en_ch: str | None = Field(None, alias='en-ch')
    en_ck: str | None = Field(None, alias='en-ck')
    en_cl: str | None = Field(None, alias='en-cl')
    en_co: str | None = Field(None, alias='en-co')
    en_cr: str | None = Field(None, alias='en-cr')
    en_cw: str | None = Field(None, alias='en-cw')
    en_cx: str | None = Field(None, alias='en-cx')
    en_cz: str | None = Field(None, alias='en-cz')
    en_de: str | None = Field(None, alias='en-de')
    en_dk: str | None = Field(None, alias='en-dk')
    en_dm: str | None = Field(None, alias='en-dm')
    en_dz: str | None = Field(None, alias='en-dz')
    en_do: str | None = Field(None, alias='en-do')
    en_ec: str | None = Field(None, alias='en-ec')
    en_ee: str | None = Field(None, alias='en-ee')
    en_eg: str | None = Field(None, alias='en-eg')
    en_es: str | None = Field(None, alias='en-es')
    en_fi: str | None = Field(None, alias='en-fi')
    en_fk: str | None = Field(None, alias='en-fk')
    en_fo: str | None = Field(None, alias='en-fo')
    en_fr: str | None = Field(None, alias='en-fr')
    en_gb: str | None = Field(None, alias='en-gb')
    en_gd: str | None = Field(None, alias='en-gd')
    en_gi: str | None = Field(None, alias='en-gi')
    en_gl: str | None = Field(None, alias='en-gl')
    en_gr: str | None = Field(None, alias='en-gr')
    en_gs: str | None = Field(None, alias='en-gs')
    en_gt: str | None = Field(None, alias='en-gt')
    en_gu: str | None = Field(None, alias='en-gu')
    en_gy: str | None = Field(None, alias='en-gy')
    en_hk: str | None = Field(None, alias='en-hk')
    en_hn: str | None = Field(None, alias='en-hn')
    en_hr: str | None = Field(None, alias='en-hr')
    en_ht: str | None = Field(None, alias='en-ht')
    en_hu: str | None = Field(None, alias='en-hu')
    en_id: str | None = Field(None, alias='en-id')
    en_ie: str | None = Field(None, alias='en-ie')
    en_il: str | None = Field(None, alias='en-il')
    en_io: str | None = Field(None, alias='en-io')
    en_iq: str | None = Field(None, alias='en-iq')
    en_is: str | None = Field(None, alias='en-is')
    en_it: str | None = Field(None, alias='en-it')
    en_jm: str | None = Field(None, alias='en-jm')
    en_jo: str | None = Field(None, alias='en-jo')
    en_jp: str | None = Field(None, alias='en-jp')
    en_kn: str | None = Field(None, alias='en-kn')
    en_kr: str | None = Field(None, alias='en-kr')
    en_kw: str | None = Field(None, alias='en-kw')
    en_ky: str | None = Field(None, alias='en-ky')
    en_lb: str | None = Field(None, alias='en-lb')
    en_lc: str | None = Field(None, alias='en-lc')
    en_li: str | None = Field(None, alias='en-li')
    en_lt: str | None = Field(None, alias='en-lt')
    en_lu: str | None = Field(None, alias='en-lu')
    en_lv: str | None = Field(None, alias='en-lv')
    en_ma: str | None = Field(None, alias='en-ma')
    en_me: str | None = Field(None, alias='en-me')
    en_mh: str | None = Field(None, alias='en-mh')
    en_mk: str | None = Field(None, alias='en-mk')
    en_mp: str | None = Field(None, alias='en-mp')
    en_ms: str | None = Field(None, alias='en-ms')
    en_mt: str | None = Field(None, alias='en-mt')
    en_mx: str | None = Field(None, alias='en-mx')
    en_my: str | None = Field(None, alias='en-my')
    en_nf: str | None = Field(None, alias='en-nf')
    en_ni: str | None = Field(None, alias='en-ni')
    en_nl: str | None = Field(None, alias='en-nl')
    en_no: str | None = Field(None, alias='en-no')
    en_nu: str | None = Field(None, alias='en-nu')
    en_th: str | None = Field(None, alias='en-th')
    en_nz: str | None = Field(None, alias='en-nz')
    en_om: str | None = Field(None, alias='en-om')
    en_pa: str | None = Field(None, alias='en-pa')
    en_pe: str | None = Field(None, alias='en-pe')
    en_pf: str | None = Field(None, alias='en-pf')
    en_ph: str | None = Field(None, alias='en-ph')
    en_pl: str | None = Field(None, alias='en-pl')
    en_pm: str | None = Field(None, alias='en-pm')
    en_pn: str | None = Field(None, alias='en-pn')
    en_pr: str | None = Field(None, alias='en-pr')
    en_ps: str | None = Field(None, alias='en-ps')
    en_pt: str | None = Field(None, alias='en-pt')
    en_qa: str | None = Field(None, alias='en-qa')
    en_py: str | None = Field(None, alias='en-py')
    en_ro: str | None = Field(None, alias='en-ro')
    en_rs: str | None = Field(None, alias='en-rs')
    en_sa: str | None = Field(None, alias='en-sa')
    en_se: str | None = Field(None, alias='en-se')
    en_sh: str | None = Field(None, alias='en-sh')
    en_si: str | None = Field(None, alias='en-si')
    en_sj: str | None = Field(None, alias='en-sj')
    en_sk: str | None = Field(None, alias='en-sk')
    en_sm: str | None = Field(None, alias='en-sm')
    en_sr: str | None = Field(None, alias='en-sr')
    en_sv: str | None = Field(None, alias='en-sv')
    en_sx: str | None = Field(None, alias='en-sx')
    en_tc: str | None = Field(None, alias='en-tc')
    en_tf: str | None = Field(None, alias='en-tf')
    en_tk: str | None = Field(None, alias='en-tk')
    en_tn: str | None = Field(None, alias='en-tn')
    en_tr: str | None = Field(None, alias='en-tr')
    en_tt: str | None = Field(None, alias='en-tt')
    en_tw: str | None = Field(None, alias='en-tw')
    en_um: str | None = Field(None, alias='en-um')
    en_uy: str | None = Field(None, alias='en-uy')
    en_va: str | None = Field(None, alias='en-va')
    en_vc: str | None = Field(None, alias='en-vc')
    en_ve: str | None = Field(None, alias='en-ve')
    en_vg: str | None = Field(None, alias='en-vg')
    en_za: str | None = Field(None, alias='en-za')
    es_ad: str | None = Field(None, alias='es-ad')
    es_ar: str | None = Field(None, alias='es-ar')
    es_bo: str | None = Field(None, alias='es-bo')
    es_cl: str | None = Field(None, alias='es-cl')
    es_co: str | None = Field(None, alias='es-co')
    es_cr: str | None = Field(None, alias='es-cr')
    es_do: str | None = Field(None, alias='es-do')
    es_ec: str | None = Field(None, alias='es-ec')
    es_es: str | None = Field(None, alias='es-es')
    es_gt: str | None = Field(None, alias='es-gt')
    es_hn: str | None = Field(None, alias='es-hn')
    es_mx: str | None = Field(None, alias='es-mx')
    es_ni: str | None = Field(None, alias='es-ni')
    es_pa: str | None = Field(None, alias='es-pa')
    es_pe: str | None = Field(None, alias='es-pe')
    es_py: str | None = Field(None, alias='es-py')
    es_sv: str | None = Field(None, alias='es-sv')
    es_us: str | None = Field(None, alias='es-us')
    es_uy: str | None = Field(None, alias='es-uy')
    es_ve: str | None = Field(None, alias='es-ve')
    es_xl: str | None = Field(None, alias='es-xl')
    fi_ax: str | None = Field(None, alias='fi-ax')
    fi_fi: str | None = Field(None, alias='fi-fi')
    fr_ad: str | None = Field(None, alias='fr-ad')
    fr_be: str | None = Field(None, alias='fr-be')
    fr_bl: str | None = Field(None, alias='fr-bl')
    fr_ca: str | None = Field(None, alias='fr-ca')
    fr_ch: str | None = Field(None, alias='fr-ch')
    fr_fr: str | None = Field(None, alias='fr-fr')
    fr_gf: str | None = Field(None, alias='fr-gf')
    fr_gp: str | None = Field(None, alias='fr-gp')
    fr_ht: str | None = Field(None, alias='fr-ht')
    fr_lu: str | None = Field(None, alias='fr-lu')
    fr_mc: str | None = Field(None, alias='fr-mc')
    fr_mf: str | None = Field(None, alias='fr-mf')
    fr_mq: str | None = Field(None, alias='fr-mq')
    fr_mu: str | None = Field(None, alias='fr-mu')
    fr_nc: str | None = Field(None, alias='fr-nc')
    fr_pf: str | None = Field(None, alias='fr-pf')
    fr_pm: str | None = Field(None, alias='fr-pm')
    fr_re: str | None = Field(None, alias='fr-re')
    fr_sx: str | None = Field(None, alias='fr-sx')
    fr_tf: str | None = Field(None, alias='fr-tf')
    fr_wf: str | None = Field(None, alias='fr-wf')
    fr_yt: str | None = Field(None, alias='fr-yt')
    he_il: str | None = Field(None, alias='he-il')
    hr_ba: str | None = Field(None, alias='hr-ba')
    hr_hr: str | None = Field(None, alias='hr-hr')
    hu_hu: str | None = Field(None, alias='hu-hu')
    id_id: str | None = Field(None, alias='id-id')
    it_ch: str | None = Field(None, alias='it-ch')
    it_it: str | None = Field(None, alias='it-it')
    it_sm: str | None = Field(None, alias='it-sm')
    it_va: str | None = Field(None, alias='it-va')
    ja_jp: str | None = Field(None, alias='ja-jp')
    ko_kr: str | None = Field(None, alias='ko-kr')
    ms_my: str | None = Field(None, alias='ms-my')
    nb_no: str | None = Field(None, alias='nb-no')
    no_no: str | None = Field(None, alias='no-no')
    nb_sj: str | None = Field(None, alias='nb-sj')
    nl_aw: str | None = Field(None, alias='nl-aw')
    nl_be: str | None = Field(None, alias='nl-be')
    nl_bq: str | None = Field(None, alias='nl-bq')
    nl_cw: str | None = Field(None, alias='nl-cw')
    nl_nl: str | None = Field(None, alias='nl-nl')
    nl_sr: str | None = Field(None, alias='nl-sr')
    nl_sx: str | None = Field(None, alias='nl-sx')
    pl_pl: str | None = Field(None, alias='pl-pl')
    pt_br: str | None = Field(None, alias='pt-br')
    pt_pt: str | None = Field(None, alias='pt-pt')
    ro_ro: str | None = Field(None, alias='ro-ro')
    sk_sk: str | None = Field(None, alias='sk-sk')
    sv_ax: str | None = Field(None, alias='sv-ax')
    sv_fi: str | None = Field(None, alias='sv-fi')
    sv_se: str | None = Field(None, alias='sv-se')
    th_th: str | None = Field(None, alias='th-th')
    tr_tr: str | None = Field(None, alias='tr-tr')
    vi_vn: str | None = Field(None, alias='vi-vn')
    zh_hk: str | None = Field(None, alias='zh-hk')
    zh_sg: str | None = Field(None, alias='zh-sg')
    zh_tw: str | None = Field(None, alias='zh-tw')

class AnnualStandaloneHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class AnnualStandaloneToggle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class AnnualStarPlus(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class BundleDefault(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class BundleNoah(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class BundleNoahHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class BundleSash(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class BundleSashHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class CancelSubscription(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class ComboPlus(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class CraveBundlePremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class CraveBundleStandardWithAds(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class DisneyHulu(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipAdsBundleAddOns(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipAdsBundleBilling(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipAdsBundleBillingOfferId(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipAdsBundleBillingOfferId2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipAdsBundleBillingOfferId3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipAdsBundleBillingOfferId4(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipBundlePremiumRetailWildcat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipBundlePremiumWildcat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipBundlePromoWildcat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipBundleRetailWildcat(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipNoAdsBundleAddOns(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class FlagshipNoAdsBundleBilling(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class Login(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MaxAdsBundleAddOns(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MaxAdsBundleflagship(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MaxBundleBasic(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MaxBundlePremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MaxNoAdsBundleAddOns(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MaxNoAdsBundleflagship(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MonthlyStandalone(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MonthlyStandaloneHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MonthlyStandaloneNoah(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MonthlyStandaloneSash(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class MonthlyStandaloneToggle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class PlanSelectCommercePlans(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class PlanSelectIdentitySignup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class Signup1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class TsnBundleStandardWithAds(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class TsnBundleStandardNoAds(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class TsnBundlePremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class TsnCraveBundleStandardWithAds(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class TsnCraveBundlePremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufAnnualStandalonePremiumCo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufAnnualStandalonePremiumHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufAnnualStandalonePremiumToggle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufAnnualStandaloneStandardCo(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufBundlePremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufBundlePremiumHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufBundleTrioBasic(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufBundleTrioBasicDefault(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufBundleTrioBasicHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDisneyAnnualStandardHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDisneyAnnualStandardToggle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDisneyMonthlyBasic(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDisneyMonthlyPremiumToggle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDisneyMonthlyStandardHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDisneyMonthlyStandardToggle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDuoBasic(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufDuoPremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufLogin(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufMonthlyStandalone(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufMonthlyStandaloneBasic(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufMonthlyStandalonePremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufMonthlyStandalonePremiumHidden(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufMonthlyStandalonePremiumToggle(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class UsufSignup(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class VenuBundleBasic(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class VenuBundlePremium(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    url: str | None = None
    glimpse_name: str | None = Field(None, alias='glimpseName')

class CannonballLinkManager1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    annual_standalone_hidden: AnnualStandaloneHidden | None = Field(None, alias='annualStandaloneHidden')
    annual_standalone_toggle: AnnualStandaloneToggle | None = Field(None, alias='annualStandaloneToggle')
    annual_star_plus: AnnualStarPlus | None = Field(None, alias='annualStarPlus')
    bundle_default: BundleDefault | None = Field(None, alias='bundleDefault')
    bundle_noah: BundleNoah | None = Field(None, alias='bundleNoah')
    bundle_noah_hidden: BundleNoahHidden | None = Field(None, alias='bundleNoahHidden')
    bundle_sash: BundleSash | None = Field(None, alias='bundleSash')
    bundle_sash_hidden: BundleSashHidden | None = Field(None, alias='bundleSashHidden')
    cancel_subscription: CancelSubscription | None = Field(None, alias='cancelSubscription')
    combo_plus: ComboPlus | None = Field(None, alias='comboPlus')
    crave_bundle_premium: CraveBundlePremium | None = Field(None, alias='craveBundlePremium')
    crave_bundle_standard_with_ads: CraveBundleStandardWithAds | None = Field(None, alias='craveBundleStandardWithAds')
    disney_hulu: DisneyHulu | None = Field(None, alias='disneyHulu')
    flagship_ads_bundle_add_ons: FlagshipAdsBundleAddOns | None = Field(None, alias='flagshipAdsBundleAddOns')
    flagship_ads_bundle_billing: FlagshipAdsBundleBilling | None = Field(None, alias='flagshipAdsBundleBilling')
    flagship_ads_bundle_billing_offer_id: FlagshipAdsBundleBillingOfferId | None = Field(None, alias='flagshipAdsBundleBillingOfferId')
    flagship_ads_bundle_billing_offer_id2: FlagshipAdsBundleBillingOfferId2 | None = Field(None, alias='flagshipAdsBundleBillingOfferId2')
    flagship_ads_bundle_billing_offer_id3: FlagshipAdsBundleBillingOfferId3 | None = Field(None, alias='flagshipAdsBundleBillingOfferId3')
    flagship_ads_bundle_billing_offer_id4: FlagshipAdsBundleBillingOfferId4 | None = Field(None, alias='flagshipAdsBundleBillingOfferId4')
    flagship_bundle_premium_retail_wildcat: FlagshipBundlePremiumRetailWildcat | None = Field(None, alias='flagshipBundlePremiumRetailWildcat')
    flagship_bundle_premium_wildcat: FlagshipBundlePremiumWildcat | None = Field(None, alias='flagshipBundlePremiumWildcat')
    flagship_bundle_promo_wildcat: FlagshipBundlePromoWildcat | None = Field(None, alias='flagshipBundlePromoWildcat')
    flagship_bundle_retail_wildcat: FlagshipBundleRetailWildcat | None = Field(None, alias='flagshipBundleRetailWildcat')
    flagship_no_ads_bundle_add_ons: FlagshipNoAdsBundleAddOns | None = Field(None, alias='flagshipNoAdsBundleAddOns')
    flagship_no_ads_bundle_billing: FlagshipNoAdsBundleBilling | None = Field(None, alias='flagshipNoAdsBundleBilling')
    login: Login | None = None
    max_ads_bundle_add_ons: MaxAdsBundleAddOns | None = Field(None, alias='maxAdsBundleAddOns')
    max_ads_bundleflagship: MaxAdsBundleflagship | None = Field(None, alias='maxAdsBundleflagship')
    max_bundle_basic: MaxBundleBasic | None = Field(None, alias='maxBundleBasic')
    max_bundle_premium: MaxBundlePremium | None = Field(None, alias='maxBundlePremium')
    max_no_ads_bundle_add_ons: MaxNoAdsBundleAddOns | None = Field(None, alias='maxNoAdsBundleAddOns')
    max_no_ads_bundleflagship: MaxNoAdsBundleflagship | None = Field(None, alias='maxNoAdsBundleflagship')
    monthly_standalone: MonthlyStandalone | None = Field(None, alias='monthlyStandalone')
    monthly_standalone_hidden: MonthlyStandaloneHidden | None = Field(None, alias='monthlyStandaloneHidden')
    monthly_standalone_noah: MonthlyStandaloneNoah | None = Field(None, alias='monthlyStandaloneNoah')
    monthly_standalone_sash: MonthlyStandaloneSash | None = Field(None, alias='monthlyStandaloneSash')
    monthly_standalone_toggle: MonthlyStandaloneToggle | None = Field(None, alias='monthlyStandaloneToggle')
    plan_select_commerce_plans: PlanSelectCommercePlans | None = Field(None, alias='planSelectCommercePlans')
    plan_select_identity_signup: PlanSelectIdentitySignup | None = Field(None, alias='planSelectIdentitySignup')
    signup: Signup1 | None = None
    tsn_bundle_standard_with_ads: TsnBundleStandardWithAds | None = Field(None, alias='tsnBundleStandardWithAds')
    tsn_bundle_standard_no_ads: TsnBundleStandardNoAds | None = Field(None, alias='tsnBundleStandardNoAds')
    tsn_bundle_premium: TsnBundlePremium | None = Field(None, alias='tsnBundlePremium')
    tsn_crave_bundle_standard_with_ads: TsnCraveBundleStandardWithAds | None = Field(None, alias='tsnCraveBundleStandardWithAds')
    tsn_crave_bundle_premium: TsnCraveBundlePremium | None = Field(None, alias='tsnCraveBundlePremium')
    usuf_annual_standalone_premium_co: UsufAnnualStandalonePremiumCo | None = Field(None, alias='usufAnnualStandalonePremiumCO')
    usuf_annual_standalone_premium_hidden: UsufAnnualStandalonePremiumHidden | None = Field(None, alias='usufAnnualStandalonePremiumHidden')
    usuf_annual_standalone_premium_toggle: UsufAnnualStandalonePremiumToggle | None = Field(None, alias='usufAnnualStandalonePremiumToggle')
    usuf_annual_standalone_standard_co: UsufAnnualStandaloneStandardCo | None = Field(None, alias='usufAnnualStandaloneStandardCO')
    usuf_bundle_premium: UsufBundlePremium | None = Field(None, alias='usufBundlePremium')
    usuf_bundle_premium_hidden: UsufBundlePremiumHidden | None = Field(None, alias='usufBundlePremiumHidden')
    usuf_bundle_trio_basic: UsufBundleTrioBasic | None = Field(None, alias='usufBundleTrioBasic')
    usuf_bundle_trio_basic_default: UsufBundleTrioBasicDefault | None = Field(None, alias='usufBundleTrioBasicDefault')
    usuf_bundle_trio_basic_hidden: UsufBundleTrioBasicHidden | None = Field(None, alias='usufBundleTrioBasicHidden')
    usuf_disney_annual_standard_hidden: UsufDisneyAnnualStandardHidden | None = Field(None, alias='usufDisneyAnnualStandardHidden')
    usuf_disney_annual_standard_toggle: UsufDisneyAnnualStandardToggle | None = Field(None, alias='usufDisneyAnnualStandardToggle')
    usuf_disney_monthly_basic: UsufDisneyMonthlyBasic | None = Field(None, alias='usufDisneyMonthlyBasic')
    usuf_disney_monthly_premium_toggle: UsufDisneyMonthlyPremiumToggle | None = Field(None, alias='usufDisneyMonthlyPremiumToggle')
    usuf_disney_monthly_standard_hidden: UsufDisneyMonthlyStandardHidden | None = Field(None, alias='usufDisneyMonthlyStandardHidden')
    usuf_disney_monthly_standard_toggle: UsufDisneyMonthlyStandardToggle | None = Field(None, alias='usufDisneyMonthlyStandardToggle')
    usuf_duo_basic: UsufDuoBasic | None = Field(None, alias='usufDuoBasic')
    usuf_duo_premium: UsufDuoPremium | None = Field(None, alias='usufDuoPremium')
    usuf_login: UsufLogin | None = Field(None, alias='usufLogin')
    usuf_monthly_standalone: UsufMonthlyStandalone | None = Field(None, alias='usufMonthlyStandalone')
    usuf_monthly_standalone_basic: UsufMonthlyStandaloneBasic | None = Field(None, alias='usufMonthlyStandaloneBasic')
    usuf_monthly_standalone_premium: UsufMonthlyStandalonePremium | None = Field(None, alias='usufMonthlyStandalonePremium')
    usuf_monthly_standalone_premium_hidden: UsufMonthlyStandalonePremiumHidden | None = Field(None, alias='usufMonthlyStandalonePremiumHidden')
    usuf_monthly_standalone_premium_toggle: UsufMonthlyStandalonePremiumToggle | None = Field(None, alias='usufMonthlyStandalonePremiumToggle')
    usuf_signup: UsufSignup | None = Field(None, alias='usufSignup')
    venu_bundle_basic: VenuBundleBasic | None = Field(None, alias='venuBundleBasic')
    venu_bundle_premium: VenuBundlePremium | None = Field(None, alias='venuBundlePremium')

class Paths(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    stage: str | None = None
    stage_preview: str | None = Field(None, alias='stagePreview')
    prod: str | None = None
    preview: str | None = None

class Lps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    environment: str | None = None
    organization: str | None = None
    space: str | None = None
    available_environments: list[str] | None = Field(None, alias='availableEnvironments')

class Explore(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    environment: str | None = None
    organization: str | None = None
    space: str | None = None
    available_environments: list[str] | None = Field(None, alias='availableEnvironments')

class ExploreFamily(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    environment: str | None = None
    organization: str | None = None
    space: str | None = None
    available_environments: list[str] | None = Field(None, alias='availableEnvironments')

class Instances(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    lps: Lps | None = None
    explore: Explore | None = None
    explore_family: ExploreFamily | None = Field(None, alias='exploreFamily')

class Cannonball(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cdn_manifest_domain: str | None = Field(None, alias='cdnManifestDomain')
    preview_manifest_domain: str | None = Field(None, alias='previewManifestDomain')
    environment: str | None = None
    organization: str | None = None
    space: str | None = None
    paths: Paths | None = None
    instances: Instances | None = None

class Paths1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    stage: str | None = None
    prod: str | None = None
    preview: str | None = None
    stage_preview: str | None = Field(None, alias='stagePreview')

class Explore1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    organization: str | None = None
    space: str | None = None
    environment: str | None = None
    available_environments: list[str] | None = Field(None, alias='availableEnvironments')

class Global(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    organization: str | None = None
    space: str | None = None
    environment: str | None = None
    available_environments: list[str] | None = Field(None, alias='availableEnvironments')

class Instances1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    explore: Explore1 | None = None
    global_: Global | None = Field(None, alias='global')
    lps: Lps | None = None
    explore_family: ExploreFamily | None = Field(None, alias='exploreFamily')

class Spaceball(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    paths: Paths1 | None = None
    instances: Instances1 | None = None

class Af1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing152(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Purchase85(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class DefaultProduct84(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce134(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct84 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Au1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing152 | None = None
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')
    commerce: Commerce134 | None = None

class Bd1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Bn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Bt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Bu1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing153(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig138(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Commerce135(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cc1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing153 | None = None
    feature_config: FeatureConfig138 | None = Field(None, alias='featureConfig')
    commerce: Commerce135 | None = None

class Commerce136(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ck1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing153 | None = None
    feature_config: FeatureConfig138 | None = Field(None, alias='featureConfig')
    commerce: Commerce136 | None = None

class Cn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Fj1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing155(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig140(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct85(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce137(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct85 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Hk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing155 | None = None
    feature_config: FeatureConfig140 | None = Field(None, alias='featureConfig')
    commerce: Commerce137 | None = None

class Hm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Id1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing155 | None = None

class In1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct86(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce138(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct86 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Jp1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing155 | None = None
    feature_config: FeatureConfig140 | None = Field(None, alias='featureConfig')
    commerce: Commerce138 | None = None

class Kh1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ki1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig142(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')
    enable_age_verification: bool | None = Field(None, alias='enableAgeVerification')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct87(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu5 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce139(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    card_options_popover_enabled: bool | None = Field(None, alias='cardOptionsPopoverEnabled')
    default_product: DefaultProduct87 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    minimum_age_to_subscribe: int | None = Field(None, alias='minimumAgeToSubscribe')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Kr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing155 | None = None
    feature_config: FeatureConfig142 | None = Field(None, alias='featureConfig')
    commerce: Commerce139 | None = None

class La1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Lk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class My1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing155 | None = None

class Marketing160(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig143(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Commerce140(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Nf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing160 | None = None
    feature_config: FeatureConfig143 | None = Field(None, alias='featureConfig')
    commerce: Commerce140 | None = None

class Np1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Nr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce141(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Nu89(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing160 | None = None
    feature_config: FeatureConfig143 | None = Field(None, alias='featureConfig')
    commerce: Commerce141 | None = None

class Marketing162(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Nu90(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    campaign_code: str | None = Field(None, alias='campaignCode')
    sku_list: list[str] | None = Field(None, alias='skuList')
    voucher_code: str | None = Field(None, alias='voucherCode')

class DefaultProduct88(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce142(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct88 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Nz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing162 | None = None
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')
    commerce: Commerce142 | None = None

class Pg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ph1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing162 | None = None

class Pk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sb1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig145(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')

class DefaultProduct89(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce143(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct89 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Sg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing162 | None = None
    feature_config: FeatureConfig145 | None = Field(None, alias='featureConfig')
    commerce: Commerce143 | None = None

class Th1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing162 | None = None

class Marketing166(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig146(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Commerce144(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing166 | None = None
    feature_config: FeatureConfig146 | None = Field(None, alias='featureConfig')
    commerce: Commerce144 | None = None

class Tl1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class To1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Tp1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Tv2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing167(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig147(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_rights_reserved_year: bool | None = Field(None, alias='displayRightsReservedYear')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct90(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce145(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct90 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_e_guid: bool | None = Field(None, alias='requiresEGuid')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing167 | None = None
    feature_config: FeatureConfig147 | None = Field(None, alias='featureConfig')
    commerce: Commerce145 | None = None

class Vn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Vu1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ws1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig148(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct91(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce146(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct91 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ad1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing167 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce146 | None = None

class Ae1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing167 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')

class Commerce147(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ai1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing167 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce147 | None = None

class DefaultProduct92(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce148(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct92 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Al1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing167 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce148 | None = None

class Am1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class An1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ao1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct93(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce149(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct93 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class At1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing167 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce149 | None = None

class Commerce150(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Aw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing167 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce150 | None = None

class Marketing174(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce151(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ax1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing174 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce151 | None = None

class Marketing175(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct94(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce152(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct94 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ba1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing175 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce152 | None = None

class DefaultProduct95(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce153(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct95 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Be1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing175 | None = None
    feature_config: FeatureConfig148 | None = Field(None, alias='featureConfig')
    commerce: Commerce153 | None = None

class Bf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig157(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class DefaultProduct96(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce154(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    local_price_enabled: bool | None = Field(None, alias='localPriceEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct96 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing175 | None = None
    feature_config: FeatureConfig157 | None = Field(None, alias='featureConfig')
    commerce: Commerce154 | None = None

class Bh1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing175 | None = None

class Bi1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Bj1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing179(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig158(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Commerce155(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Bl1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing179 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce155 | None = None

class Marketing180(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce156(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing180 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce156 | None = None

class Commerce157(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bq1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing180 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce157 | None = None

class Bv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')

class Bw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cd1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cq1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct97(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce158(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct97 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ch1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing180 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce158 | None = None

class Ci1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Cs1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')

class Cv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce159(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing180 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce159 | None = None

class Marketing184(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce160(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cx1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing184 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce160 | None = None

class Cy1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')

class Marketing185(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct98(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce161(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct98 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce161 | None = None

class DefaultProduct99(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce162(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    annual_auto_downgrade: bool | None = Field(None, alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct99 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow | None = Field(None, alias='regulatedCancelFlow')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool | None = Field(None, alias='requiresAdditionalSADisclaimer')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class De1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce162 | None = None

class Dj1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct100(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce163(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct100 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Dk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig158 | None = Field(None, alias='featureConfig')
    commerce: Commerce163 | None = None

class Dz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing185 | None = None

class FeatureConfig170(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class DefaultProduct101(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce164(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct101 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ee1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig170 | None = Field(None, alias='featureConfig')
    commerce: Commerce164 | None = None

class FeatureConfig171(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Eg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')

class Eh1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Er1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct102(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce165(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct102 | None = Field(None, alias='defaultProduct')
    disable_province_dropdown: bool | None = Field(None, alias='disableProvinceDropdown')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Es1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce165 | None = None

class Et1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct103(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce166(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct103 | None = Field(None, alias='defaultProduct')
    disable_province_dropdown: bool | None = Field(None, alias='disableProvinceDropdown')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Fi1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce166 | None = None

class Commerce167(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Fk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing185 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce167 | None = None

class Marketing194(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce168(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Fo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing194 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce168 | None = None

class Marketing195(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct104(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce169(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct104 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    regulated_cancel_flow: RegulatedCancelFlow | None = Field(None, alias='regulatedCancelFlow')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    requires_additional_sa_disclaimer: bool | None = Field(None, alias='requiresAdditionalSADisclaimer')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Fr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing195 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce169 | None = None

class Fx1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ga1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct105(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce170(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct105 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gb1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing195 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce170 | None = None

class Marketing197(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce171(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Gf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing197 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce171 | None = None

class Commerce172(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Gg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing197 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce172 | None = None

class Gh1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce173(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Gi1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing197 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce173 | None = None

class Marketing200(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct106(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce174(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    default_product: DefaultProduct106 | None = Field(None, alias='defaultProduct')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Gl1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing200 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce174 | None = None

class Gm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Gn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing201(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce175(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Gp1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing201 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce175 | None = None

class Gq1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing202(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct107(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce176(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct107 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing202 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce176 | None = None

class Commerce177(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gs1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing202 | None = None
    feature_config: FeatureConfig171 | None = Field(None, alias='featureConfig')
    commerce: Commerce177 | None = None

class Gw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig185(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class DefaultProduct108(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce178(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct108 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Hr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing202 | None = None
    feature_config: FeatureConfig185 | None = Field(None, alias='featureConfig')
    commerce: Commerce178 | None = None

class FeatureConfig186(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct109(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce179(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct109 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Hu1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing202 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce179 | None = None

class DefaultProduct110(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce180(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct110 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ie1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing202 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce180 | None = None

class Il1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing202 | None = None

class Marketing208(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce181(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Im1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing208 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce181 | None = None

class Commerce182(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Io1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing208 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce182 | None = None

class Marketing210(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Iq1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing210 | None = None

class Ir1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct111(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce183(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct111 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Is1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing210 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce183 | None = None

class DefaultProduct112(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce184(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct112 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class It1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing210 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce184 | None = None

class Marketing213(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce185(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Je1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing213 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce185 | None = None

class Marketing214(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Jo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing214 | None = None

class Ke1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Km1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Kw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing214 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')

class Commerce186(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ky1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing214 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce186 | None = None

class Lb1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing214 | None = None

class DefaultProduct113(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce187(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct113 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Li1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing214 | None = None
    feature_config: FeatureConfig186 | None = Field(None, alias='featureConfig')
    commerce: Commerce187 | None = None

class Lr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ls1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig196(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class DefaultProduct114(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce188(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct114 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Lt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing214 | None = None
    feature_config: FeatureConfig196 | None = Field(None, alias='featureConfig')
    commerce: Commerce188 | None = None

class FeatureConfig197(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct115(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce189(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct115 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Lu1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing214 | None = None
    feature_config: FeatureConfig197 | None = Field(None, alias='featureConfig')
    commerce: Commerce189 | None = None

class FeatureConfig198(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class DefaultProduct116(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce190(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct116 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Lv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing214 | None = None
    feature_config: FeatureConfig198 | None = Field(None, alias='featureConfig')
    commerce: Commerce190 | None = None

class Ly1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ma1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing214 | None = None

class Marketing223(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig199(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct117(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce191(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    default_product: DefaultProduct117 | None = Field(None, alias='defaultProduct')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mc1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing223 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce191 | None = None

class Md1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing224(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct118(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce192(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct118 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Me1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing224 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce192 | None = None

class Marketing225(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce193(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Mf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing225 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce193 | None = None

class Mg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing226(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce194(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    sells_bundle: bool | None = Field(None, alias='sellsBundle')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mh1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing226 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce194 | None = None

class DefaultProduct119(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce195(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct119 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing226 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce195 | None = None

class Ml1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing228(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce196(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Mq1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing228 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce196 | None = None

class Mr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing229(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce197(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ms1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing229 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce197 | None = None

class DefaultProduct120(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce198(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct120 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing229 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce198 | None = None

class Marketing231(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct121(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce199(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct121 | None = Field(None, alias='defaultProduct')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Mu1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing231 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce199 | None = None

class Mw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Mz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Na1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce200(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Nc1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing231 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce200 | None = None

class Ne1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ng1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing233(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct122(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce201(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct122 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    local_payment: LocalPayment | None = Field(None, alias='localPayment')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Nl1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing233 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce201 | None = None

class DefaultProduct123(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce202(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct123 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class No1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing233 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce202 | None = None

class Nt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Om1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing233 | None = None

class Marketing236(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce203(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Pf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing236 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce203 | None = None

class Marketing237(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct124(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce204(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    annual_auto_downgrade: bool | None = Field(None, alias='annualAutoDowngrade')
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct124 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pl1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing237 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce204 | None = None

class Marketing238(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce205(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Pm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing238 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce205 | None = None

class Commerce206(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Pn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing238 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce206 | None = None

class Marketing240(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ps2(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing240 | None = None

class DefaultProduct125(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce207(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct125 | None = Field(None, alias='defaultProduct')
    disable_province_dropdown: bool | None = Field(None, alias='disableProvinceDropdown')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing240 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce207 | None = None

class Qa1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing240 | None = None

class Marketing243(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce208(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Re1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing243 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce208 | None = None

class Marketing244(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct126(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce209(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct126 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ro1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing244 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce209 | None = None

class DefaultProduct127(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce210(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct127 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Rs1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing244 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce210 | None = None

class Rw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sa1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing244 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')

class Sc1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct128(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce211(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct128 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Se1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing244 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce211 | None = None

class Marketing248(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce212(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Sh1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing248 | None = None
    feature_config: FeatureConfig199 | None = Field(None, alias='featureConfig')
    commerce: Commerce212 | None = None

class Marketing249(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig222(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    cmp_enable_browser_lang: bool | None = Field(None, alias='cmpEnableBrowserLang')

class DefaultProduct129(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce213(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct129 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Si1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing249 | None = None
    feature_config: FeatureConfig222 | None = Field(None, alias='featureConfig')
    commerce: Commerce213 | None = None

class Marketing250(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig223(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Commerce214(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Sj1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing250 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce214 | None = None

class Marketing251(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct130(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    portability: Portability | None = None
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce215(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct130 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Sk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing251 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce215 | None = None

class Sl1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing252(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct131(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce216(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct131 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Sm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing252 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce216 | None = None

class Sn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class So1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ss1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class St1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing253(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce217(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Sx1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing253 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce217 | None = None

class Sy1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Sz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce218(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tc1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing253 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce218 | None = None

class Td1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing255(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce219(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Tf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing255 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce219 | None = None

class Tg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing256(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Tn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing256 | None = None

class DefaultProduct132(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce220(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct132 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing256 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce220 | None = None

class Tz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ua1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Ug1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing258(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Uk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing258 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')

class DefaultProduct133(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce221(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct133 | None = Field(None, alias='defaultProduct')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Va1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing258 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce221 | None = None

class Marketing260(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce222(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Vg1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing260 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce222 | None = None

class Marketing261(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce223(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Wf1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing261 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce223 | None = None

class Commerce224(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Xk1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')
    commerce: Commerce224 | None = None

class Ye1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce225(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show3_ds_flow: bool | None = Field(None, alias='show3DSFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_subscriber_agreement_checkbox: bool | None = Field(None, alias='showCommerceUnifiedSubscriberAgreementCheckbox')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')

class Yt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing261 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce225 | None = None

class Yu1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Marketing263(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Za1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing263 | None = None

class Zm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Zr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Zw1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct134(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce226(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct134 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ag1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce226 | None = None

class DefaultProduct135(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce227(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cancel_subscription_nav_item_promoted: CancelSubscriptionNavItemPromoted | None = Field(None, alias='cancelSubscriptionNavItemPromoted')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct135 | None = Field(None, alias='defaultProduct')
    is_one_step_cancel_billing_country: bool | None = Field(None, alias='isOneStepCancelBillingCountry')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_active_review: bool | None = Field(None, alias='requiresActiveReview')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ar1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce227 | None = None

class DefaultProduct136(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce228(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct136 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bb1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce228 | None = None

class DefaultProduct137(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce229(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct137 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bo1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig223 | None = Field(None, alias='featureConfig')
    commerce: Commerce229 | None = None

class FeatureConfig239(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    display_additional_ratings: bool | None = Field(None, alias='displayAdditionalRatings')
    display_rating_advisories: bool | None = Field(None, alias='displayRatingAdvisories')
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct138(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce230(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct138 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    starz_play_supported_regions: bool | None = Field(None, alias='starzPlaySupportedRegions')

class Br1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig239 | None = Field(None, alias='featureConfig')
    commerce: Commerce230 | None = None

class FeatureConfig240(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class DefaultProduct139(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce231(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct139 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bs1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce231 | None = None

class DefaultProduct140(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce232(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct140 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Bz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce232 | None = None

class DefaultProduct141(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce233(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct141 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cl1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce233 | None = None

class DefaultProduct142(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce234(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct142 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Co1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce234 | None = None

class DefaultProduct143(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce235(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct143 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Cr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce235 | None = None

class DefaultProduct144(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce236(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct144 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Dm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce236 | None = None

class DefaultProduct145(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce237(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct145 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Do1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce237 | None = None

class DefaultProduct146(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce238(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct146 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ec1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce238 | None = None

class DefaultProduct147(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce239(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct147 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gd1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce239 | None = None

class DefaultProduct148(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce240(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct148 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce240 | None = None

class DefaultProduct149(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce241(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct149 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gy1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce241 | None = None

class DefaultProduct150(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce242(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct150 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Hn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce242 | None = None

class DefaultProduct151(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce243(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct151 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ht1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce243 | None = None

class DefaultProduct152(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce244(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct152 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Jm1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce244 | None = None

class DefaultProduct153(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce245(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct153 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Kn1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce245 | None = None

class DefaultProduct154(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce246(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct154 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Lc1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce246 | None = None

class DefaultProduct155(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce247(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct155 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')
    starz_play_supported_regions: bool | None = Field(None, alias='starzPlaySupportedRegions')

class Mx1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce247 | None = None

class DefaultProduct156(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce248(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct156 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ni1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce248 | None = None

class DefaultProduct157(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce249(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct157 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pa1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce249 | None = None

class DefaultProduct158(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce250(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct158 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pe1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce250 | None = None

class DefaultProduct159(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce251(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct159 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Py1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce251 | None = None

class DefaultProduct160(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce252(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct160 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Sr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce252 | None = None

class DefaultProduct161(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce253(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct161 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Sv1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce253 | None = None

class DefaultProduct162(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce254(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct162 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Tt1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce254 | None = None

class DefaultProduct163(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce255(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct163 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Uy1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce255 | None = None

class DefaultProduct164(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce256(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct164 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Vc1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce256 | None = None

class DefaultProduct165(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce257(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct165 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_forced_subscriber_agreement: bool | None = Field(None, alias='requiresForcedSubscriberAgreement')
    requires_legal_entity: bool | None = Field(None, alias='requiresLegalEntity')
    sells_combo_plus_bundle: bool | None = Field(None, alias='sellsComboPlusBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_identity_unified_authentication_flows: bool | None = Field(None, alias='showIdentityUnifiedAuthenticationFlows')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ve1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing263 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce257 | None = None

class Marketing296(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce258(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class As1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing296 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce258 | None = None

class Marketing297(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class DefaultProduct166(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Commerce259(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct166 | None = Field(None, alias='defaultProduct')
    license_plate_sign_up_url: str | None = Field(None, alias='licensePlateSignUpURL')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    promotional_offers: dict[str, Any] | None = Field(None, alias='promotionalOffers')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_tiara: bool | None = Field(None, alias='showCommerceTiara')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Ca1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing297 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce259 | None = None

class Marketing298(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce260(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Gu1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing298 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce260 | None = None

class Commerce261(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Mp1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing298 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce261 | None = None

class Commerce262(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Pr1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing298 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce262 | None = None

class Marketing301(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class Commerce263(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    sells_bundle: bool | None = Field(None, alias='sellsBundle')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Um1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing301 | None = None
    feature_config: FeatureConfig240 | None = Field(None, alias='featureConfig')
    commerce: Commerce263 | None = None

class FeatureConfig273(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')
    enable_identity_consent_sync: bool | None = Field(None, alias='enableIdentityConsentSync')

class DefaultProduct167(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nu: Nu90 | None = Field(None, alias='NU')
    change_payment: ChangePayment | None = Field(None, alias='changePayment')
    purchase: Purchase85 | None = None
    un_auth: UnAuth | None = Field(None, alias='unAuth')

class Ps3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class Tv3(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    type: str | None = None
    url: str | None = None

class LicensePlateFlowNavigation1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    amazon: Amazon | None = Field(None, alias='AMAZON')
    cox: Cox | None = None
    hisense: Hisense | None = None
    lg: Lg | None = None
    ps: Ps3 | None = None
    ps4: Ps4 | None = None
    samsung: Samsung | None = None
    tivo_us: TivoUs | None = None
    tv: Tv3 | None = None
    vizio: Vizio | None = None
    xbox: Xbox | None = None
    xglobal: Xglobal | None = None

class Ft1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nine_month: NineMonth | None = Field(None, alias='nineMonth')
    one_year: OneYear | None = Field(None, alias='oneYear')
    six_month: SixMonth | None = Field(None, alias='sixMonth')
    three_year: ThreeYear | None = Field(None, alias='threeYear')
    two_year: TwoYear | None = Field(None, alias='twoYear')

class Purchase169(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nine_month: NineMonth | None = Field(None, alias='nineMonth')
    one_year: OneYear | None = Field(None, alias='oneYear')
    six_month: SixMonth | None = Field(None, alias='sixMonth')
    three_year: ThreeYear | None = Field(None, alias='threeYear')
    two_year: TwoYear | None = Field(None, alias='twoYear')

class Superbundle1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    nine_month: NineMonth | None = Field(None, alias='nineMonth')
    one_year: OneYear | None = Field(None, alias='oneYear')
    six_month: SixMonth | None = Field(None, alias='sixMonth')

class RewardsProducts1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ft: Ft1 | None = Field(None, alias='FT')
    purchase: Purchase169 | None = None
    superbundle: Superbundle1 | None = None

class Commerce264(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ads_tier_devices: AdsTierDevices | None = Field(None, alias='adsTierDevices')
    ads_tier_enabled: bool | None = Field(None, alias='adsTierEnabled')
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    card_options: list[str] | None = Field(None, alias='cardOptions')
    default_product: DefaultProduct167 | None = Field(None, alias='defaultProduct')
    devices_that_sell2_p_bundle: DevicesThatSell2PBundle | None = Field(None, alias='devicesThatSell2PBundle')
    devices_that_sell_bundle: DevicesThatSellBundle | None = Field(None, alias='devicesThatSellBundle')
    enable_global_identity_unbranded_create_account: bool | None = Field(None, alias='enableGlobalIdentityUnbrandedCreateAccount')
    license_plate_flow_navigation: LicensePlateFlowNavigation1 | None = Field(None, alias='licensePlateFlowNavigation')
    one_step_cancel_billing_states: list[str] | None = Field(None, alias='oneStepCancelBillingStates')
    payment_methods: list[str] | None = Field(None, alias='paymentMethods')
    paypal_client_id: str | None = Field(None, alias='paypalClientId')
    requires_annual_opt_in_states: list[str] | None = Field(None, alias='requiresAnnualOptInStates')
    restart_eligible_enabled: bool | None = Field(None, alias='restartEligibleEnabled')
    rewards_products: RewardsProducts1 | None = Field(None, alias='rewardsProducts')
    sells_bundle: bool | None = Field(None, alias='sellsBundle')
    show_commerce_flex_account_offer: bool | None = Field(None, alias='showCommerceFlexAccountOffer')
    show_commerce_unified_cancel_flow: bool | None = Field(None, alias='showCommerceUnifiedCancelFlow')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Us1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    footer: list[str] | None = None
    marketing: Marketing301 | None = None
    feature_config: FeatureConfig273 | None = Field(None, alias='featureConfig')
    commerce: Commerce264 | None = None

class Marketing303(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    name: str | None = None
    lang: str | None = None
    enable_parent_country_languages: bool | None = Field(None, alias='enableParentCountryLanguages')
    region_languages: list[str] | None = Field(None, alias='regionLanguages')

class FeatureConfig274(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    enable_cmp: bool | None = Field(None, alias='enableCMP')

class Commerce265(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    braintree_paypal_enabled: bool | None = Field(None, alias='braintreePaypalEnabled')
    show_commerce_unified_signup_flow: bool | None = Field(None, alias='showCommerceUnifiedSignupFlow')
    show_identity_learn_more: bool | None = Field(None, alias='showIdentityLearnMore')
    show_identity_unified_license_plate_flow: bool | None = Field(None, alias='showIdentityUnifiedLicensePlateFlow')
    special_offer_enabled: bool | None = Field(None, alias='specialOfferEnabled')
    special_offer_product: SpecialOfferProduct | None = Field(None, alias='specialOfferProduct')

class Vi1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    parent_country: str | None = Field(None, alias='parentCountry')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    marketing: Marketing303 | None = None
    feature_config: FeatureConfig274 | None = Field(None, alias='featureConfig')
    commerce: Commerce265 | None = None

class Yz1(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    is_eu: bool | None = Field(None, alias='isEU')
    name: str | None = None
    group: str | None = None
    has_launched: bool | None = Field(None, alias='hasLaunched')
    lang: str | None = None
    region_languages: list[str] | None = Field(None, alias='regionLanguages')
    feature_config: dict[str, Any] | None = Field(None, alias='featureConfig')

class CountriesConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    af: Af1 | None = Field(None, alias='AF')
    au: Au1 | None = Field(None, alias='AU')
    bd: Bd1 | None = Field(None, alias='BD')
    bn: Bn1 | None = Field(None, alias='BN')
    bt: Bt1 | None = Field(None, alias='BT')
    bu: Bu1 | None = Field(None, alias='BU')
    cc: Cc1 | None = Field(None, alias='CC')
    ck: Ck1 | None = Field(None, alias='CK')
    cn: Cn1 | None = Field(None, alias='CN')
    fj: Fj1 | None = Field(None, alias='FJ')
    hk: Hk1 | None = Field(None, alias='HK')
    hm: Hm1 | None = Field(None, alias='HM')
    id: Id1 | None = Field(None, alias='ID')
    in_: In1 | None = Field(None, alias='IN')
    jp: Jp1 | None = Field(None, alias='JP')
    kh: Kh1 | None = Field(None, alias='KH')
    ki: Ki1 | None = Field(None, alias='KI')
    kr: Kr1 | None = Field(None, alias='KR')
    la: La1 | None = Field(None, alias='LA')
    lk: Lk1 | None = Field(None, alias='LK')
    mm: Mm1 | None = Field(None, alias='MM')
    mo: Mo1 | None = Field(None, alias='MO')
    mv: Mv1 | None = Field(None, alias='MV')
    my: My1 | None = Field(None, alias='MY')
    nf: Nf1 | None = Field(None, alias='NF')
    np: Np1 | None = Field(None, alias='NP')
    nr: Nr1 | None = Field(None, alias='NR')
    nu: Nu89 | None = Field(None, alias='NU')
    nz: Nz1 | None = Field(None, alias='NZ')
    pg: Pg1 | None = Field(None, alias='PG')
    ph: Ph1 | None = Field(None, alias='PH')
    pk: Pk1 | None = Field(None, alias='PK')
    sb: Sb1 | None = Field(None, alias='SB')
    sg: Sg1 | None = Field(None, alias='SG')
    th: Th1 | None = Field(None, alias='TH')
    tk: Tk1 | None = Field(None, alias='TK')
    tl: Tl1 | None = Field(None, alias='TL')
    to: To1 | None = Field(None, alias='TO')
    tp: Tp1 | None = Field(None, alias='TP')
    tv: Tv2 | None = Field(None, alias='TV')
    tw: Tw1 | None = Field(None, alias='TW')
    vn: Vn1 | None = Field(None, alias='VN')
    vu: Vu1 | None = Field(None, alias='VU')
    ws: Ws1 | None = Field(None, alias='WS')
    ad: Ad1 | None = Field(None, alias='AD')
    ae: Ae1 | None = Field(None, alias='AE')
    ai: Ai1 | None = Field(None, alias='AI')
    al: Al1 | None = Field(None, alias='AL')
    am: Am1 | None = Field(None, alias='AM')
    an: An1 | None = Field(None, alias='AN')
    ao: Ao1 | None = Field(None, alias='AO')
    at: At1 | None = Field(None, alias='AT')
    aw: Aw1 | None = Field(None, alias='AW')
    ax: Ax1 | None = Field(None, alias='AX')
    ba: Ba1 | None = Field(None, alias='BA')
    be: Be1 | None = Field(None, alias='BE')
    bf: Bf1 | None = Field(None, alias='BF')
    bg: Bg1 | None = Field(None, alias='BG')
    bh: Bh1 | None = Field(None, alias='BH')
    bi: Bi1 | None = Field(None, alias='BI')
    bj: Bj1 | None = Field(None, alias='BJ')
    bl: Bl1 | None = Field(None, alias='BL')
    bm: Bm1 | None = Field(None, alias='BM')
    bq: Bq1 | None = Field(None, alias='BQ')
    bv: Bv1 | None = Field(None, alias='BV')
    bw: Bw1 | None = Field(None, alias='BW')
    cd: Cd1 | None = Field(None, alias='CD')
    cf: Cf1 | None = Field(None, alias='CF')
    cq: Cq1 | None = Field(None, alias='CQ')
    ch: Ch1 | None = Field(None, alias='CH')
    ci: Ci1 | None = Field(None, alias='CI')
    cm: Cm1 | None = Field(None, alias='CM')
    cs: Cs1 | None = Field(None, alias='CS')
    cv: Cv1 | None = Field(None, alias='CV')
    cw: Cw1 | None = Field(None, alias='CW')
    cx: Cx1 | None = Field(None, alias='CX')
    cy: Cy1 | None = Field(None, alias='CY')
    cz: Cz1 | None = Field(None, alias='CZ')
    de: De1 | None = Field(None, alias='DE')
    dj: Dj1 | None = Field(None, alias='DJ')
    dk: Dk1 | None = Field(None, alias='DK')
    dz: Dz1 | None = Field(None, alias='DZ')
    ee: Ee1 | None = Field(None, alias='EE')
    eg: Eg1 | None = Field(None, alias='EG')
    eh: Eh1 | None = Field(None, alias='EH')
    er: Er1 | None = Field(None, alias='ER')
    es: Es1 | None = Field(None, alias='ES')
    et: Et1 | None = Field(None, alias='ET')
    fi: Fi1 | None = Field(None, alias='FI')
    fk: Fk1 | None = Field(None, alias='FK')
    fo: Fo1 | None = Field(None, alias='FO')
    fr: Fr1 | None = Field(None, alias='FR')
    fx: Fx1 | None = Field(None, alias='FX')
    ga: Ga1 | None = Field(None, alias='GA')
    gb: Gb1 | None = Field(None, alias='GB')
    gf: Gf1 | None = Field(None, alias='GF')
    gg: Gg1 | None = Field(None, alias='GG')
    gh: Gh1 | None = Field(None, alias='GH')
    gi: Gi1 | None = Field(None, alias='GI')
    gl: Gl1 | None = Field(None, alias='GL')
    gm: Gm1 | None = Field(None, alias='GM')
    gn: Gn1 | None = Field(None, alias='GN')
    gp: Gp1 | None = Field(None, alias='GP')
    gq: Gq1 | None = Field(None, alias='GQ')
    gr: Gr1 | None = Field(None, alias='GR')
    gs: Gs1 | None = Field(None, alias='GS')
    gw: Gw1 | None = Field(None, alias='GW')
    hr: Hr1 | None = Field(None, alias='HR')
    hu: Hu1 | None = Field(None, alias='HU')
    ie: Ie1 | None = Field(None, alias='IE')
    il: Il1 | None = Field(None, alias='IL')
    im: Im1 | None = Field(None, alias='IM')
    io: Io1 | None = Field(None, alias='IO')
    iq: Iq1 | None = Field(None, alias='IQ')
    ir: Ir1 | None = Field(None, alias='IR')
    is_: Is1 | None = Field(None, alias='IS')
    it: It1 | None = Field(None, alias='IT')
    je: Je1 | None = Field(None, alias='JE')
    jo: Jo1 | None = Field(None, alias='JO')
    ke: Ke1 | None = Field(None, alias='KE')
    km: Km1 | None = Field(None, alias='KM')
    kw: Kw1 | None = Field(None, alias='KW')
    ky: Ky1 | None = Field(None, alias='KY')
    lb: Lb1 | None = Field(None, alias='LB')
    li: Li1 | None = Field(None, alias='LI')
    lr: Lr1 | None = Field(None, alias='LR')
    ls: Ls1 | None = Field(None, alias='LS')
    lt: Lt1 | None = Field(None, alias='LT')
    lu: Lu1 | None = Field(None, alias='LU')
    lv: Lv1 | None = Field(None, alias='LV')
    ly: Ly1 | None = Field(None, alias='LY')
    ma: Ma1 | None = Field(None, alias='MA')
    mc: Mc1 | None = Field(None, alias='MC')
    md: Md1 | None = Field(None, alias='MD')
    me: Me1 | None = Field(None, alias='ME')
    mf: Mf1 | None = Field(None, alias='MF')
    mg: Mg1 | None = Field(None, alias='MG')
    mh: Mh1 | None = Field(None, alias='MH')
    mk: Mk1 | None = Field(None, alias='MK')
    ml: Ml1 | None = Field(None, alias='ML')
    mq: Mq1 | None = Field(None, alias='MQ')
    mr: Mr1 | None = Field(None, alias='MR')
    ms: Ms1 | None = Field(None, alias='MS')
    mt: Mt1 | None = Field(None, alias='MT')
    mu: Mu1 | None = Field(None, alias='MU')
    mw: Mw1 | None = Field(None, alias='MW')
    mz: Mz1 | None = Field(None, alias='MZ')
    na: Na1 | None = Field(None, alias='NA')
    nc: Nc1 | None = Field(None, alias='NC')
    ne: Ne1 | None = Field(None, alias='NE')
    ng: Ng1 | None = Field(None, alias='NG')
    nl: Nl1 | None = Field(None, alias='NL')
    no: No1 | None = Field(None, alias='NO')
    nt: Nt1 | None = Field(None, alias='NT')
    om: Om1 | None = Field(None, alias='OM')
    pf: Pf1 | None = Field(None, alias='PF')
    pl: Pl1 | None = Field(None, alias='PL')
    pm: Pm1 | None = Field(None, alias='PM')
    pn: Pn1 | None = Field(None, alias='PN')
    ps: Ps2 | None = Field(None, alias='PS')
    pt: Pt1 | None = Field(None, alias='PT')
    qa: Qa1 | None = Field(None, alias='QA')
    re: Re1 | None = Field(None, alias='RE')
    ro: Ro1 | None = Field(None, alias='RO')
    rs: Rs1 | None = Field(None, alias='RS')
    rw: Rw1 | None = Field(None, alias='RW')
    sa: Sa1 | None = Field(None, alias='SA')
    sc: Sc1 | None = Field(None, alias='SC')
    se: Se1 | None = Field(None, alias='SE')
    sh: Sh1 | None = Field(None, alias='SH')
    si: Si1 | None = Field(None, alias='SI')
    sj: Sj1 | None = Field(None, alias='SJ')
    sk: Sk1 | None = Field(None, alias='SK')
    sl: Sl1 | None = Field(None, alias='SL')
    sm: Sm1 | None = Field(None, alias='SM')
    sn: Sn1 | None = Field(None, alias='SN')
    so: So1 | None = Field(None, alias='SO')
    ss: Ss1 | None = Field(None, alias='SS')
    st: St1 | None = Field(None, alias='ST')
    sx: Sx1 | None = Field(None, alias='SX')
    sy: Sy1 | None = Field(None, alias='SY')
    sz: Sz1 | None = Field(None, alias='SZ')
    tc: Tc1 | None = Field(None, alias='TC')
    td: Td1 | None = Field(None, alias='TD')
    tf: Tf1 | None = Field(None, alias='TF')
    tg: Tg1 | None = Field(None, alias='TG')
    tn: Tn1 | None = Field(None, alias='TN')
    tr: Tr1 | None = Field(None, alias='TR')
    tz: Tz1 | None = Field(None, alias='TZ')
    ua: Ua1 | None = Field(None, alias='UA')
    ug: Ug1 | None = Field(None, alias='UG')
    uk: Uk1 | None = Field(None, alias='UK')
    va: Va1 | None = Field(None, alias='VA')
    vg: Vg1 | None = Field(None, alias='VG')
    wf: Wf1 | None = Field(None, alias='WF')
    xk: Xk1 | None = Field(None, alias='XK')
    ye: Ye1 | None = Field(None, alias='YE')
    yt: Yt1 | None = Field(None, alias='YT')
    yu: Yu1 | None = Field(None, alias='YU')
    za: Za1 | None = Field(None, alias='ZA')
    zm: Zm1 | None = Field(None, alias='ZM')
    zr: Zr1 | None = Field(None, alias='ZR')
    zw: Zw1 | None = Field(None, alias='ZW')
    ag: Ag1 | None = Field(None, alias='AG')
    ar: Ar1 | None = Field(None, alias='AR')
    bb: Bb1 | None = Field(None, alias='BB')
    bo: Bo1 | None = Field(None, alias='BO')
    br: Br1 | None = Field(None, alias='BR')
    bs: Bs1 | None = Field(None, alias='BS')
    bz: Bz1 | None = Field(None, alias='BZ')
    cl: Cl1 | None = Field(None, alias='CL')
    co: Co1 | None = Field(None, alias='CO')
    cr: Cr1 | None = Field(None, alias='CR')
    dm: Dm1 | None = Field(None, alias='DM')
    do: Do1 | None = Field(None, alias='DO')
    ec: Ec1 | None = Field(None, alias='EC')
    gd: Gd1 | None = Field(None, alias='GD')
    gt: Gt1 | None = Field(None, alias='GT')
    gy: Gy1 | None = Field(None, alias='GY')
    hn: Hn1 | None = Field(None, alias='HN')
    ht: Ht1 | None = Field(None, alias='HT')
    jm: Jm1 | None = Field(None, alias='JM')
    kn: Kn1 | None = Field(None, alias='KN')
    lc: Lc1 | None = Field(None, alias='LC')
    mx: Mx1 | None = Field(None, alias='MX')
    ni: Ni1 | None = Field(None, alias='NI')
    pa: Pa1 | None = Field(None, alias='PA')
    pe: Pe1 | None = Field(None, alias='PE')
    py: Py1 | None = Field(None, alias='PY')
    sr: Sr1 | None = Field(None, alias='SR')
    sv: Sv1 | None = Field(None, alias='SV')
    tt: Tt1 | None = Field(None, alias='TT')
    uy: Uy1 | None = Field(None, alias='UY')
    vc: Vc1 | None = Field(None, alias='VC')
    ve: Ve1 | None = Field(None, alias='VE')
    as_: As1 | None = Field(None, alias='AS')
    ca: Ca1 | None = Field(None, alias='CA')
    gu: Gu1 | None = Field(None, alias='GU')
    mp: Mp1 | None = Field(None, alias='MP')
    pr: Pr1 | None = Field(None, alias='PR')
    um: Um1 | None = Field(None, alias='UM')
    us: Us1 | None = Field(None, alias='US')
    vi: Vi1 | None = Field(None, alias='VI')
    yz: Yz1 | None = Field(None, alias='YZ')
    time_stamp: str | None = Field(None, alias='timeStamp')

class LangDisplayNames(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    ar: str | None = None
    bg: str | None = None
    cs: str | None = None
    da: str | None = None
    de: str | None = None
    el: str | None = None
    en: str | None = None
    es: str | None = None
    fi: str | None = None
    fr: str | None = None
    he: str | None = None
    hr: str | None = None
    hu: str | None = None
    id: str | None = None
    it: str | None = None
    ja: str | None = None
    ko: str | None = None
    ms: str | None = None
    nl: str | None = None
    nb: str | None = None
    pl: str | None = None
    pt: str | None = None
    ro: str | None = None
    sk: str | None = None
    sv: str | None = None
    th: str | None = None
    tr: str | None = None
    vi: str | None = None
    zh: str | None = None

class RemoteConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    app_config: AppConfig | None = Field(None, alias='appConfig')
    dictionary_versions: DictionaryVersions | None = Field(None, alias='dictionaryVersions')
    path: Path | None = None
    remote_app_config: RemoteAppConfig | None = Field(None, alias='remoteAppConfig')
    version: str | None = None
    countries: Countries | None = None
    feature_config: FeatureConfig137 | None = Field(None, alias='featureConfig')
    app_lang_map: AppLangMap | None = Field(None, alias='appLangMap')
    cannonball_link_manager: CannonballLinkManager1 | None = Field(None, alias='cannonballLinkManager')
    cannonball: Cannonball | None = None
    spaceball: Spaceball | None = None
    archive_date: str | None = Field(None, alias='archiveDate')
    countries_config: CountriesConfig | None = Field(None, alias='countriesConfig')
    lang_display_names: LangDisplayNames | None = Field(None, alias='langDisplayNames')

class CannonballInstance(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    instance: str | None = None
    available_environments: list[str] | None = Field(None, alias='availableEnvironments')
    current_environment: str | None = Field(None, alias='currentEnvironment')

class Debug(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    cannonball_edit_url: str | None = Field(None, alias='cannonballEditUrl')
    entity_id: str | None = Field(None, alias='entityId')
    cannonball_instances: list[CannonballInstance] | None = Field(None, alias='cannonballInstances')
    common_available_environments: list[str] | None = Field(None, alias='commonAvailableEnvironments')

class PageProps(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    available_locales: list[str] | None = Field(None, alias='availableLocales')
    dictionary: Dictionary | None = None
    feature_flags: FeatureFlags | None = Field(None, alias='featureFlags')
    identity_sdk_config: IdentitySdkConfig | None = Field(None, alias='identitySDKConfig')
    stitch_document: StitchDocument | None = Field(None, alias='stitchDocument')
    page_id: str | None = Field(None, alias='pageId')
    metrics_data: MetricsData7 | None = Field(None, alias='metricsData')
    language: str | None = None
    region: str | None = None
    toast_cta_props: ToastCtaProps | None = Field(None, alias='toastCtaProps')
    remote_config: RemoteConfig | None = Field(None, alias='remoteConfig')
    pathname: str | None = None
    location: str | None = None
    disable_redirect: bool | None = Field(None, alias='disableRedirect')
    has_content: bool | None = Field(None, alias='hasContent')
    rtl_supported_locales: list[str] | None = Field(None, alias='rtlSupportedLocales')
    debug: Debug | None = None

class Props(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    page_props: PageProps | None = Field(None, alias='pageProps')
    field__n_ssp: bool | None = Field(None, alias='__N_SSP')

class Query(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    season: UUID | None = None
    slug: str | None = None

class PinnedPlatformOptions(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    pinned_platform_name: str | None = Field(None, alias='pinnedPlatformName')
    pinned_platform_version: str | None = Field(None, alias='pinnedPlatformVersion')

class RuntimeConfig(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    pinned_platform_options: PinnedPlatformOptions | None = Field(None, alias='pinnedPlatformOptions')
    git_commit: str | None = Field(None, alias='gitCommit')
    is_debug_tooling_enabled: bool | None = Field(None, alias='isDebugToolingEnabled')
    datadog_rum_env: str | None = Field(None, alias='datadogRUMEnv')
    datadog_rum_build_id: str | None = Field(None, alias='datadogRUMBuildId')
    datadog_service_name: str | None = Field(None, alias='datadogServiceName')
    remote_dictionaries_to_load: str | None = Field(None, alias='remoteDictionariesToLoad')

class EntityModel(BaseModel):
    model_config = ConfigDict(extra='ignore', defer_build=True)
    props: Props | None = None
    page: str | None = None
    query: Query | None = None
    build_id: str | None = Field(None, alias='buildId')
    asset_prefix: str | None = Field(None, alias='assetPrefix')
    runtime_config: RuntimeConfig | None = Field(None, alias='runtimeConfig')
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
