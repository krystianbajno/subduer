#!/usr/bin/python

from bs4 import BeautifulSoup
from pyppeteer import launch
import argparse
import asyncio

async def get_subdomains(domain):
    endpoint_url = f"https://www.virustotal.com/gui/domain/{domain}/relations"
    clickSelector = 'document.querySelector("#view-container > domain-view").shadowRoot.querySelector("#relations").shadowRoot.querySelector("div > vt-ui-expandable.mb-3.subdomains > span > div > vt-ui-button")'
    contentsSelector = 'document.querySelector("#view-container > domain-view").shadowRoot.querySelector("#relations").shadowRoot.querySelector("div > vt-ui-expandable.mb-3.subdomains > span > vt-ui-generic-list").shadowRoot.querySelector("div > div.tbody")'
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({"width":1920, "height":1080})
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 OPR/68.0.3618.125')
    await page.goto(endpoint_url, { "waitUntil": ['domcontentloaded', 'networkidle2']})
    
    evaluateQuery = f'''
        () => {{
            return {clickSelector}.getAttribute("hidden") == null
        }}
    '''
    
    evaluateClick = f'''
        () => {{
            {clickSelector}.click()
        }}
    '''
    
    evaluateContents = f'''
        () => {contentsSelector}.innerHTML
    '''
    
    while await page.evaluate(evaluateQuery):
        await page.evaluate(evaluateClick)
        await page.waitFor(500)
        
    return await page.evaluate(evaluateContents)

def parse_html(html):
    minified = html
    minified = minified.replace("\n", "")
    minified = minified.replace("  ", "")

    soup = BeautifulSoup(minified, features="html.parser")
    rows = soup.find_all("div", class_="tr")

    data = []

    for row in rows:
        entry = []
        for td in row.find_all("div", class_="td", ):
            worth_rows = td.find_all(string=True)
            for worth_row in worth_rows:
                if not "?lit" in worth_row and not " " in worth_row and worth_row != "-":
                    entry.append(worth_row)
        data.append(entry)
    return data

def save_results(data): 
    with open(f"subdomains_virustotal.csv", "w") as output:
        data_output = ""
        for row in data:
            for td in row:
                data_output += f"{td},"
            data_output += "\n"
        output.write(data_output)
        print(data_output)
        
        
async def main():
    parser = argparse.ArgumentParser("virustotal-parser.py")
    parser.add_argument("domain", help="Domain to search", type=str)
    
    with open("./logo.txt", "r") as logo:
        print(logo.read())

    args = parser.parse_args()
    
    domain = args.domain
    
    response = await get_subdomains(domain)
    data = parse_html(response)
    save_results(data)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
