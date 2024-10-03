import csv
import json

def save_to_csv(entries, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Domains', 'IPs'])

        for entry in entries:
            writer.writerow([';'.join(entry.domains), ';'.join(entry.ips)])
    
    print(f"[+] Saved CSV report to {filename}")

def save_to_json(entries, filename):
    with open(filename, mode='w') as file:
        json.dump([{"domains": entry.domains, "ips": entry.ips} for entry in entries], file, indent=4)
        
    print(f"[+] Saved JSON report to {filename}")

def save_results(entries, query):
    filename_csv = f"subdomains_report_subduer_{query}.csv"
    filename_json = f"subdomains_report_subduer_{query}.json"
    
    save_to_csv(entries, filename_csv)
    save_to_json(entries, filename_json)