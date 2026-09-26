class HomePage:

    def __init__(self, page):
        self.page = page

        self.search_box = page.locator("#search")
        self.search_button = page.get_by_role(
            "button",
            name="Search"
        )

    def search_product(self, product_name):
        self.search_box.fill(product_name)
        self.search_button.click()