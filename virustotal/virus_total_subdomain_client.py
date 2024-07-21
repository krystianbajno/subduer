from pyppeteer import launch
from virustotal.html_subdomain_parser import parse_html

class VirusTotalSubdomainClient:
    CLICK_SELECTOR = 'document.querySelector("#view-container > domain-view").shadowRoot.querySelector("#relations").shadowRoot.querySelector("div > vt-ui-expandable.mb-3.subdomains > span > div > vt-ui-button")'
    CONTENTS_SELECTOR = 'document.querySelector("#view-container > domain-view").shadowRoot.querySelector("#relations").shadowRoot.querySelector("div > vt-ui-expandable.mb-3.subdomains > span > vt-ui-generic-list").shadowRoot.querySelector("div > div.tbody")'

    async def get(self, domain):
        endpoint_url = f"https://www.virustotal.com/gui/domain/{domain}/relations"
        browser = await launch(headless=False)
        page = await browser.newPage()
        await page.setViewport({"width": 1920, "height": 1080})
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.125')
        await page.goto(endpoint_url, {"waitUntil": ['domcontentloaded', 'networkidle2']})

        evaluate_query = f'''
            () => {{
                return {self.CLICK_SELECTOR}.getAttribute("hidden") == null
            }}
        '''

        evaluate_click = f'''
            () => {{
                {self.CLICK_SELECTOR}.click()
            }}
        '''

        evaluate_contents = f'''
            () => {self.CONTENTS_SELECTOR}.innerHTML
        '''

        while await page.evaluate(evaluate_query):
            await page.evaluate(evaluate_click)
            await page.waitFor(500)

        contents = await page.evaluate(evaluate_contents)
        await browser.close()
        return parse_html(contents)