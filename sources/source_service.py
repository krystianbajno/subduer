import asyncio
from typing import List
from cleaners.results_cleaner import clean_entries
from models.entry import Entry
from sources.source import Source

async def get_results(domain, sources: List[Source]):
    output_data = []
    retries = 5
    
    counter = {
        "index": 0,
        "total": len(sources)
    }
    
    def get_counter_index(counter):
        return counter["index"]
    
    def get_counter_total(counter):
        return counter["total"]
    
    def add_counter_index(counter):
        counter["index"] = counter["index"] + 1
        
    async def collect_from_source(source: Source, counter) -> List[Entry]:
        for retry in range(retries):
            try:
                data = await source.get(domain)
                add_counter_index(counter)
                print(f"[{get_counter_index(counter)}/{get_counter_total(counter)}] {source.__class__.__name__} source collection complete.")
                return data
            except Exception as e:
                print(f"[!] {source.__class__.__name__} attempt {retry + 1}/{retries} failed. Retrying...")
            
        add_counter_index(counter)
        print(f"[!] {source.__class__.__name__} failed after {retries} attempts.")
        return []

    tasks = [collect_from_source(source, counter) for source in sources]
    results = await asyncio.gather(*tasks)

    for result in results:
        output_data.extend(result)

    return clean_entries(output_data)
