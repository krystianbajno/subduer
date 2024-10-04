import re
from models.entry import Entry

def map_data(data):
    domain_regex = re.compile(r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    ip_regex = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    date_regex = re.compile(r'''
        (?:(\d{2})[\/\-\.](\d{2})[\/\-\.](\d{4})) |  # Matches DD/MM/YYYY or MM-DD-YYYY or YYYY.MM.DD or YYYY/MM/DD
        (?:(\d{4})[\/\-\.](\d{2})[\/\-\.](\d{2})) |  # Matches YYYY/MM/DD
        (?:(\d{2})\s([A-Za-z]+)\s(\d{4}))            # Matches DD Month YYYY
    ''', re.VERBOSE)

    entries = []
    
    for item in data:
        entry = Entry()
        for element in item:
            if element is None:
                continue
            if ip_regex.match(element):
                entry.add_ip(element)
            elif domain_regex.match(element):
                entry.add_domain(element)
            elif date_regex.match(element):
                entry.add_date(element)
                
        entries.append(entry)

    return entries
