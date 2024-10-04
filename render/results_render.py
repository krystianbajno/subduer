
from render.cli import BOLD, GREEN, RESET


def print_results(entries, query):
    print(f"[{GREEN}+{RESET}] Results for {BOLD}{query}{RESET}:\n")
    for entry in entries:
        domains_component = GREEN + ", ".join(entry.domains) + RESET
        
        if entry.ips:
            ips_component = "\n  " + "\n  ".join(f"{GREEN}-{RESET} {ip}" for ip in entry.ips)
            print(f"{domains_component}{ips_component}")
        else:
            print(domains_component)
            
    print("")
