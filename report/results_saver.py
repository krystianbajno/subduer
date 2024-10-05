import csv
import json

def save_to_csv(entries, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Domain', 'IPs', 'Dates'])

        for entry in entries:
            writer.writerow([';'.join(entry.domains), ';'.join(entry.ips), ';'.join(entry.get_str_dates())])
    
    print(f"[+] Saved CSV report to {filename}")
    
def save_domain_list(entries, filename):
    domains = []
    
    for entry in entries:
        for domain in entry.domains:
            if domain in domains:
                continue
            domains.append(domain)
            
    with open(filename, mode='w') as file:
        file.write("\n".join(domains))
    
    print(f"[+] Saved domain list to {filename}")

def save_to_json(entries, filename):
    with open(filename, mode='w') as file:
        json.dump([{"domain": entry.domains[0], "ips": entry.ips, "dates": entry.get_str_dates()} for entry in entries], file, indent=4)
        
    print(f"[+] Saved JSON report to {filename}")

def save_results(entries, query):
    filename_csv = f"subdomains_report_subduer_{query}.csv"
    filename_json = f"subdomains_report_subduer_{query}.json"
    filename_domains = f"subdomains_report_subduer_domains_{query}.txt"

    save_to_csv(entries, filename_csv)
    save_to_json(entries, filename_json)
    save_domain_list(entries, filename_domains)