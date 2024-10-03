from playwright.async_api import async_playwright
from merklemap.merklemap_html_subdomain_parser import parse_html

PAGINATION_COUNT = 'document.querySelector("body > div.w-full > div > div > main > div > div > div > div > div.py-2.px-2.flex.justify-end.items-center > div > span > span:nth-child(2)")'
CONTENTS = 'document.querySelector("body > div.w-full > div > div > main > div > div > div > div > div.p-4.z-0.flex.flex-col.relative.justify-between.gap-4.bg-content1.overflow-auto.rounded-large.shadow-small.w-full")'
LOADING_SELECTOR = 'body > div.w-full > div > div > main > div > div > div > div > div.space-y-4.pt-10 > div > div.flex.items-center.justify-between.w-full.sm\:w-auto > div.flex.items-center > span'

class MerklemapSubdomainClient:

    async def get(self, domain):
        transformed_domain = "*." + domain
        pagination_index = 1
        endpoint_url = f"https://www.merklemap.com/search?query={transformed_domain}&page={pagination_index}"
        
        all_content = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)

            context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.125'
            )
            page = await context.new_page()

            await page.goto(endpoint_url, wait_until="load")
            await page.wait_for_selector(LOADING_SELECTOR, state='detached')
            
            evaluate_pagination_count = f'''
                () => {{
                    return {PAGINATION_COUNT}.innerHTML
                }}
            '''
            
            pagination_count = int(await page.evaluate(evaluate_pagination_count))
            
            while pagination_index <= pagination_count: 
                try:
                    endpoint_url = f"https://www.merklemap.com/search?query={transformed_domain}&page={pagination_index}"
                    
                    if pagination_index != 1:
                        await page.goto(endpoint_url, wait_until="load")
                        await page.wait_for_selector(LOADING_SELECTOR, state='detached')
                        
                    evaluate_contents = f'''
                        () => {CONTENTS}.innerHTML;
                    '''
                    
                    contents = await page.evaluate(evaluate_contents)
                    all_content.append(contents)
                    
                except:
                    print(f"Error happened at {endpoint_url}, continuing")
                
                pagination_index = pagination_index + 1
                
            await context.close()
            await browser.close()
            
        return parse_html(all_content)

