from Utils.logger import get_logger


class CheckoutPage:

    def __init__(self, page):

        self.page = page
        self.logger = get_logger("CheckoutPage")

        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")

        self.continue_button = page.locator(
            '[data-test="continue"]'
        )

        self.finish_button = page.locator(
            '[data-test="finish"]'
        )

        self.success_message = page.locator(
            ".complete-header"
        )

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.logger.info(
            "Entering customer checkout details"
        )

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):

        self.logger.info("Clicking Continue")

        self.continue_button.click()

    def place_order(self):

        self.logger.info("Clicking Finish / Place Order")

        self.finish_button.click()

        self.logger.info("Order placed successfully")