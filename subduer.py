#!/usr/bin/python

import argparse
import asyncio

from merklemap.merklemap_subdomain_client import MerklemapSubdomainClient
from render.logo_render import print_logo
from render.results_render import print_results
from report.results_saver import save_results
from virustotal.virustotal_subdomain_client import VirusTotalSubdomainClient

import warnings
warnings.filterwarnings("ignore")

async def main():
    parser = argparse.ArgumentParser("subduer.py")
    parser.add_argument("domain", help="Domain to search", type=str)
    parser.add_argument("--report", help="Save .json and .csv report", required=False, action="store_true")

    args = parser.parse_args()
    
    domain = args.domain
    
    print_logo() 
    
    providers = [
        VirusTotalSubdomainClient(),
        MerklemapSubdomainClient()
    ]
    
    output_data = []
    for provider in providers:
        data = await provider.get(domain)
        output_data.extend(data)

    print_results(output_data, domain)
    
    
    save_results(output_data, domain)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
