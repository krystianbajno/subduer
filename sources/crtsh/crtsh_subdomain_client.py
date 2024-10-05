# https://crt.sh/?q=nask.pl

from typing import List

import httpx
from models.entry import Entry
from sources.crtsh.crtsh_html_subdomain_parser import parse_html
from sources.source import Source

class CrtshSubdomainClient(Source):
    async def get(self, domain) -> List[Entry]:
        endpoint_url = f"https://crt.sh/?q={domain}"
        
        client = httpx.AsyncClient(
            timeout=30, 
            headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
        )
        
        res = await client.get(endpoint_url)
        
        html = res.text
            
        return parse_html(html)