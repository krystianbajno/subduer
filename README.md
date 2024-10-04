# subduer

<img src="https://raw.githubusercontent.com/krystianbajno/krystianbajno/main/img/subduer.png"/>

Subduer is a tool for passive reconnaissance, focusing on discovering subdomains for a given domain. It uses Playwright to scrape data from several online providers and generates wordlists and reports in .csv and .json formats.

# Usage

```bash
bash install.sh
python3 subduer.py <domain> # Scanning a domain
python3 subduer.py <domain> --report # Scanning a domain and saving the reports
```

# Reports
Subduer saves reports in following formats:

- `subdomains_report_subduer_example.com.csv` - CSV report
- `subdomains_report_subduer_example.com.json` - JSON report
- `subdomains_report_subduer_example.com.txt` - Newline separated wordlist

# Providers
- VirusTotal
- Merklemap
