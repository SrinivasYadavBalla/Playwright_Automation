from Utils.logger import get_logger


class ProductPage:

    def __init__(self, page):

        self.page = page
        self.logger = get_logger("ProductPage")

    def add_product_to_cart(self, product_name):

        self.logger.info(
            f"Adding product to cart: {product_name}"
        )

        product = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text=product_name
        )

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

        self.logger.info(
            f"Product added successfully: {product_name}"
        )