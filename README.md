# subduetotal.py

```                                                                                                 VirusTotal Parser
Subdomain OSINT tool made with <3 
Krystian Bajno 2024
```

# Usage
This tool prints out the subdomains to stdout, and saves the results report into a .csv file
.
```bash
python3 subduetotal.py <domain>
```

The parser uses Puppeteer and will open an instance of chrome in order to scrap the domains from VirusTotal.