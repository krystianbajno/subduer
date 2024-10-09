# subduer

<img src="https://raw.githubusercontent.com/krystianbajno/krystianbajno/main/img/subduer.png"/>

Subduer is a tool for passive reconnaissance, focusing on discovering subdomains for a given domain. It uses Playwright to scrape data from several online providers and generates wordlists and reports in .csv and .json formats.

# Usage

```bash
bash install.sh
python3 subduer.py <domain> # Scanning a domain
python3 subduer.py <domain> --report # Scanning a domain and saving the reports
```

### Docker
```
docker build -t subduer .
docker run --rm -it subduer <domain>
docker run --rm -it -v $(pwd)/reports:/app/reports subduer example.com --report
```

# Reports
Subduer saves reports in following formats:

- `subdomains_report_subduer_example.com.csv` - CSV report
- `subdomains_report_subduer_example.com.json` - JSON report
- `subdomains_report_subduer_example.com.txt` - Newline separated wordlist

# Providers
- [VirusTotal](https://www.virustotal.com/gui/home/search)
- [Merklemap](https://www.merklemap.com)
- [DnsDumpster](https://dnsdumpster.com)
- [crt.sh](https://crt.sh/)

# Async
The tool is pretty fast as it asynchronously runs collectors.

# Fail-safe
- When collector fails to retrieve the subdomains, it retries. 
- If you abuse the service and get captcha, it is yours to solve in the opened Playwright browser. After solving the captcha, the tool will retry.
- If a source fails after specified amount of retries, the subduer will simply ignore that source and continue execution.
