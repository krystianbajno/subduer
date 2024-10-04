
from typing import List
from cleaners.results_cleaner import clean_entries
from sources.source import Source

async def get_results(domain, sources: List[Source]):
    output_data = []
    for source in sources:
        data = await source.get(domain)
        output_data.extend(data)
        
    return clean_entries(output_data)