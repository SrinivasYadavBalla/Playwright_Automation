def test_checkout_click(page):

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # Add product
    page.locator(
        '[data-test="add-to-cart-sauce-labs-backpack"]'
    ).click()

    # Open cart
    page.locator(
        '[data-test="shopping-cart-link"]'
    ).click()

    print("URL:", page.url)

    # Check checkout button
    checkout = page.locator(
        '[data-test="checkout"]'
    )

    print("Count:", checkout.count())
    print("Visible:", checkout.is_visible())
    print("Enabled:", checkout.is_enabled())

    checkout.click()

    print("After click:", page.url)