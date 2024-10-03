import re
from models.entry import Entry

def map_data(data):
    domain_regex = re.compile(r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    ip_regex = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    entries = []

    for item in data:
        entry = Entry()
        for element in item:
            if ip_regex.match(element):
                entry.add_ip(element)
            elif domain_regex.match(element):
                entry.add_domain(element)
        entries.append(entry)

    return entries
