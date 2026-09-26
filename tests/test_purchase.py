# from pages.login_page import LoginPage
# from pages.home_page import HomePage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage


# # def test_complete_purchase(page):

# #     # Login
# #     login_page = LoginPage(page)

# #     login_page.login(
# #         "standard_user",
# #         "secret_sauce"
# #     )

# #     # Product
# #     product_page = ProductPage(page)

# #     product_page.add_to_cart()

# #     # Cart
# #     cart_page = CartPage(page)

# #     cart_page.click_checkout()

# #     # Checkout
# #     checkout_page = CheckoutPage(page)

# #     checkout_page.enter_customer_details(
# #         "Srinivas",
# #         "Yadav",
# #         "500001"
# #     )

# #     checkout_page.click_continue()

# #     checkout_page.place_order()

# #     assert checkout_page.success_message.is_visible()

# def test_complete_purchase(page):

#     login_page = LoginPage(page)

#     login_page.login(
#         "standard_user",
#         "secret_sauce"
#     )

#     product_page = ProductPage(page)

#     product_page.add_product_to_cart(
#         "Sauce Labs Backpack"
#     )

#     cart_page = CartPage(page)

#     cart_page.open_cart()

#     cart_page.click_checkout()

#     checkout_page = CheckoutPage(page)

#     checkout_page.enter_customer_details(
#         "Srinivas",
#         "Yadav",
#         "500001"
#     )

#     checkout_page.click_continue()

#     checkout_page.place_order()

#     assert checkout_page.success_message.is_visible()


from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_purchase(page):

    login_page = LoginPage(page)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    product_page = ProductPage(page)

    product_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    cart_page = CartPage(page)

    cart_page.open_cart()

    cart_page.click_checkout()

    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_details(
        "Srinivas",
        "Yadav",
        "500001"
    )

    checkout_page.click_continue()

    checkout_page.place_order()

    assert checkout_page.success_message.is_visible()