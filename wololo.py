from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.launch_persistent_context(
        user_data_dir="wikipedia",
        headless=False,
        locale="en-US",
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    )
    page = context.new_page()
    page.goto(
        "https://www.google.com/search?q=wikipedia&oq=wikipedia&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDEzOTVqMGoyqAIAsAIB&sourceid=chrome&ie=UTF-8"
    )
    page.get_by_role("button", name="Tout refuser").click()
    page.get_by_role("link", name="Wikipédia, l'encyclopédie").click()
    page.get_by_placeholder("Rechercher sur Wikipédia").click()
    page.get_by_placeholder("Rechercher sur Wikipédia").fill("wololo")
    page.get_by_placeholder("Rechercher sur Wikipédia").press("Enter")
    page.get_by_role("link", name="Wollongong ville de Nouvelle-").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
