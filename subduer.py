#!/usr/bin/python

import argparse
import asyncio

from sources.crtsh.crtsh_subdomain_client import CrtshSubdomainClient
from sources.dnsdumpster.dnsdumpster_subdomain_client import DnsdumpsterSubdomainClient
from render.logo_render import print_logo
from render.results_render import print_results
from report.results_saver import save_results
from sources.merklemap.merklemap_subdomain_client import MerklemapSubdomainClient
from sources.source_service import get_results
from sources.virustotal.virustotal_subdomain_client import VirusTotalSubdomainClient

async def main():
    parser = argparse.ArgumentParser("subduer.py")
    parser.add_argument("domain", help="Domain to search", type=str)
    parser.add_argument("--report", help="Save .json and .csv report", required=False, action="store_true")

    args = parser.parse_args()

    domain = args.domain
    
    print_logo()
    
    providers = [
        DnsdumpsterSubdomainClient(),
        VirusTotalSubdomainClient(),
        MerklemapSubdomainClient(),
        CrtshSubdomainClient()
    ]
    
    results = await get_results(domain, providers)
    
    print_results(results, domain)
    
    if args.report:
        save_results(results, domain)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
