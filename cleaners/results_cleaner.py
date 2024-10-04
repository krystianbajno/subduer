from typing import List
from models.entry import Entry

def clean_entries(entries: List[Entry]) -> List[Entry]:
    domain_to_entry = {}

    def merge_ips_and_dates(existing_entry: Entry, copy_entry: Entry):
        for ip in copy_entry.ips:
            existing_entry.add_ip(ip)
        
        for date in copy_entry.dates:
            existing_entry.add_date(date)

    for entry in entries:
        for domain in entry.domains:
            if domain not in domain_to_entry:
                new_entry = Entry()
                new_entry.add_domain(domain)
                new_entry.ips = entry.ips.copy()
                new_entry.dates = entry.dates.copy()
                domain_to_entry[domain] = new_entry
            else:
                merge_ips_and_dates(domain_to_entry[domain], entry)

    return list(domain_to_entry.values())
