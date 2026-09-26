# import pytest
# from playwright.sync_api import sync_playwright


# @pytest.fixture
# def page():

#     with sync_playwright() as p:

#         browser = p.chromium.launch(
#             headless=False
#         )

#         page = browser.new_page()

#         page.goto("https://www.saucedemo.com/")

#         yield page

#         browser.close()


import pytest
from playwright.sync_api import sync_playwright
import os


@pytest.fixture
def page(request):

    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("traces", exist_ok=True)

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        context = browser.new_context()

        page = context.new_page()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page.goto(
            "https://www.saucedemo.com/"
        )

        yield page

        failed = hasattr(
            request.node,
            "rep_call"
        ) and request.node.rep_call.failed

        if failed:

            test_name = request.node.name

            page.screenshot(
                path=f"screenshots/{test_name}.png",
                full_page=True
            )

        context.tracing.stop(
            path=f"traces/{request.node.name}.zip"
        )

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    outcome = yield

    rep = outcome.get_result()

    setattr(
        item,
        f"rep_{rep.when}",
        rep
    )