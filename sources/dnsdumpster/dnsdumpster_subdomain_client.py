import time
from typing import List
from playwright.async_api import async_playwright
from models.entry import Entry
from sources.dnsdumpster.dns_dumpster_xlsx_subdomain_parser import parse_xlsx
from sources.source import Source
import os

INPUT_SELECTOR = '#target'
SUBMIT_SELECTOR = '#wp--skip-link--target > div > div.wp-block-group.has-global-padding.is-layout-constrained.wp-container-core-group-is-layout-5.wp-block-group-is-layout-constrained > form > button'
DOWNLOAD_SELECTOR = '#results > div.wp-block-buttons.is-layout-flex.wp-container-core-buttons-is-layout-1.wp-block-buttons-is-layout-flex > div > a'

class DnsdumpsterSubdomainClient(Source):
    async def get(self, domain) -> List[Entry]:
        endpoint_url = "https://dnsdumpster.com"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)

            context = await browser.new_context(
                viewport={"width": 640, "height": 480},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.125'
            )
            page = await context.new_page()

            await page.goto(endpoint_url)
            await page.wait_for_selector(INPUT_SELECTOR, state='visible')
            
            input = page.locator(INPUT_SELECTOR)
            await input.type(domain)
            
            submit = page.locator(SUBMIT_SELECTOR)
            await submit.click()
                        
            download = page.locator(DOWNLOAD_SELECTOR)
            
            async with page.expect_download() as download_info:
                await download.click()
                
            download_value = await download_info.value
            
            download_path = f"dns_dumpster_temporary_{domain}"
            await download_value.save_as(download_path)
            
            with open(download_path, "rb") as file:
                download_data = file.read()
            
            os.remove(download_path)
        
            await context.close()
            await browser.close()
            
        return parse_xlsx(download_data)

