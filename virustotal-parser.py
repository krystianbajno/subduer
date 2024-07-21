#!/usr/bin/python
import argparse
import asyncio

from virustotal.results_saver import save_results
from virustotal.virus_total_subdomain_client import VirusTotalSubdomainClient

async def main():
    with open("./logo.txt", "r") as logo:
        print(logo.read())
        
    parser = argparse.ArgumentParser("virustotal-parser.py")
    parser.add_argument("domain", help="Domain to search", type=str)
    args = parser.parse_args()
    
    domain = args.domain
    
    client = VirusTotalSubdomainClient()
    data = await client.get(domain)
    save_results(data)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
