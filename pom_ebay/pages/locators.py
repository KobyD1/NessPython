class welcomePageLocators:
    adv_link_text = "Advanced"
    results_elements = "div.su-card-container__header"
    products_elements = "a.s-card__link.image-treatment"
    found_text_locator = "div[class*='srp-controls srp-controls--with-list']"
    shipping_locators = [
        "button.btn.submit-button.btn--primary btn--fluid"
    ]


class advPageLocators:
    search_button_text = "Search"
    min_price_id = "[id='s0-1-20-5[2]-@range-comp[]-@range-textbox[]-textbox']"

    min_price_locators = [
        "[id='s0-1-20-5[2]-@range-comp[]-@range-textbox[]-textbox']",
        "[name='_udlo']"
    ]

    max_price_locators = [
        "[id='s0-1-20-5[2]-@range-comp[]-@range-textbox[]_1-textbox']",
        "[name='_udhi']"
    ]

    search_menu_locators = [
        '[id="_nkw"]',
        '[name="_nkw"]',
        '[data-testid="_nkw"]'
    ]

    search_button_locators = [
        'button.btn btn--primary',
        'div.field adv-keywords__btn-help'
    ]


class productPageLocators:
    DROP_DOWN_TEXT = ":Select"
    PRICE_TEXT = "ApproximatelyILS"
    IMAGE_ID = "#PicturePanel"
