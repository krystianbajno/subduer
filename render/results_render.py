from render.cli import GREY, BOLD, GREEN, RESET


def format_date_range(entry):
    if not entry.dates:
        return ""

    sorted_dates = sorted(entry.dates)
    oldest_date = sorted_dates[0].strftime("%Y-%m-%d")
    newest_date = sorted_dates[-1].strftime("%Y-%m-%d")
    
    return f"{GREY}{oldest_date} - {newest_date}{RESET}"

def print_results(entries, query):
    print(f"[{GREEN}+{RESET}] Results for {BOLD}{query}{RESET}:\n")
    
    for entry in entries:
        domains_component = GREEN + ", ".join(entry.domains) + RESET
        dates_component = format_date_range(entry)

        if dates_component:
            print(f"{domains_component} :: {dates_component}")
        else:
            print(f"{domains_component}")

        if entry.ips:
            ips_component = "\n".join(f"  {GREEN}-{RESET} {ip}" for ip in entry.ips)
            print(ips_component)
            
    print("")
