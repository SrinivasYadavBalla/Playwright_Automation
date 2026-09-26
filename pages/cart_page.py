from Utils.logger import get_logger


class CartPage:

    def __init__(self, page):

        self.page = page
        self.logger = get_logger("CartPage")

        self.cart_icon = page.locator(
            '[data-test="shopping-cart-link"]'
        )

        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )

    def open_cart(self):

        self.logger.info("Opening shopping cart")

        self.cart_icon.click()

        self.logger.info("Shopping cart opened")

    def click_checkout(self):

        self.logger.info("Clicking Checkout")

        self.checkout_button.click()

        self.logger.info("Checkout page opened")