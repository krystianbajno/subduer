from utils.dates import normalize_date

class Entry:
    def __init__(self):
        self.ips = []
        self.domains = []
        self.dates = []
        
    def add_domain(self, domain):
        if domain not in self.domains:
            self.domains.append(domain)
        
    def add_ip(self, ip):
        if ip not in self.ips:
            self.ips.append(ip)
            
    def add_date(self, date):
        if type(date) is str:
            date = normalize_date(date)
        self.dates.append(date)
        
    def get_str_dates(self):
        return list([str(x) for x in self.dates])
        
    def __repr__(self):
        return f"{self.domains} = {self.ips}"
        