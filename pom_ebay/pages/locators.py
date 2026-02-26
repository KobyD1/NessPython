class welcomePageLocators:
    adv_link_text = "Advanced"

class advPageLocators:
    search_button_text="Search"

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