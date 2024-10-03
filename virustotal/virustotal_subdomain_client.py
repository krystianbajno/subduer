from playwright.async_api import async_playwright
from virustotal.virustotal_html_subdomain_parser import parse_html

class VirusTotalSubdomainClient:
    CLICK_SELECTOR = 'document.querySelector("#view-container > domain-view").shadowRoot.querySelector("#relations").shadowRoot.querySelector("div > vt-ui-expandable.mb-3.subdomains > span > div > vt-ui-button")'
    CONTENTS_SELECTOR = 'document.querySelector("#view-container > domain-view").shadowRoot.querySelector("#relations").shadowRoot.querySelector("div > vt-ui-expandable.mb-3.subdomains > span > vt-ui-generic-list").shadowRoot.querySelector("div > div.tbody")'

    async def get(self, domain):
        endpoint_url = f"https://www.virustotal.com/gui/domain/{domain}/relations"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)

            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.125'
            )
            page = await context.new_page()

            await page.goto(endpoint_url, wait_until='networkidle')

            evaluate_query = f'''
                () => {{
                    return {self.CLICK_SELECTOR}.getAttribute("hidden") === null;
                }}
            '''

            evaluate_click = f'''
                () => {{
                    {self.CLICK_SELECTOR}.click();
                }}
            '''

            evaluate_contents = f'''
                () => {self.CONTENTS_SELECTOR}.innerHTML;
            '''

            while await page.evaluate(evaluate_query):
                await page.evaluate(evaluate_click)
                await page.wait_for_timeout(500)

            contents = await page.evaluate(evaluate_contents)

            await context.close()
            await browser.close()

        return parse_html(contents)
